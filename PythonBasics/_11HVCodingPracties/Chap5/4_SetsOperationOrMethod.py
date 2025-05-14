# Sets Operations of Methods in Python
s1=set()  # Empty Set

#  1) Add --> add value in the set
s1.add("Tayyab")
s1.add("Umer")
s1.add("Ashr")
s1.add(67)
s1.add((3,4,5))

print(s1)

# 2) Remove --> remove item from the set

s1.remove((3,)) #--> not work
s1.remove("Ashr")
print(s1)

# 3) len --> return the length of the set
print(len(s1))
print(s1.__len__())

# 4) pop --> remove and return the arbitory item form the set (merzi he us ki)

# print(s1.pop())
# print(s1)

# 5) clear --> empty the set

# s1.clear()
# print(s1)

# 6) Union --> Return the Union of the two sets
s2={5,3,7,"Tayyab",5}
s3=s1.union(s2)
print(s3)
s4=s1.union({4,6})
print(s4)


#  7) Intersection --> return the set which is the intersection of the two sets means common value in  the both the sets
s3=s1.intersection(s2)
print(s3)
s4=s1.intersection({4,67,5})
print(s4)

