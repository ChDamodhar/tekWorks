from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def list_books():
    response = supabase.table("books").select("*").execute()
    print("\nAll Books:")
    for book in response.data:
        print(f"ID: {book['book_id']}, Title: {book['title']}, Author: {book['author']}, "
              f"Category: {book['category']}, Stock: {book['stock']}")

def search_books():
    keyword = input("Enter keyword to search books (title/author/category): ").strip()
    response_title = supabase.table("books").select("*").ilike("title", f"%{keyword}%").execute()
    response_author = supabase.table("books").select("*").ilike("author", f"%{keyword}%").execute()
    response_category = supabase.table("books").select("*").ilike("category", f"%{keyword}%").execute()
    books = {b['book_id']: b for b in response_title.data + response_author.data + response_category.data}
    print(f"\nSearch Results for '{keyword}':")
    if books:
        for book in books.values():
            print(f"ID: {book['book_id']}, Title: {book['title']}, Author: {book['author']}, "
                  f"Category: {book['category']}, Stock: {book['stock']}")
    else:
        print("No books found.")

def member_details():
    member_id = int(input("Enter member ID to see borrowed books: ").strip())
    response_member = supabase.table("members").select("*").eq("member_id", member_id).execute()
    if not response_member.data:
        print(" Member not found.")
        return
    member = response_member.data[0]
    print(f"\nMember: {member['name']}, Email: {member['email']}, Joined: {member['join_date']}")
    response_borrow = supabase.table("borrow_records").select(
        "borrow_date, return_date, books(title, author, category)"
    ).eq("member_id", member_id).execute()
    if response_borrow.data:
        print("Borrowed Books:")
        for br in response_borrow.data:
            book = br['books']
            print(f"  - {book['title']} by {book['author']} (Category: {book['category']}) "
                  f"Borrowed: {br['borrow_date']}, Returned: {br['return_date']}")
    else:
        print("No borrowed books.")

def main():
    while True:
        print("\nOnline Library - Read Operations")
        print("1. List all books")
        print("2. Search books by title/author/category")
        print("3. Show member details and borrowed books")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            list_books()
        elif choice == "2":
            search_books()
        elif choice == "3":
            member_details()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()