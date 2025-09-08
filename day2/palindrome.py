def palindrome():
    n=int(input("Enter number"))
    for i in range(1,n):
        s1=str(i)
        s2=s1[::-1]
        if(s1==s2):
            print(i)
palindrome()