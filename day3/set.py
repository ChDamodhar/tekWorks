def AddSet():
    n=int(input("Enter set size:"))
    s=set()
    for i in range(n):
        s.add(int(input("Enter element")))
    print(s)
AddSet()