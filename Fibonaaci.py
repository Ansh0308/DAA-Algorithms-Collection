def fib(n,a,b):
    if(n==1):
        return b
    if(n==0):
        return a
    c=a+b
    return fib(n-1,b,c)

def fib_memo(n):
    f = [-1 for i in range(n+1)]
    f[0]= 0
    f[1]= 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

print(fib(5,0,1))
