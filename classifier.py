#!/usr/bin/env python

from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords

stop_set = set(stopwords.words('english'))

def get_words(pub):
    for line in open('%s.txt' % pub):
        for word in word_tokenize(line):
            if word in stop_set:
                continue
            yield word

def word_features(pub):
    words = get_words(pub)
    print type(words)
    return {"contains(%s)" % lemmatize(word): True for word in words}


if __name__=="__main__":
    lemmatizer = WordNetLemmatizer()
    lemmatize = lambda word: lemmatizer.lemmatize(word.lower())

    nytimes = [(word_features("nytimes"), "Nytimes")]
    nytimes2 = [(word_features("nytimes2"), "Nytimes")]
    nytimes3 = [(word_features("nytimes3"), "Nytimes")]
    nytimes4 = [(word_features("nytimes4"), "Nytimes")]
    nltk_data = [(word_features("nltk"), "NLTK")]
    nltk_data2 = [(word_features("nltk2"), "NLTK")]
    nltk_data3 = [(word_features("nltk3"), "NLTK")]
    feature_set = nytimes + nytimes2 + nytimes3 + nytimes4 + nltk_data + nltk_data2 + nltk_data3 
    classifier = nltk.NaiveBayesClassifier.train(feature_set)

    print 'nltk4: ', classifier.classify(word_features("nltk4"))
    print 'nytimes5: ', classifier.classify(word_features("nytimes5"))
    print 'jezebel: ', classifier.classify(word_features("jezebel"))
