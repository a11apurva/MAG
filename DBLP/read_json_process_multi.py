import json
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import sys
from multiprocessing import Process, Queue


ps = PorterStemmer()
stops = set(stopwords.words("english"))

def abstract_to_words(raw_abstract):
    abstract_text=BeautifulSoup(raw_abstract).get_text()
    letters_only= re.sub("[^a-zA-Z]"," ", abstract_text)
    words=letters_only.lower().split()
    words= [w for w in words if not w in stops]
    words = [ps.stem(w) for w in words]
    return(" ".join(words))


def clean(i):
  a=1
  print("THREAD "+str(i)+" spawned")
  g=open("ID_abstracts_"+str(i)+".txt","w")
  h=open("errors_"+str(i)+".txt","w")
  with open('dblp-ref-'+str(i)+'.json') as f:
    for line in f:
      try:
        parsed = json.loads(line)
        #print json.dumps(parsed, indent=4, sort_keys=True)
        strx=parsed["id"]+"$"+abstract_to_words(parsed["abstract"])+"\n"
        g.write(strx)
        a+=1
        if a==10000:
          print("10K processed by thread "+str(i))
          a=0
      except Exception as e:
        h.write(str(e)+"\n")
  g.close()
  h.close()
  print("THREAD "+str(i)+" finished")


if __name__ == '__main__':

  print("\n***TASK STARTED***\n")
  
  q = Queue()
  p1 = Process(target=clean, args=(0,))
  p1.start()
  p2 = Process(target=clean, args=(1,))
  p2.start()
  p3 = Process(target=clean, args=(2,))
  p3.start()
  p4 = Process(target=clean, args=(3,))
  p4.start()
  
  p1.join()
  p2.join()
  p3.join()
  p4.join()
  
  print("\n***TASK COMPLETED***\n")
