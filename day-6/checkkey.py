dictionary = {"Name": "Debdut","Roll": "114", "Dept.": "CSE"}
key = input('enter the key: ')
check = dictionary.get(key,'-1')
if check=='-1':
    print("not present")
else:
    print("present")