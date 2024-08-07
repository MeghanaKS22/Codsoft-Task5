import json

# File to store contacts
CONTACTS_FILE = 'contacts.json'


def load_contacts():
    """Load contacts from a file."""
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def save_contacts(contacts):
    """Save contacts to a file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter the contact's name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter the contact's phone number: ").strip()
    email = input("Enter the contact's email: ").strip()
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print("Contact added successfully.")


def view_contacts(contacts):
    """View the contact list."""
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")


def search_contact(contacts):
    """Search for a contact by name."""
    name = input("Enter the contact's name to search: ").strip()
    contact = contacts.get(name)
    if contact:
        print(f"\nName: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print("Contact not found.")


def update_contact(contacts):
    """Update an existing contact."""
    name = input("Enter the contact's name to update: ").strip()
    contact = contacts.get(name)
    if not contact:
        print("Contact not found.")
        return
    phone = input("Enter the new phone number (leave blank to keep current): ").strip()
    email = input("Enter the new email (leave blank to keep current): ").strip()
    if phone:
        contact['phone'] = phone
    if email:
        contact['email'] = email
    contacts[name] = contact
    save_contacts(contacts)
    print("Contact updated successfully.")


def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the contact's name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def main():
    """Main function to run the contact book."""
    contacts = load_contacts()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
