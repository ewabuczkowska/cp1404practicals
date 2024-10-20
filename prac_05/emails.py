"""
CP1404 - Practical 5 - 4. emails
Estimate: 40 minutes
Actual:   50 minutes

NOT WORKING, WHY????
"""


def main():
    """Docstring!"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        expected_name = extract_name_from_email(email)
        name_confirmation = input(f"Is your name {expected_name}? (Y/n) ")

        if name_confirmation.upper() == "y" or name_confirmation != "":
            email = input("Email: ")
        else:
            expected_name = input("Name: ")

        email_to_name[email] = expected_name
        email = input("Email: ")

    for email, expected_name in email_to_name.items():
        print(f"{expected_name} ({email})")


def extract_name_from_email(email):
    """Docstring!"""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    expected_name = " ".join(parts).title()
    return expected_name


main()
