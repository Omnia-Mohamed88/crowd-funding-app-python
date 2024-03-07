import json
from models import User, Project
from datetime import datetime

class CrowdFundingApp:
    def __init__(self):
        self.users = {}
        self.projects = {}
        self.load_data()

    def load_data(self):
        try:
            with open('users.json', 'r') as user_file:
                user_data = json.load(user_file)
                self.users = user_data.get('users', {})
        except FileNotFoundError:
            pass

        try:
            with open('projects.json', 'r') as project_file:
                project_data = json.load(project_file)
                self.projects = project_data.get('projects', {})
        except FileNotFoundError:
            pass

    def save_data(self):
        user_data = {"users": {}}
        for email, user_info in self.users.items():
            user_data["users"][email] = vars(user_info["user"])
            user_data["users"][email]["projects"] = user_info["projects"]

        project_data = {"projects": {}}
        for title, project in self.projects.items():
            if isinstance(project, dict):  
                project_data["projects"][title] = project
            else:
                project_data["projects"][title] = vars(project)

        with open('users.json', 'w') as user_file:
            json.dump(user_data, user_file, indent=2)

        with open('projects.json', 'w') as project_file:
            json.dump(project_data, project_file, indent=2)

        print("Data saved.")


    def validate_registration(self, first_name, last_name, email, password, mobile):
        if not first_name.isalpha():
            print("First name should contain only alphabetical characters.")
            return False

        if not last_name.isalpha():
            print("Last name should contain only alphabetical characters.")
            return False

        if "@" not in email or "." not in email:
            print("Invalid email address.")
            return False

        if len(password) < 6:
            print("Password should be at least 6 characters.")
            return False

        if not mobile.startswith('+2') or not mobile[2:].isdigit() or not (len(mobile) == 13):
            print("Invalid Egyptian mobile number.")
            return False

        return True

   


    def validate_project_creation(self, title, details, total_target, start_time, end_time):
        if not title:
            print("Project title cannot be empty.")
            return False

        if not details:
            print("Project details cannot be empty.")
            return False

        if not total_target.isdigit():
            print("Invalid total target amount.")
            return False

        try:
            datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
            datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD HH:MM:SS.")
            return False

        return True

    def register_user(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        mobile = input("Enter your mobile number: ")

        if self.validate_registration(first_name, last_name, email, password, mobile):
            user = User(first_name, last_name, email, password, mobile)
            self.users[email] = {"user": user, "projects": []}

            print("Registration successful!")
            self.save_data()

    def create_project(self, email):
        if email:
            title = input("Enter project title: ")
            details = input("Enter project details: ")
            total_target = input("Enter total target amount: ")
            start_time = input("Enter project start time (YYYY-MM-DD HH:MM:SS): ")
            end_time = input("Enter project end time (YYYY-MM-DD HH:MM:SS): ")

            if self.validate_project_creation(title, details, total_target, start_time, end_time):
                project = Project(title, details, float(total_target), start_time, end_time, email)
                self.projects[title] = project

                self.users[email]["projects"].append(title)

                print("Project created successfully!")
                self.save_data()
        else:
            print("You must log in before creating a project.")


    def login_user(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        user = self.users.get(username)

        if user and user["user"].password == password:
            print("Login successful!")
            return username
        else:
            print("Invalid username or password.")
            return None

    def edit_project(self, username):
        if username:
            project_name = input("Enter the project name you want to edit: ")

            if project_name in self.projects and project_name in self.users[username]["projects"]:
                new_description = input("Enter the new project description: ")
                self.projects[project_name].details = new_description
                print("Project edited successfully!")
                self.save_data()
            else:
                print("Project not found or you don't have permission to edit.")

    def delete_project(self, username):
        if username:
            project_name = input("Enter the project name you want to delete: ")

            if project_name in self.projects and project_name in self.users[username]["projects"]:
                del self.projects[project_name]

                self.users[username]["projects"].remove(project_name)

                print("Project deleted successfully!")
                self.save_data()
            else:
                print("Project not found or you don't have permission to delete.")

    def view_projects(self, username):
        if username:
            if self.users[username]["projects"]:
                print("Your Projects:")
                for project_name in self.users[username]["projects"]:
                    project = self.projects[project_name]
                    print(f"Name: {project.title}, Description: {project.details}")
            else:
                print("You have no projects.")
