inventory = []
answer = "S"

while answer == "S":
    inventory.append(input("Equipment: "))
    inventory.append(float(input("Value: ")))
    inventory.append(int(input("Serial number: ")))
    inventory.append(input("Department: "))
    answer = input("Type \"S\" to continue: ").upper()

for element in inventory:
    print(element)
