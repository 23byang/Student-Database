student_list = [
{"Student": "John", "Year": 13, "Not Achieved Credits": 5, "Achieved Credits": 27,"Merit Credits": 42,"Excellence Credits":23}, 
{"Student": "Adam", "Year": 12, "Not Achieved Credits": 0, "Achieved Credits": 25,"Merit Credits": 31,"Excellence Credits":60},
{"Student": "Steven", "Year": 13, "Not Achieved Credits": 4, "Achieved Credits": 35,"Merit Credits": 11,"Excellence Credits":27},
{"Student": "Josh", "Year": 12, "Not Achieved Credits": 11, "Achieved Credits": 23,"Merit Credits": 29,"Excellence Credits":55},
{"Student": "Justin", "Year": 12, "Not Achieved Credits": 8, "Achieved Credits": 24,"Merit Credits": 22,"Excellence Credits":36},
]
pass_requisite = 60


def student_summary(database):
    for student in database:
        print(student)
    choice_lists()


def ncea_passed_calculator(database):
    passed_list = []
    for student in database:
        total_credits = (student["Achieved Credits"] + student["Merit Credits"] + student["Excellence Credits"])
        if total_credits >= pass_requisite:
            passed_list.append(f"{student["Student"]} (Total: {total_credits} credits)")
    return passed_list


def ncea_passed(database):
    result = ncea_passed_calculator(database)
    if result:
        print(f"NCEA Passed:")
        for students in result:
            print(students)
    else:
        print(f"No Students Have Passed.")
    choice_lists()


def endorsed_students(database):
    for i in database:
        total_credits = i["Achieved Credits"] + i["Merit Credits"] + i["Excellence Credits"]
        if total_credits >= pass_requisite:
            endorsement_credits = i["Merit Credits"] + i["Excellence Credits"]
            if endorsement_credits >= pass_requisite:
                if i["Excellence Credits"] >= pass_requisite:
                    print(f"{i["Student"]} has Excellence Endorsement")
                else:
                    print(f"{i["Student"]} has Merit Endorsement")
            else:
                print(f"{i["Student"]} has Achieved Endorsement")
        else:
            print(f"{i["Student"]} has Not Achieved Endorsement")
    choice_lists()


def year_levels(database):
    while True:
        try:
            year_level = int(input(f"What Year Level Would You Like To Observe "))
            if year_level in range(11,14):
                for student in database:
                    if student["Year"] == year_level:
                        print(student)
                break
            else:
                print(f"Invalid Year, Please choose between 11-13")
                break
        except ValueError:
            print(f"Invalid Year, Please choose between 11-13")
            break
    choice_lists()


def add_credits(database):
    student_found = None
    while student_found is None:
        student_name = input(f"What is the name of the student you want to add credits to? ").lower()
        for student in database:
            if student["Student"].lower() == student_name:
                student_found = student
                break
        if not student_found:
            print(f"Student Name does not exist.")
    if student_found:
        while True:
            credit_type = input(f"What kind of credits would you like to add, Not Achieved, Achieved, Merit & Excellence. ").title().strip()
            key = f"{credit_type} Credits"
            if key in student_found:
                while True:
                    try:
                        credits_added = int(input(f"How Many Credits would you like to add? "))
                        if credits_added > 0:
                            student_found[key] += credits_added
                            print(f"{student_found["Student"]} now has {student_found[key]} {credit_type} credits")
                            break
                        else:
                            print(f"Invalid Number, Please input a positive integer.")
                    except ValueError:
                        print(f"Invalid number, Please input a positive integer.")
                break
            else:
                print(f"Invalid Credit Type. ")
                continue
    elif not student_found:
        print(f"Student Name does not exist.")
        add_credits()
        return
    choice_lists()


def add_students(database):
    name = input(f"What is the name of the student you would like to add? ").strip().lower().title()
    name_exist = False
    for student in database:
        if student["Student"] == name:
            name_exist = True
    if name_exist == True:
        print(f"Student Already Exists, returning to main menu.")
        return choice_lists()
    else:
        while True:
            try:
                year = int(input(f"What is {name}'s year level? "))
                if year in range (11,14):
                    break
                else:
                    print(f"Invalid Year Level")
                continue
            except ValueError:
                print(f"Invalid Year Level")
    credits = {}
    types = ["Not Achieved", "Achieved", "Merit", "Excellence"]
    for credit_types in types:
        while True:
            try:
                amount = int(input(f"How Many {credit_types} credits? "))
                if amount < 0:
                    print(f"Credits cannot be negative.")
                    continue
                credits[f"{credit_types} Credits"] = amount
                break
            except ValueError:
                print(f"Invalid Input, please input a positive integer.")
    new_student = {"Student": name , "Year": year , "Not Achieved Credits": credits["Not Achieved Credits"], "Achieved Credits": credits["Achieved Credits"],"Merit Credits": credits["Merit Credits"],"Excellence Credits":credits["Excellence Credits"]}
    database.append(new_student)
    print(f"{name} has been added to the database.")
    choice_lists()


def choice_lists(): 
    print(f"\nWelcome to the Student Database, What Would You Like To Do? ")
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
                add_students(student_list)
            elif choice == 5:
                add_credits(student_list)
            elif choice == 4:
                year_levels(student_list)
            elif choice == 3:
                endorsed_students(student_list)
            elif choice == 2:
                ncea_passed(student_list)
            elif choice == 1:
                student_summary(student_list)
            else: 
                print(f"Invalid choice.")
                continue
            break
        except ValueError:
            print(f"Invalid choice.")
            continue
choice_lists()
    