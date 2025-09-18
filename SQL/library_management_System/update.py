from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def update_book_stock():
    book_id = int(input("Enter book ID to update stock: ").strip())
    new_stock = int(input("Enter new stock quantity: ").strip())
    response = supabase.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()
    if response.data:
        print(" Book stock updated:", response.data)
    else:
        print(" Book not found.")

def update_member_email():
    member_id = int(input("Enter member ID to update email: ").strip())
    new_email = input("Enter new email: ").strip()
    response = supabase.table("members").update({"email": new_email}).eq("member_id", member_id).execute()
    if response.data:
        print(" Member email updated:", response.data)
    else:
        print("Member not found.")

def main():
    while True:
        print("\n Online Library - Update Operations")
        print("1. Update book stock")
        print("2. Update member email")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            update_book_stock()
        elif choice == "2":
            update_member_email()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()