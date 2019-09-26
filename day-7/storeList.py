f = open('test.txt','r')
l=[]
for line in f:
    l.append(line.rstrip('\n'))
[print(i) for i in l]