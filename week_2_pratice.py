

def add(name_grade_dict):
    name=input("enter your name")
    grade=input ("enter your grade")
    name_grade_dict[name]=grade
    return name_grade_dict

def delete(name_grade_dict):
    name=input ("enter the name of the record which you want to delete")
    if name in name_grade_dict.keys():
        name_grade_dict.pop(name)
        print("deleted")
    else:
        print("name not found")
        Print(" press 1 for entering the name again or 2 to return to main menu")
        option= int(input())
        if option==1:
            delete(name_grade_dict)
    return name_grade_dict
    
def update (name_grade_dict):
    name=input ("Enter the name of the record to update")
    if name in name_grade_dict.keys():
        option=int(input ("enter 1 for updating name \n Enter 2 for updating grade"))
        if option ==1:
             grade=name_grade_dict[name]
             new_name=input("enter new name")
             name_grade_dict.pop(name)
             name_grade_dict[new_name]=grade
        elif option==2:
            new_grade=input("enter new grade")
            name_grade_dict[name]=new_grade
    else:
        update(name_grade_dict)
    return name_grade_dict
        
def search(name_grade_dict):
    name=input ("Enter the name of the record to search")
    if name in name_grade_dict.keys():
        print("Grade of" , name, "is", name_grade_dict[name])
    else:
        print("Name not found")
        print(" press 1 for entering the name again or 2 to return to main menu")
        option= int(input())
        if option==1:
            search(name_grade_dict)
    
name_grade_dict={}
while (1):
    option=int(input(" Enter 1 for adding a student name \n Enter 2 for deleting a student name \n Enter 3 for update \n Enter 4 for search\n"))
    if option==1:
        add(name_grade_dict)
    if option ==2:
        delete(name_grade_dict)
    if option ==3:
        update (name_grade_dict)
    if option ==4:
        search(name_grade_dict) 
