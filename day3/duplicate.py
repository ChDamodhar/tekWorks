def dup():
    l=[2,4,6,8,3,4,2,6,10]
    d=set()
    l1=set()
    for i in l:
        if i in l1:
            d.add(i)
        else:
            l1.add(i)
    print(list(d))
dup()