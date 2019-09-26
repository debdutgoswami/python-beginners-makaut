l = tuple(int(i) for i in input("enter the elements: ").split())
n = int(input("enter the element to be removed: "))
pos = l.index(n)
l = l[:pos]+l[pos+1:]
print("the new tuple is",l)