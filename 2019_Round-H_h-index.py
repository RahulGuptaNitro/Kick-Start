# Code by- RahulGuptaNitro

t=int(input())
for i in range(0,t):
    c=1
    count=0
    n=int(input())
    a = list(map(int,input().split()))
    print("Case #" + str(i+1) + ":", end=" ")
    for j in range(0,n):
        if(a[j]>c):
            count=count+1
        if(count>c):
            c=count
        print (c, end=" ")
