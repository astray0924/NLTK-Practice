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
    rd_parser = nltk.RecursiveDescentParser(grammar1, trace=2)
    sent = 'Mary saw a dog'.split()
    for t in rd_parser.nbest_parse(sent):
        print t
