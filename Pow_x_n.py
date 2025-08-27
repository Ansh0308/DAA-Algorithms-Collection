def power(base,exp):
    if(exp<0):
        base=1/base
        exp=-1*exp
    ans=1
    for i in range(exp):
        ans=ans*base
    return ans

def power_recursive(base,exp):
    if(exp == 0):
        return 1
    return base*power_recursive(base,exp-1)

def Power(x, n):
    if n == 0:
        return 1
    temp = Power(x, n // 2)
    if n % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp
    
print(Power(2, 5))  # Output: 32
    
def Power_n(x, n):
    if n == 0:
        return 1
    
    if n % 2 == 0:
        return Power_n(x, n // 2) * Power_n(x, n // 2)
    else:
        return x * Power_n(x, n // 2) * Power_n(x, n // 2)


# print(Power_n(2, 5))  # Output: 32

def myPow(x: float, n: int) -> float:
    biForm = n
    ans = 1.0
    if n < 0:
        biForm = -biForm
        x = 1 / x
    while biForm > 0:
        if biForm % 2 == 1:
            ans *= x
        x *= x
        biForm //= 2
    return ans


# print(power(2,5))
# print(power_recursive(2,5))
print(Power(2, 5))  # Output: 32