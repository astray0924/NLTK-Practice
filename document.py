# -*- coding: utf-8 -*-
from nltk.corpus import brown, movie_reviews
import nltk
import random

def pos_features(sentence, i):
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:]}
    if i == 0:
        features["prev-word"] = "<START>"
    else:
        features["prev-word"] = sentence[i - 1]
    return features

if __name__ == '__main__':
    tagged_sents = brown.tagged_sents(categories='news')
    featuresets = []
    for tagged_sent in tagged_sents:
        untagged_sent = nltk.tag.untag(tagged_sent)
        for i, (word, tag) in enumerate(tagged_sent):
            featuresets.append((pos_features(untagged_sent, i), tag))
            
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    
    print nltk.classify.accuracy(classifier, test_set)