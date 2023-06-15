import yake

def extract_yake(documents, language="en", max_ngram_size=1, 
                 deduplication_threshold = 0.9, deduplication_algo = 'seqm',
                 windowSize=1,numOfKeywords=10):
    number_of_documents = len(documents)
    kws = {version:[] for version in range(number_of_documents)}
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, 
                                                dedupLim=deduplication_threshold,dedupFunc=deduplication_algo, 
                                                windowsSize=windowSize, top=numOfKeywords, features=None)
    
    for current in range(number_of_documents):
        kws[current] = custom_kw_extractor.extract_keywords(documents[current])
            
    return kws
            
