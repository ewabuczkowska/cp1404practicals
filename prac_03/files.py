"""
CP1404 - Practical 3 - 7. Files
"""

# 1)
name = input("What is your name? ")
file = open('name.txt', 'w')
file.write(name)
file.close()

# 2)
file = open('name.txt', 'r')
name_from_file = file.readline().strip()
file.close()
print(f"Hi {name_from_file}!")

# 3)
with open('numbers.txt', 'r') as file:
    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())
    result = first_number + second_number
    print(result)

# 4)
with open('numbers.txt', 'r') as file:
    total = 0
    for line in file:  # Using for line in file to iterate through each line
        total += int(line.strip())  # Converting each line to int and adding to total
    print(total)