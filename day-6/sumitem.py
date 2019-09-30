dictionary = {2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
s = 0
l = [sum(tup) for tup in dictionary.items()]
print("the sum of the dictionary is",sum(l))