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
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename to save projects to: ")
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%y").date()
            filtered_projects = [project for project in projects if project.start_date > date]
            for project in sorted(filtered_projects, key=lambda x: x.start_date):
                print(project)
        elif choice == "A":
            print("Let's add a new project")
            name = input("Name: ")
            date_string = input("Start date (dd/mm/yy): ")
            start_date = datetime.datetime.strptime(date_string, "%d/%m/%y").date()
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost estimate: $"))
            completion = int(input("Percent complete: "))
            projects.append(Project(name, start_date, priority, cost_estimate, completion))
        elif choice == "U":
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




if __name__ == '__main__':
    main()