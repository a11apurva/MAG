f1 = open("/home/verma314/IIT-BHU/Paper Keywords/PaperKeywords.txt","r")

dict1 = dict()

count = 0

for line in f1:
    line = line.split('\t')
    if ( dict1.__contains__(line[0])):
        dict1[line[0]] = dict1[line[0]]+str("|")+str(line[1])
    else:
        dict1[line[0]] = line[1]

    if ( count == 1000000):
        count = 0
        print("10 lac added to dict")

    count += 1

print("added to dictionary")
    
f1.close()

f2 = open("iterations2.txt", "r")
f3 = open("iterations3.txt","r")

count = 0

for line in f2:
    paperId = line.split('\t')[0]

    if ( dict1.__contains__(paperId)):
        keyword = dict1[paperId]
    else:
        keyword = 'NA'

    writeLine = line.strip()+"\t"+keyword+"\n"
    f3.write(writeLine)

    if (count == 1000000):
        count = 0
        print("10 lac written to file")

    count += 1

f2.close()
f3.close()

print("dome")
