name = input("Type your name: ")
city = input("Type the city where you were born: ")

if city == "Sao Paulo":
    print("\n" + name + ", you're a 'paulista'.")
elif city == "Belo Horizonte":
    print("\n" + name + ", you're a 'mineiro'.")
else:
    print("\n" + name + ", you're a 'carioca'.")
