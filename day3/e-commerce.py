l=[]
def add_item(item,l):
    l.append(item)
    
def rem_item(item,l):
    if item in l:
        l.remove(item)
    else:
        print("item not found")

def search_item(item,l):
    if item in l:
        print("item available in cart")
    else:
        print("item not found")

def display_cart(l):
    print(l)

def total_num(l):
    print("total number product in cart is:",len(l))

def cart_sort(l):
    l.sort()
    print("Cart is sorted")

def cart_clear(l):
    l.clear()
    print("Cart is cleared")

print("Enter 1 for adding item in cart:")
print("Enter 2 for remove item in cart:")
print("Enter 3 for searching item in cart:")
print("Enter 4 for display items in cart:")
print("Enter 5 for number of products in cart")
print("Enter 6 for sort of products in cart")
print("Enter 7 for clear all products in cart")
print("Enter 8 for exit:")

while True:
    n=int(input("Enter option:"))
    if(n==1):
        i=input("Enter item:")
        add_item(i,l)
    elif(n==2):
        i=input("Enter item:")
        rem_item(i,l)
    elif(n==3):
        i=input("Enter item:")
        search_item(i,l)
    elif(n==4):
        display_cart(l)
    elif(n==5):
        total_num(l)
    elif(n==6):
        cart_sort(l)
    elif(n==7):
        cart_clear(l)
    elif(n==8):
        break
    else:
        print("Invalid choice ,Try again")



