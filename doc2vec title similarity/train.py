import gensim
import os
import collections
import smart_open
import random
from gensim import utils
from gensim.models.doc2vec import LabeledSentence
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from pprint import pprint
import multiprocessing

#https://github.com/RaRe-Technologies/gensim/tree/develop/docs/notebooks
filename = "/media/verma314/Windows/MAG Files/IR_training_dump.txt"

class LabeledLineSentence(object):
    def __init__(self, filename):
        self.filename = filename
    def __iter__(self):
        for line in open(filename,"r"):
            string  = line.strip().split('\t')
            yield LabeledSentence(words=string[1].split(), tags=[string[0]])


it = LabeledLineSentence(filename)

cores = multiprocessing.cpu_count()

model =Doc2Vec(dm=1, dm_mean=1, size=200, window=8, min_count=19, iter =10, workers=cores)
model.build_vocab(it)

model.train(it, total_examples=model.corpus_count, epochs=model.iter)

model.save('my_model2HUGE.doc2vec')

#pprint(model.docvecs.most_similar(positive=["Machine learning"], topn=20))

