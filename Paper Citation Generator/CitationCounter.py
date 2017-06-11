f = open('PaperReferences.txt','r')
a=[]

counter = dict()

count = 0
writer = 0

for one_line in f:
    try:

        line = one_line.split('\t')[1].rstrip('\n')
        if ( line == ''):
            continue
        if line in counter:
            counter[line]+=1
        else:
            counter[line]=1

        count += 1
        if ( count == 1000000):
            print("processed 1000000 more lines")
            count = 0
        
    except:
        pass           
    
f.close()

f2 = open('CitationCountAll.txt','w')
for i in counter:
    stx = "%s\t%s\n" % (i,counter[i])
    f2.write(stx)
    if ( writer == 100000):
        print("written 100000 more lines")
        writer = 0
    writer += 1
 
f2.close()


