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

def del_user_data(name):
        
    user_found = False
    if not os.path.exists("user_data.json"):
        print("No user data found")
        return
    else:
        with open("user_data.json", "r") as file:
            user_data = json.load(file)
            print(user_data)
        for user in user_data:
            if name.lower() == user["name"].lower():
                user_data.remove(user)
                user_found = True
                break

        if not user_found:
            print("User not found")
        
        with open("user_data.json", "w") as file:
            json_data = json.dump(user_data,file)
        return

del_name = input("Enter name which you want to delete: ")
del_user_data(del_name)    
read_user_data()
