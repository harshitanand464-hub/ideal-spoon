import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harshit@123",
    database="contact_book"
)

cursor = db.cursor()

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    query = "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, phone, email))
    db.commit()
    print(" Contact Added Successfully")

def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    records = cursor.fetchall()

    if records:
        print("\nID | Name | Phone | Email")
        print("-" * 40)
        for row in records:
            print(row[0], "|", row[1], "|", row[2], "|", row[3])
    else:
        print("❌ No contacts found")

def update_contact():
    cid = input("Enter Contact ID to Update: ")
    name = input("Enter New Name: ")
    phone = input("Enter New Phone: ")
    email = input("Enter New Email: ")

    query = """
    UPDATE contacts 
    SET name=%s, phone=%s, email=%s 
    WHERE id=%s
    """
    cursor.execute(query, (name, phone, email, cid))
    db.commit()

    if cursor.rowcount > 0:
        print("✅ Contact Updated Successfully")
    else:
        print("❌ Contact Not Found")

def delete_contact():
    cid = input("Enter Contact ID to Delete: ")
    query = "DELETE FROM contacts WHERE id=%s"
    cursor.execute(query, (cid,))
    db.commit()

    if cursor.rowcount > 0:
        print(" Contact Deleted Successfully")
    else:
        print(" Contact Not Found")

def main():
    while True:
        print("\n--- CONTACT BOOK MENU ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print(" Exiting Contact Book")
            break
        else:
            print(" Invalid choice")

main()
