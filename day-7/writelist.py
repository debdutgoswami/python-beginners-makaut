l = ["Hi","welcome to Debdut Goswami's GitHub repository","Don't forget to star the repo","Thank you"]
f = open('new.txt','w')
for i in l:
    f.writelines(i)
    f.write('\n')
f.close()