f = open('bulk3.txt','r')
ids=[]

for line in f:
    line=line.strip().split('\t')
    ids.append(line[0])
    print line[0]

f.close()

print ids

f = open('InformationRetrievalDatabase.txt','r')

g= open('network3.txt','w')

count=0

for line in f:
    line=line.strip().split('\t')
    if line[0] in ids:
        refs= line[8].split('|')
        print refs
        g.write(line[0])
        for r in refs:
            g.write('\t')
            g.write(r)
        g.write('\n')

f.close()
g.close()
    

