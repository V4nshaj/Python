import json
import os #os imported to check if the file path already exist
user_list = []
def save_user_data():

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

        if os.path.exists("user_data.json"):
            with open("user_data.json", "r") as file:
                existing_data = json.load(file)
            user_list.extend(existing_data)#extend means old data is also added to the list

        with open("user_data.json", "w") as file:
            json_data = json.dump(user_list,file)#dump helps in converting and saving file in specific locn

save_user_data()
