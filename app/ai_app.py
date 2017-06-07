"""
ai.py

configure AI application
"""

"""
generate text using LSTM
reference: https://vivshaw.github.io/blog/electric-pentameter/
"""

import numpy as np
from keras.models import model_from_yaml
from random import randint
from ai import corpusFile, modelFile, weightFile

def lstm_generate(seed):

        #============
        # Load Corpus
        #============

        # use ngasal.txt as text corpus
        with open(corpusFile) as corpus_file:
        	corpus = corpus_file.read()

        # get unique identifier for each unique char
        chars = sorted(list(set(corpus)))

        # create lexicon/dict with index as integer
        encoding = {c: i for i, c in enumerate(chars)} #i=index(uniq int), c=char
        decoding = {i: c for i, c in enumerate(chars)}

        # useful variables
        num_chars = len(chars) # number of uniq chars
        sentence_length = 50
        corpus_length = len(corpus)


        #============
        # Load Model
        #============
        with open(modelFile) as model_file:
        	architecture = model_file.read()

        model = model_from_yaml(architecture)
        model.load_weights(weightFile)
        model.compile(loss='categorical_crossentropy', optimizer='adam')

        #============
        # Feed Seed Phrase
        #============
        seed_phrase = seed

        X = np.zeros((1, sentence_length, num_chars))
        for i, character in enumerate(seed_phrase):
        	X[0, i, encoding[character]] = 1

        #============
        # Generate Text
        #============
        generated_text = ""
        # generate 500 chars
        for i in range(100):
        	prediction = np.argmax(model.predict(X, verbose=0))

        	# append to resulting text
        	generated_text += decoding[prediction] # convert to char

        	# create one-hot encoded vector
        	activations = np.zeros((1, 1, num_chars), dtype=np.bool)
        	activations[0, 0, prediction] = 1
        	# omit 1st char from old vector, append new predicted char as seed
        	X = np.concatenate((X[:, 1:, :], activations), axis=1)

        return generated_text
