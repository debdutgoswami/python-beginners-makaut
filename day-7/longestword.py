f = open('test.txt','r')
length, word=None, None
for line in f:
    l = line.rstrip('\n').split()
    for j in l:
        if length==None or len(j)>length:
            length = len(j)
            word = j
f.close()
print("the longest word is",word)