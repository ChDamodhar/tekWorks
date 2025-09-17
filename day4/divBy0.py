a,b=map(int,input("Enter a and b").split())
try:
    print("Division of a and b",a/b)
except :
    print("zero division error")
else:
    print("Division is completed")
finally:
    print("program complete")
    