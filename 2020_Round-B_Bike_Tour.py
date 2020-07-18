for ii in range(int(input())):
    n=int(input())
    h=list(map(int,input().split()))
    c=0
    for jj in range(1,n-1):
        if(h[jj-1]<h[jj] and h[jj+1]<h[jj]):
            c+=1
    print("Case #" + str(ii + 1) + ": " + str(c))
