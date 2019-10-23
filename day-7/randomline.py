import random
f = open('test.txt','r')
length = f.read().count('\n')+1
f.seek(0,0)
n = random.randint(1,length)
c = 1
for line in f:
    if c==n:
        print(line,end='')
        break
    c+=1