f = open('test.txt','a')
f.write("This line is appended")
f.close()
f = open('test.txt','r')
for line in f:
    print(line,end='')