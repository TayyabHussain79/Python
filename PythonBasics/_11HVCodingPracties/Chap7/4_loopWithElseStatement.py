# Else with loop -run when loop end successfully and not run when terminate trough break  

for i in range(9):
    print(i)
else:
    print("Done ! Loop terminate successfully")

# -- not work else here

for i in range(9):
    print(i)
    if i==3:
        break  # Break the loop if encounted
else:
    print("Done ! Loop terminate successfully")

# --> work with continue 

for i in range(9):
    if i==3:
        continue    # skip this instruction and continue to the next iteration
    print(i)
else:
    print("Done ! Loop terminate successfully")