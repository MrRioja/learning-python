equipments = []
values = []
serialNumbers = []
departments = []
answer = "S"

while answer == "S":
    equipments.append(input("Equipment: "))
    values.append(float(input("Value: ")))
    serialNumbers.append(int(input("Serial number: ")))
    departments.append(input("Department: "))
    answer = input("Type \"S\" to continue: ").upper()

search = int(input("Type a serial number to search in the list: "))
for index in range(0, len(equipments)):
    if search == serialNumbers[index]:
        print("\nPosition: ", (index + 1))
        print("Equipment: ", equipments[index])
        print("Value: ", values[index])
        print("Serial number: ", serialNumbers[index])
        print("Department: ", departments[index])
