import timeit
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
start_time = timeit.default_timer()
import operator

def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'
 
    if tag.startswith('V'):
        return 'v'
 
    if tag.startswith('J'):
        return 'a'
 
    if tag.startswith('R'):
        return 'r'
 
    return None
 
def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None
 
    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None
 
def sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))
 
    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
 
    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
 
    score, count = 0.0, 0
 
    # For each word in the first sentence
    for synset in synsets1:
        # Get the similarity value of the most similar word in the other sentence
        best_score = max([synset.path_similarity(ss) for ss in synsets2])
 
        # Check that the similarity could have been computed
        if best_score is not None:
            score += best_score
            count += 1
 
    # Average the values
    score /= count
    return score



def symmetric_sentence_similarity(sentence1, sentence2):
    """ compute the symmetric sentence similarity using Wordnet """
    return (sentence_similarity(sentence1, sentence2) + sentence_similarity(sentence2, sentence1)) / 2 
 






target="775DE74B	citation recommendation without author supervision	2011	0	42C7B402	19067	18	recommender system|extraction|recommender systems|bibliometrics	7EBD3AAB|80025E01|7DBE521C|7EA51AF4|7A29DBAA	6B9505B3|808AC408|58BB806E|798AF81F|78C6ED89|76EE4376|8114FC17|7B964E89|7DAACFDE|7B2F0A06|5A6E4EB3|7FB518DF|5ECF67BB|7FE46FF7|8014CEA3|7CC69AE9|70128864|5E52039A|7FF7A4F9|81149A7D|81496678|7CDA2D87|7E299985|58878126"
#target="5DB70F6F	ranking refinement via relevance feedback in geographic information retrieval	2009	0	42D7146F	19416	1	information retrieval|query expansion	7627CC45|099BF97C|2A274C10	753BD8F5|5E4350BD|7619958D|7E6B4E29|80BFFFD6|7EBE6A61|7F8AFC98|7EB42A5D|585DF669|81D39C07|80C71CFE|6F533A8F"
#target="5D1BD2CF	multi document summarization based on be vector clustering	2006	0	45B7D2EB	18870	9	cluster analysis|multi document summarization|k means clustering	8363AC79|80F6E83E|7DDE5340|81991490	0995E293|7BDBE804|80205F77|8032F97A|7F25C8E2|5D19D8E9|7E49509C|7D68490B"
#target="7FFB0C68	a personalized search engine based on web snippet hierarchical clustering	2005	07B3FFB5	43ABF249	17763	57	hierarchical clustering|information extraction|search engine|search engines	1FB3D39A|1A0E283F	0BFDC307|5C971886|79815880|58D989F4|59699732|0B579764|591C10DE|7BA595A1|749EBC54|7EAA6135|7B54C5A8|7F78C773|7DCAC7DD|815CD2AF|808285A5|79D11B64|5FADAAF9|5DEE1CA1|04F6025A|5CB2200B"
#target="7B67FDF4	fast and effective text mining using linear time document clustering	1999	0	436976F3	15540	331	document clustering|clustering|multi document summarization|linear time|text mining|text clustering|feature vector|feature extraction|feature selection	84C4A7DD|0158FA97	7ECAC6F5|6D4D5A85|770435EE|7BA595A1|8090FCC2|806E24A5|761E4F3F|77B562B0|0B642BCC|5AAF5492|771A7AA5|5F50D701|79E9DF0D"
#target="8066D29E	local approximation of pagerank and reverse pagerank	2008	0	43FD776C	19439	4	lower bound|social network|random walk|web pages|semantic relatedness	84A866B1|05F3AC18	5F4231F7|7588B2C6|7B837020|77F441E8|5AA4D7E8|5C407E31|7A60498C|7E192F20|5D7D589F|6DFA9132|7B3A99DF|7E688528|7B54C5A8|7F1B02A8|7F00CC59|7E4D921E|096BC37D|80A9A67D|79B8535A|77BAB9D3|7DA9B0EA|7E9C3DCF|06953C50|8269D01A|76DC0169|7F80C722|7A955FF9|0272BA5B|768800A9|767B12CC|7F78C773|6E851260|06B74904|0780953B|5E9C7E59|7661F3D4|7FC9957E|78628537|80F0C7E3|814C5734|5C36D00A|7C706126"
#target="77B104A6	a novel log based relevance feedback technique in content based image retrieval	2004	0	43AA5802	17891	58	image retrieval|support vector machines|support vector machine|semantic gap|query expansion	7A7F62D5|84C8AD82	7F4E6307|79091C04|7BB5DA6B|0E494B60|75FC25F4|7D395B9C|7DB8B5D7|7FD5060C|7F708127|80DC4B22|7ECDB999|5FD5AB11|8168FAFF|7D425221|7F6E0C34|7EFF4B1C|808FD230|7EE085C2|7F210653|7E41E33C|5E39F598|7A6765D4|6353F6D7|773FD79A|78739CC6|80EAF6A8|804EC349|7B15C5B1|5CFA5F85|7E1B78D9"
#target="8167F532	contextseer context search and recommendation at query time for shared consumer photos	2008	0	43AA5802	18388	34	feature selection|visual word|metadata	7D1A249B|80E29BAC|7FA0BCBC|7D65FC22|7F7A0AE7|82A726C0	813A9E0E|77CDC226|759114B4|75FC25F4|7E6A2DC9|80128855|7F9EC5B6|5B21EA31|7897203A|7C85E924|7FE9CCAF|80373DBF|6E851260|80F1DD1C|7AB1D8E1|8178F69D|04721757|7B02EF28|7E63ECD6|754821CB|79B92AE6|806C0802|7C23AF2E|7E58B497|784D18A3|7CA0C9ED|8162E4AF|76A2E7D2|7D461B67|7F1166EE|7DB2B0B4"
#target='75D657B4	keyblock an approach for content based image retrieval	2000	0	43AA5802	17829	32	document retrieval|image retrieval|image compression|indexing terms|image features|information retrieval	80DE9719|7D1F1531|7D3FE3A1|7D9FEC8C	7D806BAA|75734FC8|7CA9CE94|81409BB6|6164F0B1|7EAB3098|62DD6F0C|7E883AE5|7D1B1ED5|0ACD9EE5|0A856B03|75638525|7AD05E99|5ED40367'
#target="7CA0C9ED	semantic concept based query expansion and re ranking for multimedia retrieval	2007	0	43AA5802	17962	55	ontology|query expansion	7D397880|78253A26|7A8E35D2|76C93247|8152EBB3	759114B4|6A886314|7D79605B|7E2B7FFD|7E3B26BC|7BC64BFC|5BAB250D|8169C91E|79C449BF|7F1F69E9|7FCC121D|767E699B|60962B84|7FFAF0C8|5A5A4410|78B89835|813DC8AF|0B28E332|808CAF3E|7917CBEF|7CF5BD5B|7B02717F|7C85E924|7E6A2DC9|7EC9664C|607E8811|80921D88|75FC25F4|7F5885B1|805E8346|7B97EC8D|7DA07871|5C4883F3|5C8ECFF5"
#target="056897EE	querying the semantic web with corese search engine	2004	0	454F686A	18014	31	information retrieval|semantic web|search engine|query language	091887CA|0E2218C4|069D0945	805CC8F0|80078AB8|59F3F1B1|7AF4F62C|71EEDB59|706EF27B|01A7AFA4|05C79910|5CB2777F|803811AE|6B41879B|795735C5|754451AC|592E52AD"




target=target.strip().split('\t')
target_id=target[0]
target_title=target[1]                                                  
target_year=int(target[2])
target_ref=target[9]

ground_truth=target_ref.strip().split('|')




print 'checking...'


f=open("InformationRetrievalDatabase.txt",'r')
i=0
a=[]

count=0
counter=0

for line in f:
    title=line.split('\t')[1]
    
    id=line.split('\t')[0]

    if id==target_id:
        continue

    
    try:
        score=symmetric_sentence_similarity(target_title,title)

        line=line.strip().split('\t')

        if ( score >= 0.4 ):
            a.append([score,line])
        count+=1
        if(count==1000):
            print ("checked 1K lines..."+str(counter))
            counter+=1
            count=0
    except:
        pass


a.sort()
a.reverse()







print "TARGET : %s \n\nRecommendations:\n" % (target)

results=[]
i=0
for titles in a:
    if i==30:
        break
    i+=1
    print "%s\t%s"%(titles[1][0],titles[1][1])
    results.append(titles[1])

f.close()




print ("\n\nenter comma  separated paperIds for papers you find relavant")
papers = input().strip().split(',')
papers = [ i.strip() for i in papers ]

referencePapers = []



selected_papers=[]
selected_authors=[]

for i in results:
    if ( i[0] in papers):
        if ( i[-1] != 'NA'):
            referencePapers.extend(i[-1].split("|"))
        selected_papers.append([i[0], i[1], i[2], i[6], i[8], i[7],i[3],i[4]])     
	auth= i[8].split('|')    	
	selected_authors.extend(auth)




for i in selected_authors:
	print i


self_cited_papers_id=[]

print '\n\nlooking for self-cited papers...\n'

for line in open('PaperAuthor.txt','r'):
    line=line.strip().split('\t')
    if line[1] in selected_authors:
        self_cited_papers_id.append(line[0])


f=open('same.txt','w')
self_cited_papers=[]
print '\n\nfetching paper name...\n'
for line in open("InformationRetrievalDatabase.txt",'r'):
    line=line.strip().split('\t')
    if(line[0] in self_cited_papers_id):
        print line[1]
        self_cited_papers.append([line[0],line[1]])



print '\n\nchecking...\n'

i=0
a=[]

count=0
counter=0

for papers in self_cited_papers:
    try:
        score=symmetric_sentence_similarity(target_title,papers[0])
        if ( score >= 0.5 ):
            a.append([score,papers[0],papers[1]])
        count+=1
        if(count==10):
            print ("checked 10 lines..."+str(counter))
            counter+=1
            count=0
    except:
        pass


a.sort()
a.reverse()



print "\n\nTARGET : %s \n\nRecommendations:\n" % (target)

results=[]
i=0

for titles in a:
    if i==10:
        break
    i+=1
    print "%s"%(titles[2])

f.close()
