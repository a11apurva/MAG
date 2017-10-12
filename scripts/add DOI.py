f=open('ComputerScienceDatabase.txt','r')

paper_id=[]

count=0
for i in f:
    paper_id.append(i.split('\t')[0])
    count+=1
    if(count==100000):
        print '1L added to dict...'
        count=0

f.close()


doi=dict()

f=open('papers.txt','r'):

count=0
for i in f:
    i=i.strip().split('\t')
    if i[0] in paper_id:
        doi[i[0]]=i[5]
    count+=1
    if (count==1000000):
        print '10L processes...'
        count=0

f.close()



paper_id=[]



f1=open('ComputerScienceDatabase.txt','r')
f2=open('ComputerScienceDatabaseNew.txt','r')

count=0
for line in f1
    try:
        if doi.has_key(line.split('\t')[0] ):
            d=doi[line.split('\t')[0]]
        else
            d=""
        LINE = line.strip() +"\t"+ str(d) +"\n"
        f2.write(LINE)
        count+=1
        if(count==100000):
            print '1L lines written...'
            count=0


f1.close()
f2.close()
        
    


        
