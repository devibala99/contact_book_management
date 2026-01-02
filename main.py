import json
import os

FILE_NAME = "contact.json"

#---------------LOAD CONTACTS---------------
def load_contacts():
    if not os.path.exists(FILE_NAME):
        return {}
    
    with open(FILE_NAME, "r") as file:
        return json.load(file)

#---------------SAVE CONTACTS---------------
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent = 4)

#---------------VALIDATION HELPERS---------------
def clean_phone(phone):
    phone = phone.strip().replace("-","").replace(" ","")
    if not phone.isdigit() or len(phone) != 10:
        raise ValueError("Phone must be 10 digits")
    return phone

def validate_email(email):
    email = email.strip().lower()
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format.")
    return email

def phone_exists(contacts, phone):
    return any(c["phone"] == phone for c in contacts.values())

def email_exists(contacts, email):
    return any(c["email"] == email for c in contacts.values())


# -------------------- ID GENERATION --------------------
def generate_contact_id(contacts):
    if not contacts:
        return "C001"
    numbers = [int(cid[1:]) for cid in contacts.keys()]
    return f"C{max(numbers) + 1:03d}"

# -------------------- CORE FEATURES --------------------

def add_contact():
    contacts = load_contacts()

    try:
        name = input("Enter name: ").strip()
        phone = clean_phone(input("Enter phone: "))
        email = validate_email(input("Enter email: "))

        if phone_exists(contacts, phone):
            print("❌ Phone already exists")
            return

        if email_exists(contacts, email):
            print("❌ Email already exists")
            return

        contact_id = generate_contact_id(contacts)

        contacts[contact_id] = {
            "name": name,
            "phone": phone,
            "email": email
        }

        save_contacts(contacts)
        print(f"✅ Contact added with ID {contact_id}")

    except ValueError as e:
        print("❌ Error:", e)

def search_contact():
    contacts = load_contacts()
    query = input("Enter name to search: ").strip().lower()

    found = False
    for cid, details in contacts.items():
        if query in details["name"].lower():
            print(cid, details)
            found = True

    if not found:
        print("No contact found")

def delete_contact():
    contacts = load_contacts()
    cid = input("Enter Contact ID to delete: ").strip()

    if cid in contacts:
        del contacts[cid]
        save_contacts(contacts)
        print("✅ Contact deleted")
    else:
        print("❌ Contact ID not found")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts available")
        return

    for cid, details in contacts.items():
        print(cid, details)

# -------------------- MENU --------------------

def menu():
    while True:
        print("\n📒 CONTACT BOOK")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            view_contacts()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

# -------------------- RUN --------------------
if __name__ == "__main__":
    menu()