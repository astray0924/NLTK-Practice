# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import names
from nltk.classify import apply_features
import random

def gender_features(word):
    return {'suffix1': word[-1], 'suffix2': word[-2:], 'length': len(word), 'first_letter': word[0]}

def gender_features_overfitting(name):
    features = {}
    features["firstletter"] = name[0].lower()
    features["lastletter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count(%s)" % letter] = name.lower().count(letter)
        features["has(%s)" % letter] = (letter in name.lower())        
    return features

if __name__ == '__main__':
    # 코퍼스에서 이름 가져와서 랜덤 소트
    names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
    random.shuffle(names)

    # error analysis를 위해 이름 셋을 나눔
    train_names = names[1500:]
    devtest_names = names[500:1500]
    test_names = names[:500]
    
    # train set 생성
    train_set = [(gender_features(n), g) for (n, g) in train_names]
    devtest_set = [(gender_features(n), g) for (n, g) in devtest_names]
    test_set = [(gender_features(n), g) for (n, g) in test_names]
    
    # NB 훈련
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    
    print nltk.classify.accuracy(classifier, test_set)
    
    # error analysis
    errors = []
    for (name, tag) in devtest_names:
        guess = classifier.classify(gender_features(name))
        if guess != tag:
            errors.append((tag, guess, name))
            
    for (tag, guess, name) in sorted(errors):
        print 'correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name)
