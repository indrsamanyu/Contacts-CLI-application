import json
from contact import Contact

class ContactBook:
    def __init__(self):
        self.contacts = []
        self.filename = 'contacts.json'

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.contacts = [Contact(**contact_data) for contact_data in data]
        except FileNotFoundError:
            pass
    
    def save_contacts(self):
        data_to_save = [contact.to_dict() for contact in self.contacts]
        with open(self.filename, 'w') as f:
            json.dump(data_to_save, f, indent=4)

    def add_contacts(self, contact: Contact):
        self.contacts.append(contact)
        self.save_contacts()

    def view_contact(self):
        if not self.contacts:
            print("The Contact book is empty.")
        else:
            print("---- Your Contacts ----")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact}")
            print("--------------------")

    def search_contact(self, name_query: str) -> list:
        results = []
        for contact in self.contacts:
            if name_query.lower() in contact.name.lower():
                results.append(contact)
        return results
    
    def delete_contact(self, identifier: str | int) -> bool:
        contact_to_delete =  None
        if isinstance(identifier, int):
            index = identifier - 1
            if 0 <= index < len(self.contacts):
                contact_to_delete = self.contacts[index]
        elif isinstance(identifier, str):
            for contact in self.contacts:
                if contact.name.lower() == identifier.lower():
                    contact_to_delete = contact
                    break
        
        if contact_to_delete :
            self.contacts.remove(contact_to_delete)
            self.save_contacts()
            return True
        return False
    
    def update_contact(self, identifier: str | int, new_phone: str, new_email: str) -> bool:
        contact_to_update = None
        if isinstance(identifier, int):
            index = identifier - 1
            if 0 <= index < len(self.contacts):
                contact_to_update = self.contacts[index]
        elif isinstance(identifier, str):
            for contact in self.contacts:
                if contact.name.lower() == identifier.lower():
                    contact_to_update = contact
                    break
        if contact_to_update:
            if new_phone:
                contact_to_update.phone = new_phone
            if new_email:
                contact_to_update.email = new_email

            self.save_contacts()
            return True
        
        return False