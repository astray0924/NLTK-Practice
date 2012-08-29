# -*- coding: utf-8 -*-
import nltk
import re
import pprint
from nltk.corpus import conll2000

def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    
def simple_nount_phrase_chunker():
    grammar = r"""
        NP: {<DT|PP\$>?<JJ>*<NN>}        # chunk determiner/possessive, adjectives and nouns
            {<NNP>+}                     # chunk sequences of proper nouns
    """
    cp = nltk.RegexpParser(grammar)
    sentence = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"),
                    ("her", "PP$"), ("long", "JJ"), ("golden", "JJ"), ("hair", "NN")]
    
    print cp.parse(sentence)

def find_chunks(corpus, chunk_string):
    cp = nltk.RegexpParser(chunk_string)
    tag = chunk_string.split(':')[0]
    for sent in corpus.tagged_sents():
        tree = cp.parse(sent)
        for subtree in tree.subtrees():
            if subtree.node == tag: print subtree

def simple_chinker():
    grammar = r"""
        NP:
            {<.*>+}                    # chunk everything
            }<VBD|IN>+{                # chink sequences of VBD and IN
    """
    sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),
            ("dog", "NN"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
    cp = nltk.RegexpParser(grammar)
    
    print cp.parse(sentence)

class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags]]

if __name__ == '__main__':
    pass