import json

g=open('ID_abstracts.txt','a')

a=0

for i in range(0,4):
    print "PROCESSING FILE "+str(i)
    with open('dblp-ref-'+str(i)+'.json') as f:
        for line in f:
            try:
                parsed = json.loads(line)
                #print json.dumps(parsed, indent=4, sort_keys=True)
                strx=parsed["id"]+"\t"+parsed["abstract"]+"\n"
                g.write(strx)
                a+=1
            except Exception as e:
                pass

print a
f.close()
