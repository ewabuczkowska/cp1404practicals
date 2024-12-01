"""
CP1404 Practical 4 - 3. Subject Reader
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    lists = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer
        lists.append(parts)  # Add the parts to the lists
    input_file.close()
    return lists


def display_subject_details(data):
    """Display subject details."""
    for subject in data:
        subject_code = subject[0]
        lecturer = subject[1]
        number_of_students = subject[2]
        print(f"{subject_code} is taught by {lecturer} and has {number_of_students} students")


main()
