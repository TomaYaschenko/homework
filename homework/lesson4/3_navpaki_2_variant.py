import sys
filename = sys.argv[0]
f = open(filename, 'r')
l=[]
for line in f:
     l.append(str(line))
     print
print(l[::-1])
f.close() 
