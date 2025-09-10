def HighFreq(str):
    feq={}
    for i in str:
        if i in feq:
            feq[i]+=1
        else:
            feq[i]=1
    max=str[0]
    for i in feq:
        if feq[max]<feq[i]:
            max=i
    print("highest frequency character is :",max,feq[max])
HighFreq("damodhar")