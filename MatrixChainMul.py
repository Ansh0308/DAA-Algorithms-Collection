import math
def mcm(d):
    n=len(d)
    m=[[0 for _ in range(n)]for _ in range(n)]
    K=[[0 for _ in range(n)]for _ in range(n)]
    for D in range(1,n):
        for i in range(1,n-D):
            j=i+D
            m[i][j]=float('inf')
            for k in range(i,j):
                q=m[i][k]+m[k+1][j]+(d[i-1]*d[k]*d[j])
                if(q<m[i][j]):
                    m[i][j]=q
                    K[i][j]=k
                    
    return m[1][n-1]

d=[3,4,2,3]
print(mcm(d))
                    
        