def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)
def sumn(n):
    if(n==0):
        return 0
    return n+sumn(n-1)
print(factorial(5))

    