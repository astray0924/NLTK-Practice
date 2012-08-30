# -*- coding: utf-8 -*-
from nltk import load_parser

if __name__ == '__main__':
    tokens = "Kim likes children".split()
    cp = load_parser('grammars/book_grammars/feat0.fcfg', trace=2)
    trees = cp.nbest_parse(tokens)
    for tree in trees:
        print tree
    