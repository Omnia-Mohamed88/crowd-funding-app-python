# main.py

from crowdfunding_app import CrowdFundingApp
from menu_functions import main_menu

def main():
    app = CrowdFundingApp()
    main_menu(app)

if __name__ == "__main__":
    main()
