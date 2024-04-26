# spaCy Aligner

The `spacy_aligner` is a custom spaCy component designed to connect entities in text and build relational graphs based on these connections. It utilizes both spaCy's powerful NLP capabilities and NetworkX for graph management, making it an excellent tool for complex entity relationship analysis in large texts.

## Installation

To install `spacy_aligner`, you will need Python 3.7 or newer. You can install this package directly from PyPI (once uploaded) or through the repository if it is hosted on a site like GitHub.

```bash
pip install spacy_aligner
```

Or, if you have the source code:

```bash
git clone https://github.com/yourgithub/spacy_aligner
cd spacy_aligner
python setup.py install
```

## Usage

Here's a quick start example to use `spacy_aligner`:

```python
import spacy
from spacy_aligner.pipeline import Aligner
import json
import networkx as nx
import matplotlib.pyplot as plt

# Load external data


links = {
        "PERSON": {
            "Elizabeth": ["Liz", "Lizzie", "Beth", "Betsy", "Eliza"],
            "William": ["Will", "Bill", "Billy", "Liam"],
                }
        }

# Load the spaCy model
nlp = spacy.load("en_core_web_lg")

# Add the custom pipeline component to the spaCy pipeline
nlp.add_pipe("aligner", config={"links": links})

text = """Elizabeth Jenkins went to school. She works at Mattingly Autoparts.
        Liz is 20. She also goes by Lizzie. Mrs. Jenkins teaches students.
        Once she completes her PhD, she will be Dr. Elizabeth P. Jenkins.
        William also goes by Will.
        His full name is William Mattingly."""

# Process the text
doc = nlp(text)

# Access the generated graph
G = doc._.graph
```

## Visualization

The `spacy_aligner` also includes a function to visualize the relationship graph generated:

```python
def visualize_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray', linewidths=1, font_size=12)
    plt.show()

visualize_graph(doc._.graph)
```

This function uses `matplotlib` to plot the graph, showing the relationships between detected entities based on the document text.