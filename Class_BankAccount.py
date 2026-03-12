class Bank:
    def __init__(self,name,acc_num):
        self.name=name
        self.acc_num=acc_num
        self.balance=0
    
    def deposit(self,amount):
        if (amount>0):
            self.balance+=amount
            print("Deposit successfully")
        else:
            print("Enter a valid amount")

    def withdraw(self,amount):
        if(amount>0) and (amount<=self.balance):
            print("Amount withdraw successfully!!!")
        elif(amount>self.balance):
            print("Insufficient fund")
        else:
            print("Enter a valid amount")

    def Showdetails(self):
        print("Account name : ",self.name)
        print("Account number : ",self.acc_num)
        print("Balance amount : ",self.balance)


name=input("Enter your name : ")
acc_num=input("Enter your acount number : ")
lenght=len(acc_num)
if (lenght==5):
    print()
else:
    print("Please Enter a password with 5 letter")    
    exit()

account=Bank(name,acc_num,)

while True: 
    print("============Choose a option from the menu============")
    print("1.Show details")
    print("2.Amount deposit")
    print("3.Amount withdraw")
    print("4.Exit")

    Choice=int(input("Eneter a choice number : "))


    if Choice==1:
        account.Showdetails()
    elif Choice==2:
        amount=float(input("Enter the amount to deposit : "))
        account.deposit(amount)
    elif Choice==3:
        amount=float(input("Enter the amount to withdraw : "))
        account.withdraw(amount)
    elif Choice==4:
        print("======THANK YOU======")
        exit()
    else:
        print("Please enter a valid choice")

    

    
        