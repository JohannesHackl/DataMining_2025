students = []

check = False
action = 0

while True:
    action = input("""Choose an option:
    1. Add a Student
    2. Remove a Student
    3. Display all Students
    4. Exit
""")
    
    action = int(action)

    if action == 1:
        name = input("Enter the students' name to add.\n")
        students.append(name)
        print(f"Added {name} to the list!")
    elif action == 2:
        while True:
            name = input("Enter the students' name to remove. Or enter \"exit\"\n")
            if students.__contains__(name):
                students.remove(name)
                break    
            elif name.__contains__("exit"):
                break
        print(f"Removed {name} from the list!\n")
    elif action == 3:
        for i in students:
            print(f"{i}, ")
    elif action == 4:
        print("Good Bye\n")
        break

    action = 0
