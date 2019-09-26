f = open('test.txt','r')
count = 0
for line in f:
    count+=1
print("the number of lines are",count)