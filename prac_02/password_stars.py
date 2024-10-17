""" Password Stars """
MINIMUM_PASSWORD_LENGTH = 8


def main():
    password = get_password()
    print_asteriks(password)


def get_password():
    password = input("Enter a password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print(f"Password must be at least {MINIMUM_PASSWORD_LENGTH} characters long.")
        password = input("Enter a password: ")
    return password


def print_asteriks(password):
    print("*" * len(password))


main()
