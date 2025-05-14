# Dictionary - Collection of key- value pairs

# Creating {}
myDic={
    "Name": "Tayyab",
    "RollNo": 30120179,
    "Marks": [99,89,90],
    "AnotherDic": {"Age":21,"cost":"Quarashi"}
}

# Access and indexing
print(myDic)
print(type(myDic))
print(myDic["Name"])
print(myDic["Marks"])
print(myDic["AnotherDic"])
print(myDic["AnotherDic"]["Age"])

# Changing

myDic["Name"]="Tayyab Shoukat"
print(myDic)

# practice
# print(myDic["Marks","RollNo"]) --> not work

