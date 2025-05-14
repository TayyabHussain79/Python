
# Break

for i in range(9):
    print(i)
    if i==3:
        break  # Break the loop if encounted
else:
    print("Done ! Loop terminate successfully")

# Continue 

for i in range(9):
    if i==3:
        continue    # skip this instruction and continue to the next iteration
    print(i)
else:
    print("Done ! Loop terminate successfully")


# Pass  --> none ! Do nothing
i=0
if i<5:
    pass

for i in range(8):
    pass

def hellos():
    pass