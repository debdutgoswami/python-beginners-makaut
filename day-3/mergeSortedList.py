l1 = sorted([int(i) for i in input("enter the first list: ").split()])
l2 = sorted([int(i) for i in input("enter the second list: ").split()])
l = []
i, j = 0, 0
while i!=len(l1)-1 and j!=len(l2)-1:
    if l1[i]<l2[j]:
        l.append(l1[i])
        i+=1
    elif l2[j]<l1[i]:
        l.append(l2[j])
        j+=1
    else:
        l.append(l1[i])
        l.append(l2[j])
        i+=1
        j+=1

while i!=len(l1)-1:
    l.append(l1[i])
    i+=1

while j!=len(l2)-1:
    l.append(l2[j])
    j+=1

print("the merged array is",end=" ")
[print(i,end=" ") for i in l]