from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string

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
 




doc1="Automatic recommendation of citations for a manuscript ishighly valuable for scholarly activities since it can substan-tially improve the eﬃciency and quality of literature search.The prior techniques placed a considerable burden on users,who were required to provide a representative bibliographyor to mark passages where citations are needed.In thispaper we present a system that considerably reduces thisburden: a user simply inputs a query manuscript (without abibliography) and our system automatically ﬁnds locationswhere citations are needed. We show that na¨ıve approachesdo not work well due to massive noise in the document cor-pus. We produce a successful approach by carefully exam-ining the relevance between segments in a query manuscriptand the representative segments extracted from a documentcorpus. An extensive empirical evaluation using the Cite-SeerX data set shows that our approach is eﬀective.Categories and Subject DescriptorsH.3.3 [Information Storage and Retrieval]: InformationSearch and RetrievalGeneral TermsAlgorithms, Design, ExperimentationKeywordsBibliometrics, Context, Extraction, Recommender Systems1."
doc2="Citation recommendation is an interesting and signiﬁcant research area as it solves theinformation overload in academia by automatically suggesting relevant references for a research paper.Recently, with the rapid proliferation of information technology, research papers are rapidly published invarious conferences and journals. This makes citation recommendation a highly important and challengingdiscipline. In this paper, we propose a novel citation recommendation method that uses only easily obtainedcitation relations as source data. The rationale underlying this method is that, if two citing papers aresigniﬁcantly co-occurring with the same citing paper(s), they should be similar to some extent. Based onthe above rationale, an association mining technique is employed to obtain the paper representation ofeach citing paper from the citation context. Then, these paper representations are pairwise compared tocompute similarities between the citing papers for collaborative ﬁltering. We evaluate our proposed methodthrough two relevant real-world data sets. Our experimental results demonstrate that the proposed methodsigniﬁcantly outperforms the baseline method in terms of precision, recall, and F1, as well as mean averageprecision and mean reciprocal rank, which are metrics related to the rank information in the recommendationlist.INDEX TERMS Citation recommendation, collaborative ﬁltering, citation context, citation relation matrix,association mining.I. "
doc3="Citations are important in academic dissemination. To helpresearchers check the completeness of citations while author-ing a paper, we introduce a citation recommendation systemcalled RefSeer. Researchers can use it to ﬁnd related works tocited while authoring papers. It can also be used by review-ers to check the completeness of a paper’s references. RefSeerpresents both topic based global recommendation and alsocitation-context based local recommendation. By evaluatingthe quality of recommendation, we show that such recom-mendation system can recommend citations with good pre-cision and recall. We also show that our recommendationsystem is very eﬃcient and scalable.Categories and Subject DescriptorsH.3.3 [Information Storage and Retrieval]: InformationSearch and RetrievalKeywordsCitation recommendation, RefSeer1."
doc4="Although Recommender Systems have been comprehensivelyanalyzed in the past decade, the study of social-based rec-ommender systems just started.In this paper, aiming atproviding a general method for improving recommender sys-tems by incorporating social network information, we pro-pose a matrix factorization framework with social regulariza-tion. The contributions of this paper are four-fold: (1) Weelaborate how social network information can beneﬁt recom-mender systems; (2) We interpret the diﬀerences betweensocial-based recommender systems and trust-aware recom-mender systems; (3) We coin the term Social Regularizationto represent the social constraints on recommender systems,and we systematically illustrate how to design a matrix fac-torization objective function with social regularization; and(4) The proposed method is quite general, which can be eas-ily extended to incorporate other contextual information,like social tags, etc. The empirical analysis on two largedatasets demonstrates that our approaches outperform otherstate-of-the-art methods.Categories and Subject Descriptors: H.3.3 [Informa-tion Search and Retrieval]: Information Filtering; J.4 [Com-puter Applications]: Social and Behavioral SciencesGeneral Terms: Algorithm, ExperimentationKeywords: Recommender Systems, Collaborative Filter-ing, Social Network, Matrix Factorization, Social Regular-ization∗Irwin King is currently on leave from the Chinese Univer-sity of Hong Kong, where the major part of this researchwas performed.Permission to make digital or hard copies of all or part of this work forpersonal or classroom use is granted without fee provided that copies arenot made or distributed for proﬁt or commercial advantage and that copiesbear this notice and the full citation on the ﬁrst page. To copy otherwise, torepublish, to post on servers or to redistribute to lists, requires prior speciﬁcpermission and/or a fee.WSDM’11, February 9–12, 2011, Hong Kong, China.Copyright 2011 ACM 978-1-4503-0493-1/11/02 ...$10.00.1."
doc5="With  the  growth  of  the  World  Wide  Web,  a  large  amount  of  musicdata  is  available  on  the  Internet.  In  addition  to  searching  expectedmusic  objects  for  users,  it  becomes  necessary  to  develop  arecommendation  service.  In  this  paper,  we  design  the  MusicRecommendation  System serviceof  music  recommendation.  The  music  objects  of  MIDI  format  arefirst  analyzed.  For  each  polyphonic  music  object, therepresentative track is first determined, and then six features areextracted from this track. According to the features, the musicobjects are properly grouped. For users, the access histories areto  provide  a  personalized (MRS) and  statistics-based  recommendation  methods  are  proposed,which are based on the favorite degrees of the users to the musicgroups. A series of experiments are carried out to show that ourapproach feasible.is Keywordsmusic recommendation, perceptual properties, access histories,recommendation  methods, profilesuser 1.  "
doc6="this paper we want to analyse fuzzy weather forecasts, which are computed in our systemand used to forecast pollution concentrations. The system works on real data: weather forecasts,meteorological situations and pollution concentrations. We compare defuzzification of the fuzzyweather forecast with weather forecast from Institute of Meteorology and Water Management.This comprehensive analysis allows us to investigate the effectiveness of forecasting pollutionconcentrations, putting the dependence between particular attributes describing the weatherforecast in order and proving the legitimacy of the applicable fuzzy numbers in air pollutionforecasting.Model is created for data, which is measured and forecast in Poland. By reason of this data ourmodel is tested in real sets of data and effects are received in active system."
doc7="We describe latent Dirichlet allocation (LDA), a generative probabilistic model for collections of discrete data such as text corpora. LDA is a three-level hierarchical Bayesian model, in which each item of a collection is modeled as a finite mixture over an underlying set of topics. Each topic is, in turn, modeled as an infinite mixture over an underlying set of topic probabilities. In the context of text modeling, the topic probabilities provide an explicit representation of a document. We present efficient approximate inference techniques based on variational methods and an EM algorithm for empirical Bayes parameter estimation. We report results in document modeling, text classification, and collaborative filtering, comparing to a mixture of unigrams model and the probabilistic LSI model."
doc8="Data mining has been used intensively and extensively by many organizations. Inhealthcare, data mining is becoming increasingly popular, if not increasingly essential.Data mining applications can greatly benefit all parties involved in the healthcareindustry. For example, data mining can help healthcare insurers detect fraud and abuse,healthcare organizations make customer relationship management decisions,physicians identify effective treatments and best practices, and patients receivebetter and more affordable healthcare services.The huge amounts of data generated by healthcare transactions are too complex andvoluminous to be processed and analyzed by traditional methods. Data miningprovides the methodology and technology to transform these mounds of datainto useful information for decision making."


doc1=doc1.decode('unicode_escape').encode('ascii','ignore')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
doc2=doc2.decode('unicode_escape').encode('ascii','ignore')   
doc3=doc3.decode('unicode_escape').encode('ascii','ignore')   
doc4=doc4.decode('unicode_escape').encode('ascii','ignore')   
doc5=doc5.decode('unicode_escape').encode('ascii','ignore')
doc6=doc6.decode('unicode_escape').encode('ascii','ignore')
doc7=doc7.decode('unicode_escape').encode('ascii','ignore')
doc8=doc8.decode('unicode_escape').encode('ascii','ignore')


#import re
#text = re.sub('\n', '', a)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
doc = [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8]

for i in doc:
    print symmetric_sentence_similarity(doc1,i)    










