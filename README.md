📒 Contact Book – CLI Application
A simple command-line Contact Book application written in Python using Object-Oriented Programming (OOP) and JSON for persistent data storage.

✨ Features
📇 Add new contacts with name, phone, and email

📋 View all saved contacts

🔍 Search contacts by name

📝 Update contact details

❌ Delete contacts by name or index

💾 All data is saved locally in contacts.json

🧠 Technologies Used
Python 3

OOP (Object-Oriented Programming)

JSON (for file-based data storage)

📂 Project Structure
bash
Copy
Edit
.
├── main.py             # Main CLI interface
├── contact.py          # Contact class definition
├── contact_book.py     # Manages contacts (CRUD operations, file handling)
├── contacts.json       # Stores the saved contacts (auto-generated)
🚀 Getting Started
Prerequisites
Python 3.x installed on your system

Run the Application
bash
Copy
Edit
python main.py
Menu Options
pgsql
Copy
Edit
1. Add a new contact
2. View all contacts
3. Search for a contact
4. Update a contact
5. Delete a contact
6. Exit
✅ Input Validation
Phone numbers accept digits, spaces, and characters like +, -, (, )

Emails must contain @ and a . after @

💡 Example
sql
Copy
Edit
--- Contact Book Menu ---
1. Add a new contact
2. View all contacts
...
Enter your choice (1-6): 1
Enter new contact details:
 Name: Alice
 Phone: +1 (555) 123-4567
 Email: alice@example.com
Contact added successfully!
🗃️ Data Persistence
All contacts are saved to a contacts.json file in the project directory, so your data remains intact between sessions.

📜 License
This project is open source and available under the MIT License.

