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

### Example
Using the first and the last revised version of the AP-News Article with id 17313 from the AP news-edits dataset ([Google Drive](https://drive.google.com/drive/folders/17a5S3liA0C91XbgnMBUQBo-NVb22Z9xf?usp=sharing))

Also available in the demo notebook (using documents[17313])

```python
from cke import extract_contrastive_keywords

document_a, document_b = documents[17313]

combined_kws, former_kws, latter_kws = extract_contrastive_keywords(document_a, document_b, num_keywords=10, max_ngram=2)
```

#### Output

##### Combined Keywords
```python
print(combined_kws)
```

```python
{'state transportation': 0.16218195157227563,
 'transportation taxes': 0.16218195157227563,
 'new york': 0.11901325999183027,
 'records show': 0.11021500265104711,
 'york city': 0.09940959219076993,
 'city yellow': 0.09940959219076993,
 'taxes': 0.07831640607467383,
 'also sought': 0.06403374274208463,
 'attorneyclient privilege': 0.05739060614971311,
 'medallions': 0.047847894864559946}
```

##### Former Keywords
```python
print(former_kws)
```

```python
{'attorneyclient privilege': 0.14622844020560088,
 'fbi agents': 0.11396681642987444,
 'fire mueller': 0.107559144093367,
 'dead': 0.09032079989587966,
 'furious president': 0.09032079989587966,
 'president blasted': 0.09032079989587966,
 'blasted displeasure': 0.09032079989587966,
 'displeasure early': 0.09032079989587966,
 'early tuesday': 0.09032079989587966,
 'tuesday saying': 0.09032079989587966}
```

##### Latter Keywords
```python
print(latter_kws)
```

```python
{'state transportation': 0.1641493556133856,
 'transportation taxes': 0.1641493556133856,
 'new york': 0.12041330413087999,
 'records show': 0.11155200371377005,
 'york city': 0.10061551449904882,
 'city yellow': 0.10061551449904882,
 'taxes': 0.07926645022140402,
 'also sought': 0.0648105261203635,
 'medallions': 0.04842833023854907,
 'pleaded guilty': 0.0459996453501646}
```

## Citation
If you use CKE in your own work please consider citing the following Paper. The Paper can be found at [pdf](https://dl.acm.org/doi/10.1145/3583780.3614735).
```
Lukas Eder, Ricardo Campos and Adam Jatowt: Contrastive Keyword Extraction from Versioned Documents,
Proceedings of the 32nd ACM International Conference on Information and Knowledge Management (CIKM 2023),
ACM Press, pp. 5026-5030 (2023)
```

```
@inproceedings{10.1145/3583780.3614735,
author = {Eder, Lukas and Campos, Ricardo and Jatowt, Adam},
title = {Contrastive Keyword Extraction from Versioned Documents},
year = {2023},
isbn = {9798400701245},
publisher = {Association for Computing Machinery},
url = {https://doi.org/10.1145/3583780.3614735},
doi = {10.1145/3583780.3614735},
booktitle = {Proceedings of the 32nd ACM International Conference on Information and Knowledge Management},
pages = {5026–5030},
numpages = {5},
keywords = {keyword extraction, comparative summarization, change analysis},
location = {Birmingham, United Kingdom},
series = {CIKM '23}
}
```


