"""
CP1404 - Practical 07 - 4. Project Management Program
Estimated: 1h
Actual:
"""

import datetime

from prac_07.project import Project


def main():
    """Main program for project management"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")

    MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

    choice = input(f"{MENU}\n>>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects_from_user()
        elif choice == "S":
            save_projects_to_file(projects)
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
        save_projects(projects, "projects.txt")
    print("Thank you for using custom-built project management software")

def load_projects(filename):
    """Load projects from file"""
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
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects

def save_projects(projects, filename):
    """Save projects to file"""
    with open(filename, 'w') as file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=file)
        for project in projects:
            print(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
                file=file)


def display_projects(projects):
    """Display projects sorted by priority"""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]

    print("Incomplete projects: ")
    for project in sorted(incomplete_projects):
        print(f"  {project}")
    print("Completed projects: ")
    for project in sorted(completed_projects):
        print(f"  {project}")


if __name__ == '__main__':
    main()