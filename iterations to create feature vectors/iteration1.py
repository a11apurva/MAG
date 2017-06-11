f1 = open("extracted_papers.txt","r")

f2 = open("iterations1.txt","w")

counter = 0


for line in f1:
    line = line.strip().split('\t')
    if ( line[8] == ''):
        line[8] = '0'
    if ( line[9] == ''):
        line[9] = '0'
        
    writeLine = line[0]+"\t"+line[2]+"\t"+line[3]+"\t"+line[8]+"\t"+line[9]+"\t"+line[10]+"\n"
    f2.write(writeLine)

    if ( counter == 100000):
        print("1 lac lines written")
        counter = 0

    counter += 1

f1.close()
f2.close()
