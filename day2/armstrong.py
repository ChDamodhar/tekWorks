def armstrong():
    n=int(input("Enter number"))
    
    for i in range(1,n):
        s=0
        n1=i
        while i>0:
            s+=(i%10)**3
            i//=10
        if(s==n1):
            print(n1)
armstrong()