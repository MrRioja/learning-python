def to_ask():
    return input("\nWhat do you want to ask\n" +
                 "<I> - To insert a user\n" +
                 "<S> - To search for a user\n" +
                 "<D> - To delete a user\n" +
                 "<L> - To list a user: ").upper()


def insert(dictionary):
    dictionary[
        input("Type login: ").upper()
    ] = [input("\nType the name: ").upper(),
         input("Enter the last access date: "),
         input("What was the last station accessed: ").upper()]
    save(dictionary)


def save(dictionary):
    with open("bd.txt", "a") as file:
        for key, value in dictionary.items():
            file.write(key + ":" + str(value))


def list_dictionary(dictionary):
    return print("\n", dictionary)


def delete(dictionary):
    return dictionary.__delitem__(input("\nType the key you want to delete: ").upper())


def search(dictionary):
    return print(dictionary.get(input("\nType the key you want to search: ").upper()))
