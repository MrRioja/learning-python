import json

dictionary = {
    "login": "MrRioja",
    "id": 55336456,
    "avatar_url": "https://avatars3.githubusercontent.com/u/55336456?v=4",
    "url": "https://api.github.com/users/MrRioja"
}


with open("myFirstJSON.json", "w") as file:
    json.dump(dictionary, file)


# with open("user.json", "r") as file:
#     dictionary = json.load(file)
#     for key, value in dictionary.items():
#         print(key + " | " + str(value))


# database = []
# with open("iris.data", "r") as file:

#     for data in file.readlines():
#         database.append(data.split(","))

# # print(database)

# print(float(database[0][0]) + float(database[0][1]))
