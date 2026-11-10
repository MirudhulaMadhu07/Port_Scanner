import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Enter a username: ")
    if username in password_manager:
        print("Username already exists. Please choose a different username.")
        return
    password = getpass.getpass("Enter a password: ")
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hash_password
    print("Account created successfully.")

def login():
    username = input("Enter your username: ")
    if username not in password_manager:
        print("Username does not exist. Please create an account first.")
        return
    password = getpass.getpass("Enter your password: ")
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    if password_manager[username] == hash_password:
        print("Login successful!")
    else:
        print("Incorrect password. Please try again.")

def main():
    while True:
        print("\nPassword Manager")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    