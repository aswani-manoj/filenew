string=input("enter the string:")
count=0
for i in range(len(string)):
    if(string[i]!=' '):
        count=count+1
        print("the number of characyers in the string is",count)