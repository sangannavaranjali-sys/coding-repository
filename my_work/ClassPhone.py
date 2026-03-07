class Phone:
    def __init__(self,name,brand,colour,memory):
        self.name=name
        self.brand=brand
        self.colour=colour
        self.memory=memory
        self.list=[]
        self.list1=[]
        self.battery=100

    def showdetails(self):
        print("Mobile Phone company name :",self.name)
        print("The mobile phone brand i : ",self.brand)
        print("The colour of the mobile phone",self.colour)
        print("The memory of the mobile phone is : ",self.memory)

    def call(self):
        if self.battery>20:
            num=(input("Enter the phone number : +19"))    
            lenght=len(num)
            if (lenght==10):
                print("Dailing!!!!!")
                self.list.append(num)
                self.battery=self.battery-10
            else:
                print("Enter the correct phone number")  
                return  
        else:
            print("Battery is running low. Please charge it")

    def message(self):
        if self.battery>20:
            num=(input("Enter the phone number to send message : "))
            lenght=len(num)
            if (lenght==10):
                msg=input("Enter the message to send : ")    
                print("Message sent!!!")
                self.list1.append((num,msg))
                if self.battery>0:
                    self.battery=self.battery-5
            else:
                print("Please enter the correct contact number")
                return
        else:
            print("Battery is running low. Please charge it")    

    def playmusic(self):
        if self.battery>20:
            music=input("Enter the song name : ")
            print("Plyaing",music,"music") 
            if self.battery>0:
                self.battery=self.battery-15
        else:
            print("Battery is running low. Please charge it")
            
real_p=12345   
password=int(input("Enter the password : "))
if(real_p==password):
    print("The password is correct")
else:
    print("The password is incorrect")   
    exit() 

name=input("Enter the phone company name : ")
brand=input("Enter the mobile phone brand name : ")
colour=input("Enter the mobile phone colour : ")
memory=input("Enter the memory of the mobile phone : ")

phone1=Phone(name,brand,colour,memory)

while True:
    print("========Menu========")
    print("1.Show the details of the Mobile phone")
    print("2.Make a call")
    print("3.Send a message")
    print("4.Play a music")
    print("5.Show call history")
    print("6.Show message history")
    print("7.Show phone battery")
    print("8.Exit")

    Choice=int(input("Enter a choice number from the menu : "))

    if phone1.battery>20:
        if Choice==1:
            phone1.showdetails()
        elif Choice==2:
            phone1.call()
        elif Choice==3:
            phone1.message()
        elif Choice==4:
            phone1.playmusic()
        elif Choice==5:
            print(phone1.list) 
        elif Choice==6:
            if not phone1.list1:
                print("History is empty")
            else:    
                print(phone1.list1)
        elif Choice==7:
            print(phone1.battery)

        elif Choice==8:
            exit()
        else:
            print("Please enter a valid number!!!")                    
    else:
        print("Battery running slow please charge it./n current battery :  ",phone1.battery)
        exit()
