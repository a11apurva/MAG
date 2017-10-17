import operator

f=open('ComputerScienceDatabase.txt','r')

results=[]

target=raw_input('Enter querry: ')



print "\n\nRecommendations:\n"

for i in f:
    line=i.split('\t')
    if ((target in line[1])): #or  ('scientific paper' in line)): # or ('citation analysis' in line) or ('bibliometrics' in line)):
        #print i.split('\t')[1]
        print '%s\t%s' % (line[0],line[1])
        results.append(i)
f.close()






print "\n\n"


print ("enter comma  separated paperIds for papers you find relavant")
papers = input().strip().split(',')
papers = [ i.strip() for i in papers ]

referencePapers = []


for i in results:
    if ( i[0] in papers):
        if ( i[-1] != 'NA'):
            referencePapers.extend(i[-1].split("|"))
    
    
print 'Checking...'

f = open("ComputerScienceDatabase.txt","r")
count=0
count2=0
anubhavKiList = []
vermaKiList = []


for line in f:
    line=line.strip().split('\t')
    if ( line[0] in referencePapers):
        anubhavKiList.append([line[0], line[1], line[2], line[6], line[8], line[7]])

    for p in papers:
        if p in line[-1].strip().split('|'):
            vermaKiList.append([line[0], line[1], line[2], line[6], line[8], line[7]])

    count+=1
    if count==1000000 :
        print "10L lines Checked : %s" % (count2)
        count2+=1
        count=0

f.close()

commonList=[]
commonList.extend(anubhavKiList)
commonList.extend(vermaKiList)
commonList=dict((x[0], x) for x in commonList).values()


'''PRINT REFERENCED PAPAERS'''

print "\n\nReferences:\n"
for papers in anubhavKiList:
    print "%s:\t%s" % (papers[0],papers[1])

'''PRINT CITED PAPAERS'''
print "\n\nCited:\n"
for papers in vermaKiList:
    print "%s:\t%s" % (papers[0],papers[1])



'''PRINT RECENT PAPAERS'''

commonList.sort(key = lambda row: int(row[2]))
commonList.reverse()
i=0
print "\n\nTop 10 Recent Papers:\n"
for papers in commonList:
    print "%s:\t%s" % (papers[2],papers[1])
    i+=1
    if i==10:
        break;
                               

'''PRINT MOST POPULAR PAPAERS'''

commonList.sort(key = lambda row: int(row[3]))
commonList.reverse()
i=0

print "\n\nTop 10 Popular Papers:\n"                              

for papers in commonList:
    print "%s:\t%s" % (papers[3],papers[1])
    
    i+=1
    if i==10:
        break;


'''COUNT COMMON AUTHORS AND KEYWORDS'''

authors=dict()
keywords=dict()
for papers in commonList:
    for auth in papers[4].strip().split('|'):
        if authors.has_key(auth):
            authors[auth]+=1
        else:
            authors[auth]=1

    for keys in papers[5].strip().split('|'):
        if keywords.has_key(keys):
            keywords[keys]+=1
        else:
            keywords[keys]=1
 


'''TOP SIMILAR PAPERS'''

print "\n\nTop 10 Similar Papers:\n"                              


for i in commonList::
    line=i.split('\t')
    if ((target in line[1])): #or  ('scientific paper' in line)): # or ('citation analysis' in line) or ('bibliometrics' in line)):
        #print i.split('\t')[1]
        print '%s\t%s' % (line[0],line[1])







'''TOP AUTHORS'''

sorted_authors = sorted(authors.items(), key=operator.itemgetter(1), reverse=True)

print '\n\nTop Authors:'
i=0
for auth in sorted_authors:
    print auth
    i+=1
    if i==10:
        break


'''TOP KEYWORDS'''

sorted_keywords = sorted(keywords.items(), key=operator.itemgetter(1), reverse=True)

print '\n\nTop Keywords:'
i=0
for keys in sorted_keywords:
    print keys
    i+=1
    if i==10:
        break


print '\ndone'

