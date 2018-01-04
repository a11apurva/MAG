f = open('paper3_after_avrage_pruning.txt','r')


ids=set()

for line in f:
    line=line.strip()
    ids.add(line)

f.close()

f = open('network3.txt','r')
g = open('network3_after_average_pruning.txt','w')

for line in f:
    line=line.strip().split('\t')
    if line[0] in ids or line[1] in ids:
        continue
    else:
        g.write(line[0]+"\t"+line[1]+"\n")

f.close()
g.close()
        


