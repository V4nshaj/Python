import json
import os #os imported to check if the file path already exist
user_list = []
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

read_user_data()
