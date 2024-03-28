#Serialization meaning converting stream into data
#JSON is a javascript object notification
#the process of converting JSON string into data or python dictionary is called Deserialization
import json

json_Data='{"name": "John Doe", "age": 30, "city": "New York"}'

data = json.loads(json_Data)#loads converts the json string into data
print(type(json_Data))
print(type(data))
print(data)
print(data["name"])
print(data["age"])
print(data["city"])