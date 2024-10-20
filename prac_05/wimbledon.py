"""
CP1404 - Practical 5 - 6. Wimbledon
Estimate: 40 minutes
Actual:   1 hour 20 minutes

"""
FILENAME = "wimbledon.csv"


def main():
    records = read_data(FILENAME)
    champion_to_count, countries = process_records(records)  # Correct unpacking
    display_results(champion_to_count, countries)


def read_data(filename):
    """Read Wimbledon data from a CSV file and return a list of records."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Count champions and track countries from the records provided."""
    champion_to_count = {}
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            champion_to_count[record[2]] += 1
        except KeyError:
            champion_to_count[record[2]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display the results of the processed data."""
    print("Wimbledon Champions:")
    for name, count in champion_to_count.items():
        print(f"{name} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


main()
