tup = tuple(int(i) for i in input("enter the elements: ").split())
n = int(input("enter the no to be searched: "))
if n in tup:
    print("yes")
else:
    print("no")