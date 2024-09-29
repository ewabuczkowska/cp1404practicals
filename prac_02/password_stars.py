""" Password Stars """
MINIMUM_PASSWORD_LENGTH = 8
password = input("Enter a password: ")
while len(password) < MINIMUM_PASSWORD_LENGTH:
    print(f"Password must be at least {MINIMUM_PASSWORD_LENGTH} characters long.")
    password = input("Enter a password: ")
print("*" * len(password))