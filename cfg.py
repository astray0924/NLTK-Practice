# -*- coding: utf-8 -*-
import nltk

if __name__ == '__main__':
    grammar1 = nltk.parse_cfg("""
        S -> NP VP
        VP -> V NP | V NP PP
        PP -> P NP
        V -> "saw" | "ate" | "walked"
        NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
        Det -> "a" | "an" | "the" | "my"
        N -> "man" | "dog" | "cat" | "telescope" | "park"
        P -> "in" | "on" | "by" | "with"
        """)
    
#    sent = "Mary saw Bob".split()
    sent = "the dog saw a man in the park".split()
    rd_parser = nltk.RecursiveDescentParser(grammar1)
    for tree in rd_parser.nbest_parse(sent):
        print tree