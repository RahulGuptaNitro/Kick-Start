# Code by- RahulGuptaNitro

for ii in range(int(input())):
    n,d=map(int,input().split())
    x=list(map(int,input().split()))
    min=(10**12)+1
    for jj in reversed(x):
        dd=d//jj
        r=dd*jj
        d=r
        if(min>r):
            min=r
    print("Case #" + str(ii + 1) + ": " + str(min))
