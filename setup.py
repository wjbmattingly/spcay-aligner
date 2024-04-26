from setuptools import setup, find_packages

setup(
    name='spacy_aligner',
    version='0.0.1',
    author='William J.B. Mattingly',
    description='A spaCy component for connecting entities and building relational graphs in text.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/wjbmattingly/spacy_aligner',  # Change this to your repository URL
    packages=find_packages(),
    install_requires=[
        'spacy',
        'networkx'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    python_requires='>=3.7'
)
