def currentBill():
    cno,cname=map(str,input("Enter customer number and name").split())
    pmr,lmr=map(int,input("Enter present month and last month readings:").split())
    tu=pmr-lmr
    print(f'customerno:{cno} cname:{cname} pmr:{pmr} lmr:{lmr} totalunits:{tu}')
    if(tu<=50):
        cbill=tu*3.80
        print("current bill is:",cbill)
    elif(tu > 50 and tu <= 100):
        cbill=(50*3.80)+(tu-50)*4.20
        print("Current bill is:",cbill)
    elif(tu > 100 and tu <= 200):
        cbill=(50*3.80)+(50*4.20)+(tu-100)*5.10
        print("Current bill is:",cbill)
    elif(tu > 200 and tu <= 300):
        cbill=(50*3.80)+(50*4.20)+(100*5.10)+(tu-200)*6.30
        print("Current bill is:",cbill)
    else:
        cbill=(50*3.80)+(50*4.20)+(100*5.10)+(100*6.30)+(tu-300)*7.50
        print("Current bill is:",cbill)
currentBill()
    