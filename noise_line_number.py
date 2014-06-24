f=open(sys.argv[1])
h=open(sys.argv[3])
for line1 in f:
	w=line.strip().split('\t')
	i=0
	g=open(sys.argv[2])
	for line2 in g:
		i=i+1
		x=line2.strip().split()
		if(x[0] == w[0])
			h.write(str(i)+ '\n')
	h.flush()
	
		
