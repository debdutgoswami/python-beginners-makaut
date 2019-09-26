f = open('test.txt','r')
n = int(input("enter the value of n: "))
count = 0
for lines in f:
    if count>=n:
        break
    print(lines,end='')
    count = count+1