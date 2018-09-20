import gensim
import os
import collections
import smart_open
import random
import pandas as pd
import time
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

df = pd.read_csv('ID_abstract.txt', delimiter="$" , header=0)

print("BP1")

df['abstract'].replace('', pd.np.nan, inplace=True)

print("BP2")

df.dropna(subset=['abstract'], inplace=True)

print("BP3")

print(df.head())
print(df["id"][0])
    
#g=open("doc2vec-error.txt","w")
    
train_corpus=[]
for index, row in df.iterrows():
    #print(row["bugId"],row["logs"])
    #g.write(row["id"]+"\t"+row["abstract"]+"\n")
    train_corpus.append(gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(row['abstract']), [index]))
    
print(train_corpus[0])

df2 = pd.read_csv('ID_abstracts_3_test.txt', delimiter="$" , header=0)
df2['abstract'].replace('', pd.np.nan, inplace=True)
df2.dropna(subset=['abstract'], inplace=True)
df2.head()


test_corpus=[]
for index, row in df2.iterrows():
    print(row["id"],row["abstract"])
    test_corpus.append(gensim.utils.simple_preprocess(row['abstract']))
    
print(len(test_corpus))

model = gensim.models.doc2vec.Doc2Vec(dm=0, size=100, min_count=5, window=10, iter=200, workers=14)
model.build_vocab(train_corpus)
model.train(train_corpus, total_examples=model.corpus_count, epochs=model.iter)
model.save_word2vec_format('doc_tensor-TP-1-Pilot.w2v', doctag_vec=True, word_vec=False)

print(df.shape[0])
print(df.shape[1])
print(model.docvecs.count)


for doc_id in range(len(test_corpus)):
    inferred_vector = model.infer_vector(test_corpus[doc_id])
    sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
    #print(sims)
    #sim_id=
    print("\n")
    print(df2["id"][doc_id])
    print(df["id"][[sims][0][0][0]]+"\t"+df["id"][[sims][0][0][1]])
    print(df["id"][[sims][0][1][0]]+"\t"+df["id"][[sims][0][1][1]])
    print(df["id"][[sims][0][2][0]]+"\t"+df["id"][[sims][0][2][1]])
    
        






