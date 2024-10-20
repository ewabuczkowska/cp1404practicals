"""
CP1404 - Practical 5 - 4. emails
Estimate: 40 minutes
Actual:   50 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        expected_name = extract_name_from_email(email)
        name_confirmation = input(f"Is your name {expected_name}? (Y/n) ")

        if name_confirmation.lower() == "y" or name_confirmation == "":
            email_to_name[email] = expected_name
        else:
            expected_name = input("Name: ")
            email_to_name[email] = expected_name

        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extract name from email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    expected_name = " ".join(parts).title()
    return expected_name


main()
