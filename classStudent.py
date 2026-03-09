class Student:
    def __init__(self,name,roll_num,sub1,sub2,sub3):
        self.name=name
        self.roll_num=roll_num
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    def student(self):
        print("Student Name : ",self.name)
        print("Student Roll Number : ",self.roll_num)
        print("Subject 1 marks : ",self.sub1)
        print("Subject 2 marks : ",self.sub2)
        print("Subject 3 marks : ",self.sub3)
    def Marks(self):
        total_marks=self.sub1+self.sub2+self.sub3
        print("The total marks is : ",total_marks)
    def Avg_marks(self):
        self.avg_marks=(self.sub1+self.sub2+self.sub3)/3
        print("The avarage marks is : ",self.avg_marks)
    def result(self):
        if(self.avg_marks>35):
            print("pass")
        else:
            print("fail")

name=input("Enter the student name : ")
roll_num=int(input("Enter the student roll number : "))
sub1=int(input("Enter the marks of first subject : "))
sub2=int(input("Enter the marks of second subject : "))
sub3=int(input("Enter the marks of third subject : "))
s1=Student(name,roll_num,sub1,sub2,sub3)
s1.student()
s1.Marks()
s1.Avg_marks()
s1.result()