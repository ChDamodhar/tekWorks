def pattern2():
    n= int(input("Enter n:"))
    for i in range(n):
        for j in range(n):
            if(i==j):
                print("$",end=" ")
            else:
                print("*",end=" ")
        print("\n")
pattern2()