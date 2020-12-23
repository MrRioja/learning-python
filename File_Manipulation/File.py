with open("myFirstFile.txt", "r") as file:
    for line in file.readlines():
        print(line)
