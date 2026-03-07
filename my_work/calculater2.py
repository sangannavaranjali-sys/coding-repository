#calculater number three
def add():
    return(a+b)
def subtracter():
    return(a-b)
def multiply():
    return(a*b)
def division():
    return(a/b)
def rem():
    return(a%b)
def squarea():
    return(a*a)
def squareb():
    return(b*b)
def cubea():
    return(a*a*a)
def cubeb():
    return(b*b*b)
#playground
print("---Enter the numbers to perform operations---")
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))

print("---CALCULATOR MENY---")
print("1.Sumation")
print("2.subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Reminder")
print("6.Square of first number")
print("7.Square of second number")
print("8.cube of first number")
print("9.cube of second number")

choice=int(input("Enter the number of operation from the calculator menu : "))

if choice==1:
    print("The sumation of the numbers is : ",add())
elif choice==2:
    print("The subtraction of the numbers is : ",subtracter())
elif choice==3:
    print("The Multiplication of the numbers is : ",multiply())        
elif choice==4:
    print("The Division of the numbers is : ",division())
elif choice==5:
    print("The Reminder of the numbers is : ",rem())
elif choice==6:
    print("The sqaure of the first number is : ",squarea()) 
elif choice==7:
    print("The sqaure of the second number is : ",squareb()) 
elif choice==8:
    print("The cube of the first number is : ",cubea())         
elif choice==9:
    print("The cube of the numbers is : ",cubeb())