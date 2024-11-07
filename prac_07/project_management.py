"""
CP1404 - Practical 07 - 4. Project Management Program
Estimated: 1h
Actual:
"""

import datetime

from prac_07.project import Project

# Constants
FILENAME = "projects.txt"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """Main program for project management."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    choice = input(f"{MENU}\n>>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename to save projects to: ")
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        choice = input(f"{MENU}\n>>> ").upper()

    save = input("Would you like to save to projects.txt? ")
    if save.lower().startswith('y'):
        save_projects(projects, FILENAME)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from file."""
    projects = []
    with open(filename) as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(projects, filename):
    """Save projects to file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t"
                      f"{project.start_date.strftime('%d/%m/%Y')}\t"
                      f"{project.priority}\t"
                      f"{project.cost_estimate}\t"
                      f"{project.completion_percentage}\n")


def display_projects(projects):
    """Display projects sorted by priority."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]

    print("Incomplete projects: ")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(f"  {project}")
    print("Completed projects: ")
    for project in sorted(completed_projects, key=lambda x: x.priority):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Display projects after a specified date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%y").date()
    filtered_projects = [project for project in projects if project.start_date >= date]
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(project)


def add_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    # Convert 2-digit year to 4-digit year for consistency
    date = datetime.datetime.strptime(date_string, "%d/%m/%y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    project = Project(name, date, priority, cost_estimate, completion)
    projects.append(project)


def update_project(projects):
    """Update a project's completion percentage and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    new_percentage = input("New Percentage: ")
    if new_percentage:
        projects[project_choice].completion_percentage = int(new_percentage)
    new_priority = input("New Priority: ")
    if new_priority:
        projects[project_choice].priority = int(new_priority)


if __name__ == '__main__':
    main()
