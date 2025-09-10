def count():
    c1,c2=0,0
    lt=[2,4,5,1,9,7,34,74,9,8]
    for i in lt:
        if(i%2==0):
            c1+=1
        else:
            c2+=1
    print("Evens:",c1,"odds:",c2)
count()