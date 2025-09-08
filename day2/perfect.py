def perfect():
    n=int(input("Enter n:"))
    for i in range(1,n):
        s=0
        for j in range(1,i):
            if(i%j==0):
                s+=j
        if(i==s):
            print(i)
perfect()