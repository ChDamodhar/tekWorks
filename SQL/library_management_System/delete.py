from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def delete_member():
    member_id = int(input("Enter member ID to delete: ").strip())
    borrowed = supabase.table("borrow_records").select("*").eq("member_id", member_id).execute()
    if borrowed.data:
        print(" Cannot delete member. They have borrowed books.")
    else:
        response = supabase.table("members").delete().eq("member_id", member_id).execute()
        if response.data:
            print(" Member deleted:", response.data)
        else:
            print(" Member not found.")

def delete_book():
    book_id = int(input("Enter book ID to delete: ").strip())
    borrowed = supabase.table("borrow_records").select("*").eq("book_id", book_id).execute()
    if borrowed.data:
        print(" Cannot delete book. It is currently borrowed.")
    else:
        response = supabase.table("books").delete().eq("book_id", book_id).execute()
        if response.data:
            print(" Book deleted:", response.data)
        else:
            print(" Book not found.")

def main():
    while True:
        print("\n Online Library - Delete Operations")
        print("1. Delete Member")
        print("2. Delete Book")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            delete_member()
        elif choice == "2":
            delete_book()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()