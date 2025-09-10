def wordcount(str):
    feq={}
    for i in str:
        if i in feq:
            feq[i]+=1
        else:
            feq[i]=1
    for i in feq:
        print(i,feq[i],sep='',end='')
wordcount("damodhar")

