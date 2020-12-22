def to_ask():
    return input("What do you want to ask\n" +
                 "<I> - To insert a user\n" +
                 "<S> - To search for a user\n" +
                 "<D> - To delete a user\n" +
                 "<L> - To list a user: ").upper()


def insert(dictionary):
    dictionary[
        input("Type login: ").upper()
    ] = [input("Type the name: ").upper(),
         input("Enter the last access date: "),
         input("What was the last station accessed: ").upper()]
