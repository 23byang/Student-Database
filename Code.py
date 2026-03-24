student_1 = {
{"Student": "John", "year": 13, "Achieved Credits": 27,"Merit Credits": 42,"Excellence Credits":23}, 
{"Student": "Adam", "year": 12, "Achieved Credits": 25,"Merit Credits": 31,"Excellence Credits":47},
{"Student": "Steven", "year": 13, "Achieved Credits": 35,"Merit Credits": 11,"Excellence Credits":27},
{"Student": "Josh", "year": 12, "Achieved Credits": 23,"Merit Credits": 29,"Excellence Credits":55},
{"Student": "Justin", "year": 12, "Achieved Credits": 24,"Merit Credits": 22,"Excellence Credits":36},
}
def choice_1():
    print(student_1)
def choice_2():
    total_credits = student_1["Achieved Credits"] + student_1["Merit Credits"] + student_1["Excellence Credits"]
    for total_credits >= 60:
        print(student_1)
def choice_3():

def choice_4():

def choice_5():

def choice_6():

def choice_lists(): 
    print(f"Welcome to the Student Database, What Would You Like To Do? ")
    print(f"1. Summary Of Student Data")
    print(f"2. List Of Students That Have Passed NCEA")
    print(f"3. List Of Students That Have An Endorsement")
    print(f"4. Summary Of Students From Year Levels")
    print(f"5. Add Credits To Existing Students")
    print(f"6. Add New Students And Credit Data")
    while True:
        try:
            choice = int(input(f"What Is Your Choice? "))
            if choice == 6: 
                choice_6()
            elif choice == 5:
                choice_5()
            elif choice == 4:
                choice_4()
            elif choice == 3:
                choice_3()
            elif choice == 2:
                choice_2()
            elif choice == 1:
                choice_1()
            else: 
                print(f"Invalid choice.")
                continue
            break
        except ValueError:
            print(f"Invalid choice.")
            continue
    