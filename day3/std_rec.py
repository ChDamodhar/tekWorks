students=[(1,"damodhar",99),(2,"Bharath",96),(3,"Ashwith",69),(4,"Raj",75),(5,"anvesh",66)]
def topper(students):
    top=students[0]
    for i in students:
        if i[2]>top[2]:
            top=i
    return top[1]

def above75(students):
    l=[]
    for i in students:
        if i[2]>75:
            l.append(i)
    for i in l:
        print(i[1])

print("Topper is:",topper(students))
print("above 75 is :")
above75(students)





