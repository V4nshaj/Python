def save_user_data():
    name= input("Enter name: ")
    email= input("Enter email: ")
    contact= input("Enter contact: ")

    user_data = f"Name: {name}\nEmail: {email}\nContact: {contact}\n"
    with open("user_Data.txt", "a") as file:
        file.write(user_data)

save_user_data()

def read_user_Data():
    with open("user_Data.txt", "r") as file:
        print(file.read())

read_user_Data()