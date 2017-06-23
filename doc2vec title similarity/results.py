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
filename = "IR_training_dump.txt"

class LabeledLineSentence(object):
    def __init__(self, filename):
        self.filename = filename
    def __iter__(self):
        for line in open(filename,"r"):
            string  = line.strip().split('\t')
            yield LabeledSentence(words=string[1].split(), tags=string[0])


#it = LabeledLineSentence(filename)

fname = 'my_model2HUGE.doc2vec'
model = Doc2Vec.load(fname)  # you can continue training with the loaded model!
cores = multiprocessing.cpu_count()


while( True):
    print("enter paper id")
    idd = input()
    #for line in open("/home/verma314/Word2Vec/IR_training_dump.txt","r"):
    d = []
    ans = model.docvecs.most_similar(positive=[idd], topn=30)
    ansx = [ i[0] for i in ans]
    print (ansx)

    for line in open ("/home/verma314/Word2Vec/IR_training_dump.txt","r"):
        if ( line.strip().split('\t')[0] in ansx ):
            print ( line )

        
