from Functions import *


users = {}

option = to_ask()

while option == "I" or option == "S" or option == "D" or option == "L":
    if option == "I":
        insert(users)
    option = to_ask()
