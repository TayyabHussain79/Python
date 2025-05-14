# Sets --> collection of non-reptitative elements {}

s1={2,4,5,6,7,2}
print(s1)
print(type(s1))


# ---> Empty set creation
# s1={} #--> Error! no its a dict
# print(type(s1))

# So the way to create the empty set is 
s1=set()
print(type(s1))

# Add function can add values, tuples but no list,dict that are unhasable means these can changes
s1.add(5)
s1.add(4)
s1.add(5)
s1.add("Tayyab")
s1.add((3,5,"Tayyab")) #---> Tuples can added
print(s1)
# s1.add([3,5,"Tayyab"]) #---> List can  not added
# s1.add({"Name":"Tayyab"}) #---> Dictionary can not added