def delete():
    lt=[2,4,7,9,0,5,8,9,42,778,28]
    n=int(input("Enter index:"))
    lt=lt[:n-1]+lt[n:]
    print(lt)
delete()