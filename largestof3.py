num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
num3=int(input("enter the number:"))
if num1>num2 and num1>num3:
    big=num1
elif num2>num1 and num2>num3:
    big=num2
else:
    big=num3
    print("biggest number is",big)