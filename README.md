# Contrastive Keyword Extraction (CKE) from Versioned Documents

Unsupervised Approach for Automatic Summarization (using Keywords) of Changes between two Document Versions 

## Introduction

Keyword Extraction (KE) in its original form is defined as the automatic identification of terms that best describe the subject of a
document. KE has been successfully applied to many tasks as a
special form of document summarization. Unlike traditional
document summarization, in KE the created summary of a document does not consist of entire sentences but rather of a set of the
most informative words or n-grams. In this work, we focus on a
novel setting of keyword extraction that is applicable to versioned
documents. In particular, we propose a novel task called Contrastive
Keyword Extraction (CKE) which is defined as the summarization of
changes between two versions of the same document. This is where
Contrastive Keyword Extraction is fundamentally different from existing in-place diff tools, since it does not only extract differences
between text versions, but it also ranks these differences based on
how much they altered the meaning of the document. This could
be especially useful when the amount of change is large (e.g., a
substantial revision of a long document, such as a novel or a legal
contract) and can be used to quickly summarize changes made to a
document or even a collection of documents over time.

## Try it yourself:
<a href="https://contrastive-keyword-extraction.streamlit.app"><strong>Open WebInterface »</strong></a>

<a href="https://colab.research.google.com/github/LukasEder1/ContrastiveKeywordExtraction/blob/main/demo/CKE-demo.ipynb"><strong>Open Google Colab Notebook: »</strong></a>



## Installing CKE

#### Requirements

Python3

#### Installation

To install CKE using pip:

``` bash
pip install git+https://github.com/LukasEder1/ContrastiveKeywordExtraction
```

To upgrade using pip:

``` bash
pip install git+https://github.com/LukasEder1/ContrastiveKeywordExtraction –-upgrade
```

### Usage 

#### Using default parameters

``` python
from cke import extract_contrastive_keywords

combined_kws, former_kws, latter_kws = extract_contrastive_keywords(document_a, document_b)
```

Parameters:

  * ``document_a``: Older Document Version (string)
  
  * ``document_b``: Newer Document Version (string)

#### Specifying more indepth parameters
```python
from cke.sentence_comparision import match_sentences_semantic_search
from cke.sentence_importance import yake_weighted_importance
import string
import nltk

num_keywords = 10
max_ngram = 2
min_ngram = 1
threshold = 0.6
model = 'all-MiniLM-L6-v2'
num_splits = 1
symbols_to_remove = string.punctuation
stopwords = nltk.corpus.stopwords.words("english")

combined_kws, former_kws, latter_kws = extract_contrastive_keywords(document_a,
                                                                    document_b,
                                                                    num_keywords
                                                                    max_ngram=max_ngram,
                                                                    min_ngram=min_ngram,
                                                                    extra_stopwords=stopwords,
                                                                    importance_estimator= yake_weighted_importance,
                                                                    match_sentences=match_sentences_semantic_search,
                                                                    matching_model=model,
                                                                    threshold=threshold,
                                                                    symbols_to_remove=string.punctuation,
                                                                    num_splits=num_splits)

```

Parameters:
* ``document_a``: Older Document Version (string)

* ``document_b``: Newer Document Version (string)

* ``num_keywords``: Number of Keywords to Extract (default=10)

* ``max_ngram``: Maximum n-gram size of Keyphrases (default=2)

* ``min_ngram``: Minimum n-gram size of Keyphrases (default=1)

* ``extra_stopwords``: List of Stop words that should not be used as keywords (default=[])

* ``importance_estimator``: Importance Calculator -> Predefined in ``cke.sentence_importance``: ``yake_weighted_importance`` or ``text_rank_importance``

* ``match_sentences``: Sentence Matching Algorithm -> Predefined in ``cke.sentence_comparision``: ``match_sentences_semantic_search`` or ``match_sentences_tfidf_weighted``

* ``matching_model``: Transformer Model for Semantic Search (default='all-MiniLM-L6-v2'): https://www.sbert.net/examples/applications/semantic-search/README.html

* ``threshold``:  Matching Threshold: acts as a lowerbound for whether or not two sentences should match (default=0.6)

* ``symbols_to_remove``: List of Symbols that should be removed (defaul=[,])

* ``num_splits``: Maximum Number Sentence a Source Sentence can split into (default=1)

#### Output


