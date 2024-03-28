#Serialization meaning converting data into stream to tranfer or save data easily
#JSON is a javascript object notification
#the process of converting data or python dictionary into JSON string is called Serialization
import json
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
json_Data=json.dumps(data)#dumps converts the data into json string
print(type(data))
print(type(json_Data))
print(json_Data)