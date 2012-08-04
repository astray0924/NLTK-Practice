# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import names
from nltk.classify import apply_features
import random

def gender_features(word):
    return {'last_letter': word[-1], 'length': len(word), 'first_letter': word[0], 'last_two_letter': word[-2:]}

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

    # feature를 뽑고 NB를 훈련시킴
#    featuresets = [(gender_features(n), g) for (n, g) in names]
#    train_set, test_set = featuresets[500:], featuresets[:500]    # 이러면 메모리를 많이 소비함
    train_set = apply_features(gender_features, names[500:])
    test_set = apply_features(gender_features, names[:500])
    
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print nltk.classify.accuracy(classifier, test_set)
    classifier.show_most_informative_features(5)