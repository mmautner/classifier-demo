#!/usr/bin/env python

from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords

LEMMATIZER = WordNetLemmatizer()
STOP_SET = set(stopwords.words('english'))

def get_words(filename):
    """returns a generator that allows iteration over the words in the 
    document, so that the entire document doesn't need to be loaded into 
    memory. Read up about generators here: http://www.dabeaz.com/generators/

    If a word is contained in the set of stop words, then it is ignored.
    Examples of stop words include "the", "it", "so"
    """
    for line in open('data/%s.txt' % filename):
        for word in word_tokenize(line):
            if word in STOP_SET:
                continue
            yield word

def lemmatize(word, lemmatizer=LEMMATIZER):
    """Lowercases and lemmatizes the given word using the given lemmatizer.
    For information about lemmatization: http://en.wikipedia.org/wiki/Lemmatisation
    """
    return lemmatizer.lemmatize(word.lower())

def word_features(filename):
    """iterate over a text file and construct a dictionary of lemmatized words
    as keys, and a given key's existence in the dictionary as a feature by 
    which to train a model.
    """

    words = get_words(filename)
    return {"contains(%s)" % lemmatize(word): True for word in words}


if __name__=="__main__":

    nytimes = [(word_features("nytimes"), "Nytimes")]
    nytimes2 = [(word_features("nytimes2"), "Nytimes")]
    nytimes3 = [(word_features("nytimes3"), "Nytimes")]
    nytimes4 = [(word_features("nytimes4"), "Nytimes")]
    nltk_data = [(word_features("nltk"), "NLTK")]
    nltk_data2 = [(word_features("nltk2"), "NLTK")]
    nltk_data3 = [(word_features("nltk3"), "NLTK")]
    feature_set = nytimes + nytimes2 + nytimes3 + nytimes4 + nltk_data + nltk_data2 + nltk_data3 
    classifier = nltk.NaiveBayesClassifier.train(feature_set)
    #classifier.show_most_informative_features(5)

    print 'nltk4: ', classifier.classify(word_features("nltk4"))
    print 'nytimes5: ', classifier.classify(word_features("nytimes5"))
    print 'jezebel: ', classifier.classify(word_features("jezebel"))
