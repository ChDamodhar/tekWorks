def std():
    sno,name=map(str,input("Enter student number and name").split())
    marks=[95,99,76]
    total=0
    for i in marks:
        total+=i
    av=total/3
    print("total marks and average of student",sno,name,"is\n",total,"\n",av)
    if(av < 40):
        print("Student filed")
    else:
        if(av < 50 and av >40):
            print("C grade")
        elif(av <70 and av >50):
            print("B grade")
        elif(av < 80 and av > 70):
            print("A grade")
        else:
            print("Distension")
std()
