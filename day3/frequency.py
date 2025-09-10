def frequency():
    l=[1,2,3,3,3,5,5,5,5,5,6,6,6,6]
    feq={}
    for i in l:
        if i in feq:
            feq[i]+=1
        else:
            feq[i]=1
    print(feq)
frequency()