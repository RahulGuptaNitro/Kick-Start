# Code by- RahulGuptaNitro

for ii in range(1,int(input())+1):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    f=True
    for i in range(n-k+1):
        if a[i]==k:
            for j in range(i,i+k-1):
                if (a[j]-1)!=a[j+1]:
                    f=False
                    break
            if f:
                c+=1
        f=True
    print("Case #" + str(ii) + ": " + str(c))
