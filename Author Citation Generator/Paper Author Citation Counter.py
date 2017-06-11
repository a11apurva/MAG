f=open("CitationCountAll.txt",'r')

dict1=dict()
counter = 0 

for line in f:
    try:
        line=line.split('\t')
        #print(line)
        paperId= line[0].strip()
        cited= line[1].strip()
        dict1[paperId]=cited

        if (counter == 100000):
            print("1lac added to dict1")
            counter = 0
        counter += 1
    except:
        pass
    
f.close()


f=open("/home/verma314/IIT-BHU/Paper Author Affiliations New/PaperAuthorCol1and2.txt",'r')
counter = 0

f2 = open("/home/verma314/IIT-BHU/Paper Author Affiliations New/PaperAuthorCitation.txt","w")
for line in f:
    line = line.split('\t')
    paperId = line[0].strip()
    authorId = line[1].strip()

    if ( dict1.__contains__(paperId)):
        strX = paperId+"\t"+authorId +"\t"+dict1[paperId]+"\n"
        f2.write(strX)
    if ( counter == 100000):
        print("1lac written to file")
        counter = 0
    counter += 1

f.close()
f2.close()

    
    
    
