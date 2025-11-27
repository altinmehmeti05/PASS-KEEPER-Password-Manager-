import sqlite3
import shutil
from cryptography.fernet import Fernet

print("--------------------------------------------------------")
print("|                    ~PΛƧƧ KΣΣPΣЯ~                     |")
print("--------------------------------------------------------")
#                                               Altin Mehmeti

class PasswordManager:
    def __init__(self):
        # Load or create encryption key
        try:
            with open("secret.key", "rb") as key_file:
                self.key = key_file.read()
        except FileNotFoundError:
            self.key = Fernet.generate_key()
            with open("secret.key", "wb") as key_file:
                key_file.write(self.key)

        self.fernet = Fernet(self.key)

        # Connect to SQLite
        self.conn = sqlite3.connect("passwords.db")
        self.cursor = self.conn.cursor()

        # Create table if not exists
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS passwords (
                platform TEXT PRIMARY KEY,
                password BLOB,
                email TEXT
            )
        """)
        self.conn.commit()

    # ------------------------------------------
    # Encryption / Decryption
    # ------------------------------------------

    def encrypt(self, text: str) -> bytes:
        return self.fernet.encrypt(text.encode())

    def decrypt(self, encrypted_text: bytes) -> str:
        return self.fernet.decrypt(encrypted_text).decode()

    # ------------------------------------------
    # CRUD OPERATIONS
    # ------------------------------------------

    def add_password(self, platform, password, email=None):
        encrypted_pw = self.encrypt(password)

        try:
            self.cursor.execute(
                "INSERT INTO passwords (platform, password, email) VALUES (?, ?, ?)",
                (platform, encrypted_pw, email)
            )
            self.conn.commit()
            print(f"Password for {platform} saved successfully.")
        except sqlite3.IntegrityError:
            print(f"Password for {platform} already exists.")

    def view_password(self, platform):
        self.cursor.execute("SELECT password, email FROM passwords WHERE platform = ?", (platform,))
        result = self.cursor.fetchone()

        if result:
            encrypted_pw, email = result
            decrypted_pw = self.decrypt(encrypted_pw)
            print(f"Password for {platform}: {decrypted_pw}")
            print(f"Email: {email if email else 'No email saved'}")
        else:
            print("Platform not found.")

    def change_password(self, platform, new_password):
        encrypted_pw = self.encrypt(new_password)

        self.cursor.execute("UPDATE passwords SET password = ? WHERE platform = ?", (encrypted_pw, platform))
        if self.cursor.rowcount == 0:
            print("Platform not found.")
        else:
            print("Password updated.")
            self.conn.commit()
#                                                                      /Daddy/
    def delete_password(self, platform):
        self.cursor.execute("DELETE FROM passwords WHERE platform = ?", (platform,))
        if self.cursor.rowcount == 0:
            print("Platform not found.")
        else:
            print("Password deleted.")
            self.conn.commit()

    def list_platforms(self):
        self.cursor.execute("SELECT platform FROM passwords")
        platforms = self.cursor.fetchall()

        if not platforms:
            print("No saved platforms.")
        else:
            print("Saved platforms:")
            for (platform,) in platforms:
                print(platform)

    # ------------------------------------------
    # EXPORT / IMPORT
    # ------------------------------------------

    def export_database(self, backup_name="backup.db"):
        try:
            shutil.copyfile("passwords.db", backup_name)
            print(f"Database exported successfully as {backup_name}")
        except FileNotFoundError:
            print("No database found to export.")

    def import_database(self, backup_name="backup.db"):
        try:
            shutil.copyfile(backup_name, "passwords.db")
            print(f"Database imported successfully from {backup_name}")
        except FileNotFoundError:
            print(f"Backup file '{backup_name}' not found.")


# ---------------------------------------------------
#                       MENU
# ---------------------------------------------------

password_manager = PasswordManager()


while True:
    print("\nChoose an action:")
    print("1. Add a password")
    print("2. View password")
    print("3. Change password")
    print("4. Delete password")
    print("5. List platforms")
    print("6. Export database")
    print("7. Import database")
    print("8. Exit")

    choice = input("Your choice: ")

    if choice == '1':
        platform = input("Platform name: ")
        password = input("Password: ")
        email = input("Email (optional): ").strip()
        email = email if email else None
        password_manager.add_password(platform, password, email)

    elif choice == '2':
        platform = input("Platform name: ")
        password_manager.view_password(platform)

    elif choice == '3':
        platform = input("Platform name: ")
        new_password = input("New password: ")
        password_manager.change_password(platform, new_password)

    elif choice == '4':
        platform = input("Platform name: ")
        password_manager.delete_password(platform)

    elif choice == '5':
        password_manager.list_platforms()

    elif choice == '6':
        filename = input("Backup filename (default: backup.db): ").strip() or "backup.db"
        password_manager.export_database(filename)

    elif choice == '7':
        filename = input("Backup file to import: ").strip()
        password_manager.import_database(filename)

    elif choice == '8':
        print("--------------------------------------------------------")
        print("|                      ~𝓖𝓸𝓸𝓭 𝓑𝔂𝓮~                      |")
        print("--------------------------------------------------------")
        break

    else:
        print("Invalid choice.")
