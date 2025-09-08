def factorial():
    n=int(input("Enter n:"))
    c=1
    for i in range(1,n+1):
        c=c*i
    print("factorial of given value is :",c)
factorial()