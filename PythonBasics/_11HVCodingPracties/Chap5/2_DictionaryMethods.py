# Dictonary Methods

myDic={
    "name": "Tayyab",
    "rollNo": 30120179,
    "marks": [99,89,90],
    "anotherDic": {"age":21,"cost":"Quarashi"},
    3:5
}

# 1) keys --> return list of keys in the list but its type is dict_keys you can change it to list 

# print(myDic.keys())
# print(type(myDic.keys()))
# print(list(myDic.keys()))

# 2) values --> return list of valuess in the list but its type is dict_value you can change it to list 

# print(myDic.values())
# print(type(myDic.values()))
# print(list(myDic.values()))

# 3) items --> return the list of (keys,values) tuples and its type is dict_items you can also convert it

print(myDic.items())
print(type(myDic.items()))
print(list(myDic.items()))

# 4) update --> update the list to adds these content at the end the dictionary and if value is already present it will change it

myDic.update({"Degree":"BCS","name":"Tayyab Shoukat",5:4})
# myDic.update(anotherDicName) #--> its works means another dic add to this dic
print(myDic)

# 5) get --> give the value of the current key and if value not present retrun (none) not show any error
# as same as myDic[""] but if key not present this wala show error uppr wla show no error
print(myDic.get("name"))
print(myDic["name"])
# Difference
print(myDic.get("name2")) #-->Show no error return none
# print(myDic["name2"]) #-->Show error

