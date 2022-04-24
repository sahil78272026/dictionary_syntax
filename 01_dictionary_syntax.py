"""# Dictionaries work in key-value pair , they are mutable

myDict = {"First_Name":"Sahil",
"Last_Name":"Garg",
"age" : 31,
"place" : "Ghaziabad",
"Marriage_Status": False, 
"Work": {'Airtel':'Network'}
}

print(myDict)
print(myDict["First_Name"])
print(myDict["Last_Name"])
print(myDict["age"])
myDict["age"] = 30
print(myDict)
print(myDict["Work"]["Airtel"])


"""

myDict = {"Name": "Sahil Garg",
"Place" : "Ghaziabad",
"age": 30}

print(myDict["Name"])
print(type(myDict))
print((myDict.keys()))
print(myDict.items())