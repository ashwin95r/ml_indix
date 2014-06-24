import sys

f=open(sys.argv[1])
g=open(sys.argv[2],'w')
for line in f:
	w=line.strip().split('\t')
	if(w[3]!='Cell Phone'):
		g.write(line)
f.close()
g.close()
