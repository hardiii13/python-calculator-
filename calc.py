def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("Enter your option")
print("Addition\n")
print("Subtraction\n")
print("multiplication\n")
print("Division\n")
while True:
    choice=input("Enter your choice 1/2/3/4")
    if choice in('1','2','3','4'):
        num1=float(input("Enter the first number"))
        num2=float(input("Enter the second number"))
        if choice==1:
            print(num1, "+",num2,"=",add(num1,num2))
        elif choice==2:
            print(num1,"-",num2,"=",sub(num1,num2))
        elif choice==3:
            print(num1,"*",num2,"=",mul(num1,num2))
        elif choice==4:
            print(num1,"/",num2,"=",div(num1,num2))
    else:
        print("Entered number is incorrect")
