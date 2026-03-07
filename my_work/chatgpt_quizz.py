'''question 1
movie=[]
mov1=input("Enter your first fev movie:")
mov2=input("Enter your second fev movie:")
mov3=input("Enter your third fev movie:")
movie.append(mov1)
movie.append(mov2)
movie.append(mov3)
print(movie)'''

'''question 2
item=[]
item1=input("Enter your first grocery Item:")
item2=input("Enter your second grocery Item:")
item3=input("Enter your third grocery Item:")
item4=input("Enter your forth grocery Item:")
item5=input("Enter your fifth grocery Item:")

item.append(item1)
item.append(item2)
item.append(item3)
item.append(item4)
item.append(item5)
print(item1)
print(item2)
print(item3)
print(item4)
print(item5)'''

'''question 3
names=[]
n=int(input("Enter the limit to the number of names:"))
for i in range (0,n):
    x=input("Enter the names:")
    names.insert(i,x)
print("The given list:",names) 
s_name=input("Enter a name to search:")
if s_name in names:
    print("The name is found")
else:
    print("The name is not found")'''

'''question 4
num=[]
n=int(input("Enter the limit to the numbers:"))
for i in range(0,n):
    x=int(input("Enter the numbers:"))
    num.insert(i,x)
total=sum(num)    
print("The sum of number is=",total)'''

'''question 5
student ={
    "name" : "Anjali",
    "age" : 18,
    "city" : "Hubli",
    "marks" : {
        "SQL" : 98,
        "PYTHON" :99,
        "FOC" : 97
    }
}
print(student["PYTHON"])'''
             
'''#question 6
n=int(input("Enter the number : "))
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i+=1'''

'''#question 7
print()
print()
print("---THE SIGN IN PAGE---")
print()
u_name=input("Enter your user name : ")
print()
print("Your password should contain 8 letters")  
print()
y_p=input("Enter your password : ")
lenght=len(y_p)
if (lenght==8):
    print("The password is correct")
else:
    print("The password should be contain 8 letters")    
r_p=input("Enter your password to confirm again")
if (y_p == r_p):
    print("Your password is correct")
else:
    print("Your password is wrong") '''


''' question 8
N=int(input("Enter any number"))
if (N%5==0):
        print("The number is devisible by 5 ")
else:
    print("This number is not devisible by 5 ")        
if(N%11==0):
        print("The number is devisible by  11")
else:
    print("This number is not devisible by 11")'''

''' question 9
N=int(input("Enter any number : "))
rem=N%3
if (rem==0):
    print("The number is devisible by 3")    
else:     
     print("The number is not devisible by 3")'''

'''#question 10
i=1
while i<=10:
    print(i)
    i=i+1'''

'''question 11
for i in range(2,51,2):
    print(i)'''

''' question 12
N=int(input("Enter any number : "))
sum=0
for i in range(1,N+1):
    sum=sum+i
print(sum)'''

'''question 13
N=int(input("Enter any number : "))
sum=0
rem=0
while (N>0):
    rem=N%10
    N=int(N/10)
    sum=sum+rem
print(sum)'''

''' question 14
N=int(input("Enter any number : "))
sum=0
rem=0
while (N>0):
    rem=N%10
    N=int(N/10)
    sum=sum+1
print(sum) '''

'''question 15
N=input("Enter a word : ")
print(len(N))'''

'''question 16
N=input("Enter any word : ")
if N(::-1):
    print(N)'''

'''question 17
N=int(input("Enter any number to find Factorial : "))
i=1
fact=1
while i<=N:
    fact=fact*i
    i+=1
print("The Factorial = ",fact)'''    
 
''' question 18
N=int(input("Enter any number : "))
i=1
for i in range(i,11):
    print(N,"X",i,"=",N*i)'''

'''question 19
N=int(input("Enter any number : "))
reverse=0
rem=0
while N>0 :
    rem=N%10
    N=int(N/10)
    reverse=reverse*10+rem
print(reverse)    '''

''' question 20
list=[1,2,3]
print("The list : ",list)
n=len(list)
sum=0

for i in range(0,n):
    sum=sum+list[i]
print("The sum is : ",sum)    '''

# question 21
list=[1,2,3,96,5,801]
n=len(list)
large=0
for i in range(0,n):
    if(list[i]>large):
        large=list[i]
print(large)        





    

