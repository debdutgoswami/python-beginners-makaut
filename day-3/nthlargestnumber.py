l = [int(i) for i in input("enter the elements: ").split()]
l.sort(reverse=True)
n = int(input("enter the value of n: "))
print("the {}-th largest element is {}".format(n,l[n-1]))