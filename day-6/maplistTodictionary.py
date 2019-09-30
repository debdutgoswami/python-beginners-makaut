key = [1, 2, 3, 4]
value = [1, 4, 9, 16]
dictionary = dict()
[dictionary.update({k: v}) for k, v in zip(key, value)]
print(dictionary)