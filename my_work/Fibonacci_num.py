def fib(n):
    if (n==0):
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        return fib(n-1)+fib(n-2)

n=int(input("Enter the element to find the fibonacci series : "))
for i in range(n):
    print("The result : ",fib(i))

    
    