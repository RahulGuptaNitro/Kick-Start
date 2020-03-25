t=int(input())
for i in range (t):
    n=int(input())
    a=list(map(int,input().split()))
    l=[]
    for j in range (int(n/2)):
        b = a[-j:] + a[:-j]
        l.append(sum(b[:int(n/2)]))
    x=min(l)
    c=l.count(x)
    if (c==len(l)):
        c=0
    print(c)
