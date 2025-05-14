# Class Name is in a pascal (EmployeeName-->First and then all next words capital start)
# isClass-->cammal Case

class Numbers:
    def sum(self):
        return self.a + self.b

# Object of the class
num = Numbers()
num.a = 40
num.b = 60

ans = num.sum()
print(ans)