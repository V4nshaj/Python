import json
import os #os imported to check if the file path already exist
def read_user_data():
        
    if not os.path.exists("user_data.json"):
        print("No user data found")
        return
    else:
        with open("user_data.json", "r") as file:
            user_data = json.load(file)
            print(user_data)
        for user in user_data:
            print(user)
            print("Name: ",user["name"])
            print("Email: ",user["email"])
            print("Contact: ",user["contact"])
            print("\n")
        return

def edit_user_data(name):
        
    user_found = False
    if not os.path.exists("user_data.json"):
        print("No user data found")
        return
    else:
        with open("user_data.json", "r") as file:
            user_data = json.load(file)
            print(user_data)
        for user in user_data:
            if(name == user["name"]):
                new_name = input("Enter new name: ")
                new_email = input("Enter new email: ")
                new_contact = input("Enter new contact: ")
                user["name"] = new_name
                user["email"] = new_email
                user["contact"] = new_contact                
                user_found = True
                break

        if not user_found:
            print("User not found")
        
        with open("user_data.json", "w") as file:
            json_data = json.dump(user_data,file)
        return

edit_name = input("Enter name which you want to edit: ")
edit_user_data(edit_name)    
read_user_data()
