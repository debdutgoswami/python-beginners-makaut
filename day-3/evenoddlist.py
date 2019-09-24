l = [int(i) for i in input("enter the elements: ").split()]
even, odd = [],[]
[odd.append(i) for i in l if i%2]
[even.append(i) for i in l if not(i%2)]
print("The even list elements are",end=" ")
[print(i, end=" ") for i in even]
print("\nThe odd list elements are",end=" ")
[print(i, end=" ") for i in odd]