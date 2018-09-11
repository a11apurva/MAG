import json
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re


ps = PorterStemmer()
stops = set(stopwords.words("english"))
def abstract_to_words(raw_abstract):
    abstract_text=BeautifulSoup(raw_abstract).get_text()
    letters_only= re.sub("[^a-zA-Z]"," ", abstract_text)
    words=letters_only.lower().split()
    words= [w for w in words if not w in stops]
    words = [ps.stem(w) for w in words]
    return(" ".join(words))



g=open('ID_abstracts.txt','a')
g.write("id$abstract\n")

h=open('error_log.txt','w')

a=0

for i in range(0,4):
    print("PROCESSING FILE "+str(i))
    with open('dblp-ref-'+str(i)+'.json') as f:
        for line in f:
            try:
                parsed = json.loads(line)
                #print json.dumps(parsed, indent=4, sort_keys=True)
                strx=parsed["id"]+"$"+abstract_to_words(parsed["abstract"])+"\n"
                g.write(strx)
                a+=1
            except Exception as e:
                h.write(str(e)+"\n")

print(a)

f.close()
