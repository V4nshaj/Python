import json
def save_user_data():
    user_list = []

    while True:
        name = input("Enter Name(or 'quit' to exit the program): ")
        if name == 'quit':
            break
        email = input("Enter email: ")
        contact = input("Enter contact: ")

        #creating dictionary
        userdata = {"name": name,
                    "email": email,
                    "contact": contact
                    }
        user_list.append(userdata)
        with open("user_data.json", "w") as file:
            json_data = json.dump(user_list,file)#dump helps in converting and saving file in specific locn

save_user_data()
