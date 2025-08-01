from contact import Contact
from contact_book import ContactBook

def print_menu():
    print('\n--- Contact Book Menu ---')
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Exit")
    print("-------------------------")

def is_valid_phone(phone_str: str) -> bool:
    allowed_chars = "+-() "
    for char in phone_str:
        if not char.isdigit() and char not in allowed_chars:
            return False
    return True

def main():
    contact_book = ContactBook()
    contact_book.load_contacts()
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            print('Enter new contact details: ')
            name = input(" Name: ")
            while True:
                phone = input(" Phone: ")
                if is_valid_phone(phone):
                    break
                else:
                    print(" Invalid phone number. Please use digits, spaces and the '+-()'.")

            while True:
                email = input(" Email: ")
                if '@' in email and '.' in email and email.find('@') < email.rfind('.'):
                    break
                else :
                    print("Invalid Email format. Please ensure it contains '@' and a '.' after the '@'.")

            new_contact = Contact(name=name, phone=phone, email=email)
            contact_book.add_contacts(new_contact)
            print("\nContact added successsfully!")

        elif choice == '2':
            print("All Contacts\n")
            contact_book.view_contact()

        elif choice == '3':
            print('Search\n')
            name_query = input()
            result = contact_book.search_contact(name_query)
            if not result:
                print(f"No contacts found matching '{name_query}")
            else :
                print("\n--- Search Results ---")
                for contact in result:
                    print(contact)
                print("-----------------------")

        elif choice == '4':
            identifier_str = input("Enter the name or index of the contact to update: ")
            print("Enter new details (keep blank space to keep current value): ")
            new_phone = input(" New Phone: ")
            new_email = input(" New Email: ")
            identifier = None
            try:
                identifier = int(identifier_str)
            except ValueError:
                identifier = identifier_str
            
            if contact_book.update_contact(identifier, new_phone, new_email):
                print("Contact updated successfully!")
            else:
                print(f"Error: Contact '{identifier_str}' not found.")

        elif choice == '5':
            identifier_str = input('Enter the name or index of the contact to delete: ')
            identifier = None
            try:
                identifier = int(identifier_str)
            except:
                identifier = identifier_str

            if contact_book.delete_contact(identifier):
                print("Contact deleted successfully!")
            else :
                print(f"Error: Contact '{identifier_str}' not found.")

        elif choice == '6':
            print('Goodbye!')
            break

        else:
            print('Invalid choice. Please enter a number between 1 and 6.')

if __name__ == "__main__":
    main()
