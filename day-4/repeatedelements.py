l = tuple(int(i) for i in input("enter the elements: ").split())
n = []
[n.append(i) for i in set(l) if l.count(i) > 1]
print("the repeated elements are:",end=" ")
[print(i,end=" ") for i in n]