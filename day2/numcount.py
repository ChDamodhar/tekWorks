def numcount():
    n=int(input("enter n:"))
    s=0
    while(n>0):
        s+=1
        n//=10
    return s
print(numcount())
