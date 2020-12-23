from Functions import *


users = {}

option = to_ask()

while option == "I" or option == "S" or option == "D" or option == "L":
    if option == "I":
        insert(users)
    if option == "S":
        search(users)
    if option == "D":
        delete(users)
    if option == "L":
        list_dictionary(users)
    option = to_ask()
