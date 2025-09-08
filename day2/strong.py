def factorial(n):
    c=1
    for i in range(1,n+1):
        c=c*i
    return c

def armstrong():
    n=int(input("Enter number"))
    for i in range(1,n):
        s=0
        n1=i
        while i>0:
            s+=factorial(i%10)
            i//=10
        if(s==n1):
            print(n1)
armstrong()