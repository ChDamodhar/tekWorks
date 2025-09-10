def length(str1,str2):
    c1,c2=0,0
    for i in str1:
        c1+=1
    for i in str2:
        c2+=1
    print("Length of str1 and str2 is :",c1,c2)
    print(str1==str2)
    print(str1+str2)
length("damodhar","Bharath")