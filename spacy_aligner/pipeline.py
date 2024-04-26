import networkx as nx
from collections import defaultdict
from spacy.language import Language
from spacy.tokens import Doc

# Setting up extensions
Doc.set_extension("connections", default=defaultdict(list))
Doc.set_extension("graph", default=nx.Graph())
Doc.set_extension("links", default={})


DEFAULT_SPACY_CONFIG = {
        "links": {},
        "part_labels": ["PERSON"]
    }

@Language.factory("aligner", default_config=DEFAULT_SPACY_CONFIG)
class Aligner:
    def __init__(self, nlp: Language, name: str, links: dict, part_labels:list):
        self.nlp = nlp
        self.links = links
        self.part_labels = part_labels

    def __call__(self, doc):
        self._connect_parts(doc)
        self._connect_nicknames(doc)
        self._build_graph(doc)
        return doc

    def _connect_parts(self, doc):
        connections = doc._.connections

        for ent in doc.ents:
            if ent.label_ in self.part_labels:
                for token in ent:
                    connections[token.text].append(ent.text)
        doc._.connections = connections

    def _connect_nicknames(self, doc):
        connections = doc._.connections
        for label, links in self.links.items():
            for ent in doc.ents:
                if ent.label_ == label:
                    main_connected = False
                    for token in ent:
                        for main_name, variants in links.items():
                            if token.text == main_name or token.text in variants:
                                if not main_connected:
                                    connections[main_name].append([ent.text, label])
                                    main_connected = True
                                connections[token.text].append([main_name, label])
        doc._.connections = connections

    def _build_graph(self, doc):
        G = doc._.graph
        for token, entities in doc._.connections.items():
            G.add_node(token)
            for entity in entities:
                if entity != token:  # Avoid self-loops
                    G.add_edge(token, entity[0], label=entity[1])
        doc._.graph = G
