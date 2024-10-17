"""
CP1404 - Practical 4 - 2. Total Income
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    total = calculate_total(incomes)
    print_report(incomes, number_of_months)


def calculate_total(incomes):
    """Calculate the total income."""
    return sum(incomes)


def print_report(incomes, total):
    """Print the income report."""
    print("\nIncome Report\n-------------")
    cumulative_total = 0
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        cumulative_total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, cumulative_total))


main()
