class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"{contact.name}: {contact.phone}")

    def search_contact(self, query):
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                print(f"Found: {contact.name}, {contact.phone}, {contact.email}, {contact.address}")

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_phone: contact.phone = new_phone
                if new_email: contact.email = new_email
                if new_address: contact.address = new_address
                print(f"Updated: {contact.name}")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

def main():
    contact_book = ContactBook()
    while True:
        print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            query = input("Search by name or phone: ")
            contact_book.search_contact(query)
        elif choice == '4':
            name = input("Contact name to update: ")
            new_phone = input("New phone (leave blank for no change): ")
            new_email = input("New email (leave blank for no change): ")
            new_address = input("New address (leave blank for no change): ")
            # contact_book.update_contact(name, new_phone, new)
            contact_book.update_contact(name, new_phone, new_email, new_address)
        elif choice == '5':
            name = input("Contact name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
                                        


