import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Welcome to the Random Password Generator!")
    while True:
        print("\nMenu:")
        print("1. Generate Password")
        print("2. Quit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Password length must be greater than zero.")
            else:
                password = generate_password(length)
                print("Generated Password:", password)
        elif choice == '2':
            print("Thank you for using the Random Password Generator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
