contacts = []
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print("Contact added successfully.")
def view_contact_list():
    if not contacts:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}")
def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            found_contacts.append(contact)
    if not found_contacts:
        print("No contacts found.")
    else:
        print("Found contacts:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
def update_contact():
    search_term = input("Enter name or phone number of the contact to update: ")
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            found_contacts.append(contact)
    if not found_contacts:
        print("Contact not found.")
    else:
        print("Select the contact to update:")
        for index, contact in enumerate(found_contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}")
        choice = int(input("Enter the number corresponding to the contact: ")) - 1
        field = input("Enter field to update (name/phone/email/address): ")
        new_value = input(f"Enter new {field}: ")
        found_contacts[choice][field] = new_value
        print("Contact updated successfully.")
def delete_contact():
    search_term = input("Enter name or phone number of the contact to delete: ")
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            found_contacts.append(contact)
    if not found_contacts:
        print("Contact not found.")
    else:
        print("Select the contact to delete:")
        for index, contact in enumerate(found_contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}")
        choice = int(input("Enter the number corresponding to the contact: ")) - 1
        del contacts[contacts.index(found_contacts[choice])]
        print("Contact deleted successfully.")
def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
