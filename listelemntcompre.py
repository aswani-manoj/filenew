list1=[12,4,6]
list2=[4,6,9,7,1]
l1=len(list1)
l2=len(list2)
sum1=0
sum2=0
for i in list1:
    for j in list2:
        if i==j:
            print(j,"occur in both")