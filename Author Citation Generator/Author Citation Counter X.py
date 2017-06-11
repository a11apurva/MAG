f = open("PaperAuthorCitation.txt","r")


dict1 = dict()

count = 0

for line in f:
    line = line.split("\t")
    authorId = line[1].strip()
    cc = line[2].strip()
    if ( dict1.__contains__(authorId)):
        dict1[authorId] += int(cc)
    else:
        dict1[authorId] = int(cc)

    if ( count == 1000000):
        print("written 10 lac more to dictionary...")
        count = 0
        
    count += 1


f.close()

f = open("FinallyAuthorCitation.txt","w")

count = 0

for i in dict1:
    line = str(i)+"\t"+str(dict1[i])+"\n"
    f.write(line)
    
    if ( count == 100000):
        print("wriiten 1 lac more files to file...")
        count = 0

    count += 1
