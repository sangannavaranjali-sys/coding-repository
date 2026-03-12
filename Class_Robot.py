class Robot:
    def __init__(self,name,R_id,):
        self.name = name
        self.R_id = R_id
        self.battery = 100
        self.X = 0
        self.Y = 0

    def move(self,direction,steps):
        if self.battery<=20:
            print("Battery running low, Please charge it!!!")
            exit()
        else:
            if direction == 1:
                self.Y=self.Y+steps 
                print("Robot moved in",direction,"by",steps,"steps")
                print("Current position :") 
                print("X position",self.X)
                print("Y position : ",self.Y)
                self.battery = self.battery-10
                print("Current battery",self.battery)
            elif direction == 2:
                self.Y=self.Y-steps
                print("Robot moved in",direction,"by",steps,"steps")
                print("Current position :") 
                print("X position",self.X)
                print("Y position : ",self.Y)
                self.battery = self.battery-10
                print("Current battery",self.battery)
            elif direction == 3:
                self.X=self.X+steps
                print("Robot moved in",direction,"by",steps,"steps")
                print("Current position :") 
                print("X position",self.X)
                print("Y position : ",self.Y) 
                self.battery = self.battery-10
                print("Current battery",self.battery)
            elif direction == 4:
                self.X=self.X-steps
                print("Robot moved in",direction,"by",steps,"steps")
                print("Current position :") 
                print("X position",self.X)
                print("Y position : ",self.Y) 
                self.battery = self.battery-10
                print("Current battery",self.battery)
            else:
                print("Enter correct choice")

    def detect_obstacle(self,distance):
        if self.battery<=20:
            print("Battery running low, Please charge it!!!")
            exit
        else:
            if (distance>5):
                print("Obstacale ditected")
            else:
                print("Clear path!!")
                self.battery=self.battery-10
    
    def R_status(self):
        if self.battery<=20:
            print("Battery running low, Please charge it!!!")
            exit
        else:
            print("Showing current robot status")
            print("X posotion : ",self.X)    
            print("Y posotion : ",self.Y)  
            self.battery=self.battery-10         

    def recharge(self): 
        if (self.battery==100):
            print("The charge is already full!!!")
        else:
            if (self.X ==0 & self.Y==0):
                print("Robot is charging")  
                self.battery=100
            else:
                print("Please return to the base place")    

    def back_to_place(self):
        print("Robo is back to it's place")
        self.x=0
        self.y=0    
              
    def Show_details(self):
        if self.battery<=20:
            print("Battery running low, Please charge it!!!")
            exit
        else:
            print("Roboat name : ",self.name)
            print("Roboat ID : ",self.R_id)
            print("Roboat battery : ",self.battery)
            print("X position : ",self.X)
            print("Y position : ",self.Y)
            self.battery=self.battery-10

print("Fill the robot details")
name=input("Enter the robot name : ")
R_id=input("Enter the robot id : ")

robot=Robot(name,R_id)

print("======Roboat action menu======")
print("1.Move robot")
print("2.Detect obstacal")
print("3.Show status")
print("4.Recharge robot")
print("5.Show details")
print("6.Exit")

while True:

    print("======Roboat action menu======")
    print("1.Move robot")
    print("2.Detect obstacal")
    print("3.Show status")
    print("4.Recharge robot")
    print("5.Return to base ")
    print("6.Show details")
    print("7.Exit")

    choice=int(input("Enter a choice number from the menu : "))

    if choice==1:
        print("Moving robot")
        print("1.UP")
        print("2.DOWN")
        print("3.RIGHT")
        print("4.LEFT")
        direction=int(input("Enter a direction : "))
        steps=int(input("Enter the steps : "))
        robot.move(direction,steps)
    elif choice==2:
        distance=int(input("Enter the distance :" ))
        robot.detect_obstacle(distance)
    elif choice==3:
        robot.R_status()
    elif choice==4:
        robot.recharge()
    elif choice==5: 
        robot.back_to_place()   
    elif choice==6:
        robot.Show_details()
    elif choice==7:
        exit()
    else:
        print("Enter the correct choice")                    
  

        
