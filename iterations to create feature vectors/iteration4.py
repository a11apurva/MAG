f1 = open("iterations3.txt","r")

f2 = open("/home/cse/phd/16071505/MAGNEW/PaperAuthorAffiliations.txt","r")


print("creating set from iterations3 ..")

paperIds = set()
count = 0
flag = 0
for line in f1:
    paperId = line.split('\t')[0]
    paperIds.add(paperId)
    count += 1
    if ( count == 1000000):
        print("10 lac added to set "+ str(flag) )
        count = 0
        flag += 1

f1.close()
print("creating dictionary with paperId and authorId")

dict1 = dict()
count = 0
flag=0
for line in f2:
    line = line.strip().split('\t')
    if ( line[0] in paperIds):
        if ( dict1.__contains__(line[0])):
            dict1[line[0]] = dict1[line[0]]+"|"+line[1]
        else:
            dict1[line[0]] = line[1]

    count += 1
    if ( count == 1000000):
        print("10 lac added to dict "+ str(flag))
        count = 0
        flag += 1

f2.close()
print("just there, hold on...")

count = 0
flag=0
f1 = open("iterations3.txt","r")
f3 = open("iterations4.txt","w")
for lineOri in f1:
    line = lineOri.strip().split('\t')
    paperId = line[0]
    if ( dict1.__contains__(paperId)):
        authorId = dict1[paperId]
    else:
        authorId = 'NA'
    writeLine = lineOri.strip()+"\t"+authorId+"\n"
    f3.write(writeLine)
    
    count += 1
    if ( count == 1000000):
        print("10 lac added to dict "+ str(flag))
        count = 0
        flag += 1

f1.close()
f3.close()
print("and there you go!")
    







    
