def Power(x, n):
    if n == 0:
        return 1
    temp = Power(x, n // 2)
    if n % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp
    
print(Power(2, 5))  # Output: 32