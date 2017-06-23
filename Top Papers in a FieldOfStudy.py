f=open('CSE_fields_names.txt','r')




fields=dict()
for line in f:
    line=line.strip().split('\t')
    fields[line[1]]=line[0]

f.close()
    
    
fos= raw_input('Enter two comma seperated FOS: ')
fos=[i.strip() for i in fos.split(',')]
n=len(fos)


target=[]

for i in fos:
    target.append(fields[i])


print target


print 'finding paper ids...'

papers=[]

for i in range(n):
    temp=[]
    f=open('paper_field_relation_CSE.txt','r')
    for line in f:
        line=line.strip().split('\t')
        if line[1] == target[i]:
            temp.append(line[0])
    papers.append(temp)
    f.close()



selected= set(papers[0]) & set(papers[1])

##f=open('selected.txt','w')
##
##for i in selected:
##    f.write(i)
##    f.write('\n')
##
##f.close()
    
print 'finding papers...'

f=open('InformationRetrievalDatabase.txt','r')


papers=[]

for line in f:
    line=line.split('\t')
    if line[0] in selected:
        papers.append(line)

f.close()


papers.sort(key = lambda row: int(row[6]), reverse=True)

i=0
for line in papers:
    print '%s\t%s' % (line[1],line[6])
    i+=1
    if i==10:
        break










