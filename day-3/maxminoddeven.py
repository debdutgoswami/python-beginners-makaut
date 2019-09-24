l = [int(i) for i in input("enter the elements: ").split()]
even, odd = [],[]
[odd.append(i) for i in l if i%2]
[even.append(i) for i in l if not(i%2)]
print("The maximum odd number is",max(odd))
print("The minimum even number is",min(even))