with open('test.txt','r') as inline, open('testoutput.txt','w') as outline:
    data = inline.read()
    data = data.replace('\n','. ')
    outline.write(data)
