#CS AA
#Johan Ramirez
#Ysha Manalo
#Dylan Aguado
#Zachy Garcia

requirements = []
new_requirements = []
import datetime
#Inital Input of requirements
print("Hello welcome to the requirements tracker!")
while True:
    try:
        a_req = int(input("How many requirements would you like to enter first: "))
        if a_req >= 0:
            break
        else:
            print("Please enter a non-negative number.")
    except ValueError:
            print("Invalid input, Please enter a number.")

for i in range(a_req):
    subject = input(f"Enter a requirement: ")
    while True:
        due_date = input("Enter the due date of the requirement (MM/DD/YYYY): ")
        try:
            datetime.datetime.strptime(due_date, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format, Please use MM/DD/YYYY.")
    while True:
        try:
            difficulty = int(input("Enter the difficulty of the requirement (1-5): "))
            if 1 <= difficulty <= 5:
                break
            else:
                print("Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid input, Please enter a number.")
    requirements.append([subject, due_date, difficulty])
    i+1

def sort_date(d):
    return datetime.datetime.strptime(d, "%m/%d/%Y")

sorted_dates = sorted(
    requirements,
    key = lambda a: (sort_date(a[1]),-a[2])
)

print("List of Requirements!")
for b in sorted_dates:
    print(f"{b[0]}|{b[1]}|Difficulty: {b[2]}")

while True:
    print("------- Requirements Tracker -------")
    print("1. Add a new requirement")
    print("2. Edit an existing requirement")
    print("3. Delete and existing requirement")
    print("4. Check a completed requirement")
    print("5. Exit the Requirements Tracker")

    while True:
        try:
            choice = int(input("What would you like to do? (Enter 1-5): "))
            if choice in [1, 2, 3, 4, 5]:
                break
            else:
                print("Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid input, Please enter a number.")
            
            
    
    #1
    if choice == 1:
        subject = input("Enter the requirement: ")
        while True:
            due_date = input("Enter the due date of the requirement (MM/DD/YYYY): ")
            try:
                datetime.datetime.strptime(due_date, "%m/%d/%Y")
                break
            except ValueError:
               print("Invalid date format, Please use MM/DD/YYYY.")
        while True:
            try:
                difficulty = int(input("Enter the difficulty of the requirement (1-5): "))
                if 1 <= difficulty <= 5:
                    break
                else:
                    print("Please enter a number from 1 to 5.")
            except ValueError:
                print("Invalid input, Please enter a number.")
        requirements.append([subject, due_date,difficulty])
        def sort_date(d):
            return datetime.datetime.strptime(d, "%m/%d/%Y")

        sorted_dates = sorted(
        requirements,
        key = lambda a: (sort_date(a[1]),-a[2])
        )


        print("List of Requirements!")
        for b in sorted_dates:
            print(f"{b[0]}|{b[1]}|Difficulty: {b[2]}")
            
    #2
    elif choice == 2:
        while True:
            subject = input("Enter the requirement: ")
            while True:
                due_date = input("Enter the due date of the requirement (MM/DD/YYYY): ")
                try:
                    datetime.datetime.strptime(due_date, "%m/%d/%Y")
                    break
                except ValueError:
                    print("Invalid date format, Please use MM/DD/YYYY.")
            while True:
                try:
                    difficulty = int(input("Enter the difficulty of the requirement (1-5): "))
                    if 1 <= difficulty <= 5:
                        break
                    else:
                        print("Please enter a number from 1 to 5.")
                except ValueError:
                    print("Invalid input, Please enter a number.")
            new_requirement =[subject, due_date, difficulty]
            if new_requirement in requirements:
                requirements.remove(new_requirement)
                print("Please enter the new details of the requirement\n")
                subject = input("Enter the requirement: ")
                due_date = input("Enter the deadline  (MM/DD/YYYY): ")
                difficulty = int(input("Enter the difficulty of the requirement (1-5): "))
                requirements.append([subject,due_date,difficulty])
                def sort_date(d):
                    return datetime.datetime.strptime(d, "%m/%d/%Y")
                
                sorted_dates = sorted(
                requirements,
                key = lambda a: (sort_date(a[1]),-a[2])
                )

                print("List of Requirements!")
                for b in sorted_dates:
                    print(f"{b[0]}|{b[1]}|Difficulty: {b[2]}")
                break
            else:
                print("Requirement not found, please input the information needed again")
    #3
    elif choice == 3:
        while True:
            subject = input("Enter the requirement: ")
            
            while True:
                due_date = input("Enter the due date of the requirement (MM/DD/YYYY): ")
                try:
                    datetime.datetime.strptime(due_date, "%m/%d/%Y")
                    break
                except ValueError:
                    print("Invalid date format, Please use MM/DD/YYYY.")
            while True:
                try:
                    difficulty = int(input("Enter the difficulty of the requirement (1-5): "))
                    if 1 <= difficulty <= 5:
                        break
                    else:
                        print("Please enter a number from 1 to 5.")
                except ValueError:
                    print("Invalid input! Please enter a number.")
            new_requirement =[subject, due_date, difficulty]
            if new_requirement in requirements:
                requirements.remove(new_requirement)
                def sort_date(d):
                    return datetime.datetime.strptime(d, "%m/%d/%Y")
                
                sorted_dates = sorted(
                requirements,
                key = lambda a: (sort_date(a[1]),-a[2])
                )

                print("List of Requirements!")
                for b in sorted_dates:
                    print(f"{b[0]}|{b[1]}|Difficulty: {b[2]}")
                break
            else:
                print("Requirement not found, please input the information needed again")
    #4
    elif choice == 4:
        def sort_date(d):
            return datetime.datetime.strptime(d, "%m/%d/%Y")
                
        sorted_dates = sorted(
        requirements,
        key = lambda a: (sort_date(a[1]),-a[2])
        )

        print("List of Requirements!")
        for b in sorted_dates:
            print(f"{b[0]}|{b[1]}|Difficulty: {b[2]}")
    #5
    elif choice == 5:
        input("Please press any button to close the program, thank you for using the requirements tracker!")
        break
