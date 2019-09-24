l = [i for i in input("enter the elements: ").split()]
if l == l[::-1]:
    print("PALLINDROME")
else:
    print("NOT PALLINDROME")