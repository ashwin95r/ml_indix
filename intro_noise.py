import sys

f = open(sys.argv[1])
g = open(sys.argv[2],'w')

c=0
n=0

for line in f:
	word = line.strip().split('\t')
	if len(word) < 5:
		word.append(' ')
	if "Baby Gyms & Playmats" in word[0]:
		c += 1
		if c==5:
			c=0
			word[0] = "carriers"
	else:
		n += 1
		if n==1000:
			n=0
			word[0] = "Baby Gyms & Playmats"
	
	line1 = word[0]+'\t'+word[1]+'\t'+word[2]+'\t'+word[3]+'\t'+word[4]+'\n'
			
	g.write(line1)		
	
f.close()
g.close()	
