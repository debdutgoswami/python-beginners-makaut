dictionary = {"Name": "Debdut","Roll": "114", "Dept.": "CSE"}
ascending = dict(sorted(dictionary.items(), key=lambda x: x[1]))
descending = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
print("the dictionary in ascending order of values is",ascending)
print("the dictionary in descending order of values is",descending)