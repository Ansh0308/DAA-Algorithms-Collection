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


print(power(2,5))
print(power_recursive(2,5))