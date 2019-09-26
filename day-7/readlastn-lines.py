f = open('test.txt','r')
n=int(input("enter the value of n: "))
l=[]
for line in f:
    l.append(line.rstrip('\n'))
[print(i) for i in l[len(l)-n:]]