# Concatenation of two string (Work only when both are string )(one integer and one string not work)

# FirstName="Tayyab "
# LastName="Shoukat"
# name= FirstName + LastName
# print(name)

# Sting Indexing using [these brakets]

# Name="Tayyab"
# print(Name[4])

# Name[4]=7 --> its doesnot work


# Sring Slicing -->getting part of the string

# Name="Tayyab"
# print(Name[0:6])
# print(Name[3:5])
# print(Name[:6]) # its mean Name[0:6] (minimum tk)
# print(Name[2:]) # its mean Name[2:6] (max mean length tk)

# --> Negative Indexing

# Name="Tayyab"
# print(Name[-5:-1]) # same as Name[1:5]
# print(Name[0:-1]) # same as Name[0:5]
# print(Name[0:0]) # same as Name[0:0]-->hahh Not Work just space show

# --> Slicing with skip value or step
Name="TayyabShoukat"
print(Name[0::1]) # 1 show no effect mens hr value print kro (no skip)
print(Name[0:8:2]) # 2 show that hr 2nd value print (1 skip)
print(Name[0::3]) # 3 show that hr 3rd value print (Two skip)
