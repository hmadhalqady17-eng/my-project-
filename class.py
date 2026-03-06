import os 
import time 
memberance=open("gym_membrance.txt","a+")
def clear_screen():
    os.system("cls" if os.name =="nt" else "clear")
class Gym :
    def __init__(self,name ,Id ,status):
        self.name=name
        self.Id=Id
        self.status=status
    def print_all(self):
        print(f"name      : {self.name}")
        print(f"ID     : {self.Id}")
        print(f"status    : {self.status}")
def added():
    n=input("Enter name :")
    D=input("Enter membership ID :")
    s=input("Enter membership status or click enter :")
    if s =="":
        s="inactive"
    return Gym(n,D,s)

def search():
    a=input("Enter your choise :")
    if a=="1":
        q=input("Enter to membership ID to search :")
        for i  in  memberance :
            if i.Id.strip().lower() == q.strip().lower(): 
                print("_"*20)
                i.print_all()
                print("_"*20)
    elif a=="2":
        name1=input("Enter to membership name to search :")
        for i  in  memberance :
            if i.name.lower() == name1.lower() :
                print("_"*20)
                i.print_all()
                print("_"*20)

                
    elif a=="3":
        status1=input(r"Enter to membership status to search active \ inactive :")
        for i  in  memberance :
            if i.status.lower()==status1.lower() :
                print("_"*20)
                i.print_all()
                print("_"*20)

    else :
        print("invended Erorr you must enter 1 or 2 or 3")
                

while True :
    print ("\n choose an action \n")
    print("1.Add new member")
    print("2.Display all member")
    print("3.search for a member")
    print("4.Exit\n")
    x=input("enter your choise :")
    if x=="1":
        added()
        memberance.write(gymer1)
        time.sleep(2)
        print("user added sucessfully!")
        time.sleep(2)
        clear_screen()
    elif x=="2":
        clear_screen()
        if not  memberance:
            print("do not found employee")
            time.sleep(2)
        elif  memberance :
            print("dis play all new gmyer ...") 
            time.sleep(3)    
            for i , gymer1 in enumerate(gymer , start=1):
                print(f"\nGym {i}")
                gymer1.print_all()
                print("_"*20)
            time.sleep(4)
            clear_screen()
    elif x=="3" :
        clear_screen()
        print ("search by :")
        print("1.Membership ID")
        print("2.Membership name")
        print("3.Membership status\n")
        search()
    elif x=="4":
        break
    else :
        print ("invided Error \n you must enter 1 or 2 or 3 or 4 ")



memberance.close()




