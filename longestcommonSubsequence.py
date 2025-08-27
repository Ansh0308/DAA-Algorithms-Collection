def SubSequence(s1,s2):
    
    L=[[0 for i in range(len(s2)+1)]for j in range(len(s1)+1)]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if(s1[i-1]==s2[j-1]):
                L[i][j]=1+L[i-1][j-1]
            else:
                L[i][j]=max(L[i][j-1],L[i-1][j])
    return L[len(s1)][len(s2)]

s1="LONGEST"
s2="STONE"
print(SubSequence(s1,s2))
