"""
import file for LSTM
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

corpusFile = os.path.join(basedir, 'ngasal.txt')
modelFile = os.path.join(basedir, 'model.yaml')
weightFile = os.path.join(basedir, 'weights-29-1.517.hdf5')
