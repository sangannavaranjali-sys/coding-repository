class Node:
    def __init__(self,value=None):
        self.data=value
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
        
    def insert_front(self,value):
        new_node=Node(value)
        if (self.head==None):
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node

    def insert_end(self,value):
        print("hi")
        new_node=Node(value)
        if (self.head==None):
            print("List is empty")
            self.head=new_node
        else:
            cur_node=self.head
            while(cur_node.next):
                cur_node=cur_node.next
            cur_node.next=new_node

    def delete_front(self):
        if (self.head==None):
            print("List is empty, can not delete")
        else:
            del_node=self.head
            print("Deleted item :",del_node)
            self.head=self.head.next
            del del_node

    def delete_end(self):
        if (self.head==None):
            print("List is empty, can not delete")
        else:
            cur_node=self.head
            while(cur_node.next):
                cur_node=cur_node.next
            print("Deleted item : ",cur_node) 
            del cur_node

    def display(self):
        if (self.head==None):
            print("List is empty can not display")
        else:
            cur_node=self.head
            while(cur_node):
                print(cur_node.data,end="  ") 
                cur_node=cur_node.next
               

    def search(self,key):
        if (self.head==None):
            print("List is empty can not search")
        else:
            cur_node=self.head
            while(cur_node):
                if(cur_node.data==key):
                    print("Element found :",key," search successful!!!")
                    return
                cur_node=cur_node.next
            print("Element not found, search unsuccessful!!!")    


ll=SLL()

while True:
    print()
    print("======Choose the operation from menu======")
    print("1.Insert Front")
    print("2.Insert End")
    print("3.Delete Front")
    print("4.Delete End")
    print("5.Display")
    print("6.search")
    print("7.Exit")

    ch=int(input("Enter the choice : "))

    if (ch==1):
        item=int(input("Enter the element to insert : "))
        ll.insert_front(item)
        ll.display()
    elif(ch==2):
        item=int(input("Enter the element to insert : "))
        ll.insert_end(item)
        ll.display()
    elif(ch==3):
        ll.delete_front()
        ll.display()
    elif(ch==4):
        ll.delete_end()
        ll.display()  
    elif(ch==5):
        ll.display()
    elif(ch==6):
        key=int(input("Enter the element to insert : "))
        ll.search(key)
    elif(ch==7):
        exit
    else:
        print("Enter the correct choice from the menu")        







