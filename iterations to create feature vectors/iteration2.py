f1 = open("iterations1.txt","r")
f2 = open("/home/verma314/IIT-BHU/Paper Author Affiliations New/PaperCitationCountAll.txt","r")

f3 = open("iterations2.txt","w")

dic1 = dict()
count = 0
for line in f2:
    line = line.strip().split('\t')
    dic1[line[0]] = line[1]
    if ( count == 100000):
        print("1 lac files added")
        count = 0
    count += 1
    
f2.close()

print("added to dictionary")

count = 0
for line in f1:
    paperId = line.split('\t')[0].strip()

    if dic1.__contains__(paperId):
        citations=dic1[paperId]
    else:
        citations='0'
    
    writeLine = line.strip()+"\t"+citations+"\n"
    f3.write(writeLine)
    if ( count == 100000):
        print("1 lac citation values added...")
        count = 0
    count += 1


print ("done scenes mofo!")

f1.close()
f3.close()
