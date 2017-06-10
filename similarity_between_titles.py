import timeit
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
start_time = timeit.default_timer()

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
 
sentences = [
    "Dogs are awesome.",
    "Some gorgeous creatures are felines.",
    "Dolphins are swimming mammals.",
    "Cats are beautiful animals.",
]
 
focus_sentence = "Cats are beautiful animals."


def symmetric_sentence_similarity(sentence1, sentence2):
    """ compute the symmetric sentence similarity using Wordnet """
    return (sentence_similarity(sentence1, sentence2) + sentence_similarity(sentence2, sentence1)) / 2 
 

f = open('ict_papers','r')


target="A Recommendation System Based on Hierarchical Clustering of an Article-Level Citation Network"


i=0
a=[]

for line in f:
    title=line.split('\t')[1]
    id=line.split('\t')[0]
    try:
        score=symmetric_sentence_similarity(target,title)
    ##    print '%s\t%s\t%s' % (id, score,title)    
        a.append([score,id,title.rstrip('\n')])        
    except:
        pass


a.sort()
a.reverse()

print "TARGET : %s \n\nRecommendations:\n" % (target)

for titles in a:
    if i==15:
        break
    i+=1
    print "%s\t%s"%(i,titles[2])

f.close()
elapsed = timeit.default_timer() - start_time
print '\ndone'
print elapsed
