f = open('global-key-route(1-30).txt','r')
ids=[]

for line in f:
    line=line.strip()
    print line[-8:]
    ids.append(line[-8:])
    
f.close()

ids.reverse()
ids.pop()
ids.pop()
ids.pop()
ids.pop()
print ids


f=open("E:\MAG\FOS\ComputerScienceDatabase.txt",'r')
g=open("results-global-keyroute.txt","w")

for line in f:
    line=line.strip().split("\t")
    if line[0] in ids:
        strx=line[0]+"\t"+line[1]+"\n"
        print strx
        g.write(strx)


f.close()
g.close()
        


