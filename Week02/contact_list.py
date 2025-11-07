def addContact(name, number):
    contacts[name] = number

def removeContact(name):
    contacts.pop(name)

def getContact(name):
    contacts[name]
def printContacts():
    for i in contacts:
        print(i, contacts[i])

contacts = {}

        
while True:
    action = input("""
    1. add contact
    2. remove contact
    3. display all
    4. exit
                   
    """)
    action = int(action)

    if action == 1:
        name = input("enter the name\n")
        number = input("enter the number\n")
        addContact(name, number)
    elif action == 2:
        name = input("enter the name to remove\n")
        if contacts.__contains__(name):
            removeContact(name)
            print(f"removed {name}")
    elif action == 3:
        for person in contacts:
            print(f"Name: {person}, Number: {contacts[person]}")
    elif action == 4:
        break
    else:
        print("please enter a valid number 1-4")