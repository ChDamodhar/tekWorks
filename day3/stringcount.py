def StringCount(str):
    c1,c2,c3=0,0,0
    for i in str:
        if (i.isalpha()):
            c1+=1
        elif (i.isdigit()):
            c2+=1
        else:
            c3+=1
    print("No of alphabet are:",c1,"No of digits are:",c2,"No of special characters are:",c3)
StringCount("Damodhar@123")
