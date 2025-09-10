def SecLar():
    lt=[2,4,7,9,3,44,27]
    m1=lt[0]
    m2=lt[1]
    for i in lt:
        if i > m1:
            m1,m2=i,m1
        elif i > m2 and i < m1:
            m2 = i
    print(m2)
SecLar()
        
