# Got only 11 points on this submission 
for ii in range(int(input())):
    n=input()
    for kk in range(n.count('(')):
        cl = n.index(")")
        ol = n[:cl].rindex("(")
        z=n[ol+1:cl]
        n= n[:ol-1]+(int(n[ol-1])*z)+n[cl+1:]
    h,w=1,1
    h-=n.count("N")
    if(h<1):
        h=1000000000+h
    h += n.count("S")
    if (h > 1000000000):
        h = h-1000000000
    w -= n.count("W")
    if (w < 1):
        w = 1000000000 +w
    w += n.count("E")
    if (w > 1000000000):
        w = w - 1000000000
    print("Case #" + str(ii + 1) + ": " + str(w)+ " "+str(h))
