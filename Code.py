student_list = [
{"Student": "John", "Year": 13, "Not Achieved Credits": 5, "Achieved Credits": 27,"Merit Credits": 42,"Excellence Credits":23}, 
{"Student": "Adam", "Year": 12, "Not Achieved Credits": 0, "Achieved Credits": 25,"Merit Credits": 31,"Excellence Credits":60},
{"Student": "Steven", "Year": 13, "Not Achieved Credits": 4, "Achieved Credits": 35,"Merit Credits": 11,"Excellence Credits":27},
{"Student": "Josh", "Year": 12, "Not Achieved Credits": 11, "Achieved Credits": 23,"Merit Credits": 29,"Excellence Credits":55},
{"Student": "Justin", "Year": 12, "Not Achieved Credits": 8, "Achieved Credits": 24,"Merit Credits": 22,"Excellence Credits":36},
]
def student_summary():
    print(student_list)
    choice_lists()
def ncea_passed():
    for i in student_list:
        total_credits = i["Achieved Credits"] + i["Merit Credits"] + i["Excellence Credits"]
        if total_credits > 59:
            print(f"{i["Student"]} has passed with {total_credits} credits")
    choice_lists()
def endorsed_students():
    for i in student_list:
        total_credits = i["Achieved Credits"] + i["Merit Credits"] + i["Excellence Credits"]
        if total_credits > 59:
            endorsement_credits = i["Merit Credits"] + i["Excellence Credits"]
            if endorsement_credits > 59:
                if i["Excellence Credits"] > 59:
                    print(f"{i["Student"]} has Excellence Endorsement")
                else:
                    print(f"{i["Student"]} has Merit Endorsement")
            else:
                print(f"{i["Student"]} has Achieved Endorsement")
        else:
            print(f"{i["Student"]} has Not Achieved Endorsement")
    choice_lists()
def year_levels():
    year_level = int(input(f"What Year Level Would You Like To Observe "))
    for student in student_list:
        if student["Year"] == year_level:
            print(student)
    choice_lists()
def add_credits():
    student_found = None
    student_name = input(f"What is the name of the student you want to add credits to? ").lower()
    for student in student_list:
        if student["Student"].lower() == student_name:
            student_found = student
            break
    if student_found:
        while True:
            credit_type = input(f"What kind of credits would you like to add, Not Achieved, Achieved, Merit & Excellence. ").title().strip()
            key = f"{credit_type} Credits"
            if key in student_found:
                credits_added = int(input(f"How Many Credits would you like to add? "))
                student_found[key] += credits_added
                print(f"{student_found["Student"]} now has {student_found[key]} {credit_type} credits")
                break
            else:
                print(f"Invalid Credit Type. ")
                continue
    elif not student_found:
        print(f"Student Name does not exist.")
        add_credits()
        return
    choice_lists()
def add_students():
    name = input(f"What is the name of the student you would like to add? ").strip().title()
    for student in student_list:
        if student["Student"] in student_list:
            print(f"Student already exists.")
            choice_lists()
    while True:
        try:
            year = int(input(f"What is the {name}'s year level? "))
            break
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
    student_list.append(new_student)
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
                add_students()
            elif choice == 5:
                add_credits()
            elif choice == 4:
                year_levels()
            elif choice == 3:
                endorsed_students()
            elif choice == 2:
                ncea_passed()
            elif choice == 1:
                student_summary()
            else: 
                print(f"Invalid choice.")
                continue
            break
        except ValueError:
            print(f"Invalid choice.")
            continue
choice_lists()
    