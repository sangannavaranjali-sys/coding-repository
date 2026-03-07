def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        result=n*fact(n-1)
        return result
    
n=int(input("Enter the number to find factorial : "))
print("The factorial number: ",fact(n))    

     