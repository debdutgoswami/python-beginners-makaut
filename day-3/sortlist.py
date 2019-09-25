l = [int(i) for i in input("enter the elements: ").split()]
l.sort()
print("the sorted list is",end=" ")
[print(i,end=" ") for i in l]