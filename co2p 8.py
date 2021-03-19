n=int(input("enter the no.of string:"))
list=[]
for i in range(n):
    x=(input("enter the string:"))
    list.append(x)
print(list)
max=len(list[0])
temp=list[0]
for i in list:
    if(len(i)>max):
        max=len(i)
        temp=i
        print("the longest word:",temp)
        print("the length of word",max)