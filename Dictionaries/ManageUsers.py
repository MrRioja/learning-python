from Functions import to_ask


users = {}

option = to_ask()

while option == "I" or option == "S" or option == "D" or option == "L":
    if option == "I":
        users[input("Type login: ").upper()] = [input("Type the name: ").upper(), input(
            "Enter the last access date: "), input("What was the last station accessed: ").upper()]
    option = to_ask()
