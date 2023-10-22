def main():
    while True:
        menu()
        choice=int(input("Please Choose"))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice ==0:
                ans=input("Do you want to exit ? y/n")
                if ans=="y"or ans=="Y":
                    print("Thank you for using")
                    break # exit system done
                else:
                    continue

            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()
def menu():
    print("==================Student Management System 2023==================")
    print("-----------------------Function Main Menu-------------------------")
    print("\t\t\t\t\t1.Insert Student Info")
    print("\t\t\t\t\t2.Search Student Info")
    print("\t\t\t\t\t3.Delete Student Info")
    print("\t\t\t\t\t4.Modify Student Info")
    print("\t\t\t\t\t5.Sort Student Info")
    print("\t\t\t\t\t6.Total Student Sum")
    print("\t\t\t\t\t7.Show Student Info")

def insert():
    student_list=[]
    while True:
        id=input("Please Input Student ID")
        if not id:
            break
        name=input("Please Input Name")
        if not name:
            break
        try:
            english=int(input("English Result Input"))
            python=int(input("Python Result Input"))
            java=int(input("Java Result Input"))
        except:
            print("Invalid input, not int type and key in again")
            continue
        student={"id":id,"name":name,"english":english,"python":python,"java":java}
        

def search():
    pass
def delete():
    pass
def modify():
    pass
def sort():
    pass
def total():
    pass
def show():
    pass

if __name__ == "__main__":
    main()