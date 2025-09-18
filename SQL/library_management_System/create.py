from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def add_member():
    name = input("Enter member name: ").strip()
    email = input("Enter member email: ").strip()
    response = supabase.table("members").insert({"name": name, "email": email}).execute()
    print("Inserted Member:", response.data)

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    category = input("Enter category: ").strip()
    stock = int(input("Enter stock quantity: ").strip())
    response = supabase.table("books").insert({
        "title": title,
        "author": author,
        "category": category,
        "stock": stock
    }).execute()
    print("Inserted Book:", response.data)

def main():
    while True:
        print("\n Online Library - Insert Operations")
        print("1. Add New Member")
        print("2. Add New Book")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_member()
        elif choice == "2":
            add_book()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()