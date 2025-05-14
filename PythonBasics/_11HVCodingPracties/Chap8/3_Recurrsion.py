# RecursionFunciton  --> call function itself
#  ( must include base condition in program to control the inifinty time calling funtion)
#  (The direct way to code the  algorithm )

# Factorial Program --- Iterative Method

def factorial_iterative(n):
    factorial = 1
    for i in range(n):
        factorial = factorial*(i+1) # Because i start from 0 
    return factorial

print("Factorial is ", factorial_iterative(5))


# Factorial Program --- Recursion Method

# n! = 1 * 2 * 3 * 4 *....* n
# n! = [1 * 2 * 3 * 4 *....*(n-1)]* n
# n! = (n-1)! * n or n * (n-1)!

def factorial_recursion(n):
    if n==0 or n==1:
        return 1
    else:
        return  n * factorial_recursion(n-1)
 

print("Factorial is ", factorial_recursion(5))


