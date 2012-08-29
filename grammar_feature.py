# -*- coding: utf-8 -*-
kim = {'CAT': 'NP', 'ORTH': 'Kim', 'REF': 'k'}
chase = {'CAT': 'V', 'ORTH': 'chased', 'REL': 'chase', 'AGT': 'sbj', 'PAT': 'obj'}
lee = {'CAT': 'NP', 'ORTH': 'Lee', 'REF': 'l'}
surprise = {'CAT': 'V', 'ORTH': 'surprised', 'REL': 'surprise', 'SRC': 'sbj', 'EXP': 'obj'}

def lex2fs(word):
    for fs in [kim, lee, chase]:
        if fs['ORTH'] == word:
            return fs

if __name__ == '__main__':
    # 시작
    sent = 'Kim chased Lee'
    tokens = sent.split()
    subj, verb, obj = lex2fs(tokens[0]), lex2fs(tokens[1]), lex2fs(tokens[2])
    verb['AGT'] = subj['REF']       # agent of 'chase' is Kim
    verb['PAT'] = obj['REF']        # patient of 'chase' is Lee
    for k in ['ORTH', 'REL', 'AGT', 'PAT']:     # check featstruct of 'chase'
        print "%-5s => %s" % (k, verb[k])