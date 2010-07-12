'''
Created on Jul 11, 2010

@author: vasco
'''

from nltk.corpus import wordnet as wn
import itertools

def flatten(lst):
    for elem in lst:
        if type(elem) in (tuple,list):
            for e in flatten(elem):
                yield e
        else:
            yield elem

def get_type_expansion(name,shallow=False,unique=True):
    syn = get_syn(name)
    if not syn:
        return None
    
    if shallow:
        names = [lemma.replace("_"," ") for lemma  in syn.lemma_names]
        hyps = syn.hyponyms()
    else:
        names = []
        hyp = lambda s:s.hyponyms()
        hyp_tree = syn.tree(hyp)
        hyps = list(flatten(hyp_tree))

    if unique:
        # remove ambiguous lemmas
        for synset in hyps:
            ln = synset.lemma_names
            for lemma_name in ln:
                s = wn.synsets(lemma_name)
                if len(s) == 1:
                    names.append(lemma_name.replace("_"," ")) 
    else:
        for synset in hyps:
            names.extend([name.replace("_"," ") for name in synset.lemma_names])

    return names


    
        
def get_syn(typename):
    syns = wn.synsets(typename)
    if len(syns) > 0:
        return syns[0]
    else:
        return None
    
         
        

if __name__ == "__main__":
    import sys
    print (get_type_expansion(sys.argv[1],shallow=False,unique=False))
    
    
    
    
    
    