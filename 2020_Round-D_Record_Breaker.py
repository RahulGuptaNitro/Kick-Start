# Code by- RahulGuptaNitro

for ii in range(int(input())):
    n=int(input())
    d=[-1]+list(map(int, input().split()))+[-1]
    m,c=-1,0
    for jj in range(0,n+1):
        if d[jj]>m:
            m=d[jj]
            if d[jj + 1] < d[jj]:
                c+=1
    print('Case #'+str(ii+1)+': '+str(c))
