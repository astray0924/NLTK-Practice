# -*- coding: utf-8 -*-
from nltk.corpus import brown, movie_reviews
import nltk
import random

def pos_features(word):
    features = {}
    for suffix in common_suffixes:
        features['endswith(%s)' % suffix] = word.lower().endswith(suffix)
    return features

if __name__ == '__main__':
    # 사용할 feature 생성
    suffix_fdist = nltk.FreqDist()
    for word in brown.words():
        word = word.lower()
        suffix_fdist.inc(word[-1:])
        suffix_fdist.inc(word[-2:])
        suffix_fdist.inc(word[-3:])
    common_suffixes = suffix_fdist.keys()[:100]

    # feature를 이용해서 DecisionTreeClassifier를 훈련함
    tagged_words = brown.tagged_words(categories='news')
    featuresets = [(pos_features(n), g) for (n, g) in tagged_words]
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    
    classifier = nltk.DecisionTreeClassifier.train(train_set)
    print nltk.classify.accuracy(classifier, test_set)