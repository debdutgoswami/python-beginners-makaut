f = open('test.txt','r')
freq={}
for line in f:
    for i in line.rstrip('\n').split():
        freq[i]=freq.get(i,0)+1
f.close()
[print("the frequency of {} is {}".format(i,j)) for i, j in freq.items()]