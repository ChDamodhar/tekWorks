book={}
def add_dict(book,key,val):
    book[key]=val

def rem_dict(book,key):
    if key in book:
        book.remove(key)
    else:
        print("Book is not present")

def search(book,key):
    if key in book:
        print("book is present")
    else:
        print("not present")

def display(book):
    print(book)

def count(book):
    print("total no of books are:",len(book))

def lookup(book,value):
    if value in book.values():
        print("Book with title",value,"is present in library")
    else:
        print("not present")

print("Enter 1 for adding book")
print("Enter 2 for removing book")
print("Enter 3 for searching a book")
print("Enter 4 for display ")
print("Enter 5 for num of books")
print("Enter 6 for searching book by title")
print("Enetr 7 for exit")
while True:
    n=int(input("Enter choice:"))
    if(n==1):
        k=int(input("Enter book id:"))
        v=input("Enter title of book:")
        add_dict(book,k,v)
    elif(n==2):
        k=int(input("Enter book id:"))
        rem_dict(book,k)
    elif(n==3):
        k=int(input("Enter book id:"))
        search(book,k)
    elif(n==4):
        display(book)
    elif(n==5):
        count(book)
    elif(n==6):
        v=input("Enter title of book:")
        lookup(book,v)
    elif(n==7):
        break
    else:
        print("Invalid choice")

    