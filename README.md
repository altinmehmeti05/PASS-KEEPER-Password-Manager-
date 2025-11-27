# 🔐 Password Manager (SQLite + Encryption)

A simple and secure **Password Manager** written in Python.  
It stores your passwords in an **encrypted SQLite database**, using **Fernet (AES-based encryption)**, and includes features like exporting/importing the database, platform management, and email association.

---

## 🚀 Features

- 🗄 **SQLite Database Storage**  
  All data is saved in a local SQLite database (`passwords.db`).

- 🔒 **Strong Encryption (Fernet / AES-128)**  
  Passwords are encrypted before being stored.  
  A secret key is automatically generated and saved as `secret.key`.

- ➕ **Add Platform Passwords**
- 🔍 **View Decrypted Passwords**
- ✏️ **Change Existing Passwords**
- ❌ **Delete Passwords**
- 📜 **List All Saved Platforms**
- 📤 **Export Database** (Backup)
- 📥 **Import Database** (Restore)

---

## 📦 Requirements

Install the required dependency:

  pip install cryptography

No other libraries are required.
SQLite is built into Python by default.

▶️ How to Run
python password_manager.py


When launched, a menu will appear:

1. Add a password
2. View password
3. Change password
4. Delete password
5. List platforms
6. Export database
7. Import database
8. Exit

🔑 Encryption Details

Uses Fernet encryption from the cryptography library.

A secret encryption key is automatically created on first run:

secret.key


Never delete this key unless you want to lose access to all stored passwords.

If you move the database to another computer, you must also move the key.

🗄 Database Files
File	Description
passwords.db	Encrypted SQLite database holding all entries
secret.key	The encryption key required to decrypt passwords
backup.db	Optional exported backup file
🔁 Export / Import
Export database (backup)

Creates a copy of your encrypted database.

6 → Export database

Import database (restore)

Replaces your current database with a backup file.

7 → Import database


⚠ Warning: Importing will overwrite your current passwords.db.

🛡 Security Notes

Passwords are always stored encrypted.

Exported databases remain encrypted.

Protect your secret.key — anyone with this key and the DB can decrypt all passwords.

Never upload the key publicly.

📌 Disclaimer

This is a lightweight educational password manager.
For professional, large-scale, or cloud-sensitive purposes, consider a battle-tested password manager like:

Bitwarden

KeePass

1Password
