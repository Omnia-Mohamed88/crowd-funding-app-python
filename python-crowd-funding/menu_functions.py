# menu_functions.py

from crowdfunding_app import CrowdFundingApp

def display_menu():
    print("\nMenu:")
    print("1. Register")
    print("2. Login")
    print("3. Create Project")
    print("4. Edit Project")
    print("5. Delete Project")
    print("6. View Projects")
    print("7. Exit")

def main_menu(app):
    username = None

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            app.register_user()
        elif choice == "2":
            username = app.login_user()
        elif choice == "3":
            app.create_project(username)
        elif choice == "4":
            app.edit_project(username)
        elif choice == "5":
            app.delete_project(username)
        elif choice == "6":
            app.view_projects(username)
        elif choice == "7":
            app.save_data()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
