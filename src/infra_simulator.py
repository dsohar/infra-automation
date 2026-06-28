import logging
import machine_manager
from script_runner import run_install_script
from paths import LOG_FILE

LOG_FILE.parent.mkdir(exist_ok=True)
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

MENU = """
What would you like to do?
1. Create a machine
2. Delete a machine
3. Display all active machines
4. Display all machines
5. Run install script
6. Exit

"""
VALID_CHOICES = ["1", "2", "3", "4", "5", "6", "0"]

def main():
    logging.info("Started project run")

    print("Welcome to Daniel's CLI Project!!")
    while True: 
        while True:
            user_choice = input(MENU)
            if user_choice in VALID_CHOICES:
                break
            print("Invalid entry: " + user_choice + ". Please select an option from the menu.")
            logging.warning("Invalid menu option selected: " + user_choice)
        
        try:
            if user_choice == "1": # Create a machine
                logging.info("User selected: 1. Create a machine")
                machine_manager.create_machine()

            elif user_choice == "2": # Delete a machine
                logging.info("User selected: 2. Delete a machine")
                machine_manager.delete_machine()

            elif user_choice == "3": # Display all active machines
                logging.info("User selected: 3. Display all active machines")
                machine_manager.display_existing_machines("active")

            elif user_choice == "4": # Display all machines
                logging.info("User selected: 4. Display all machines")
                machine_manager.display_existing_machines()

            elif user_choice == "5": # Run install script
                logging.info("User selected: 5. Run install script")
                run_install_script()

            elif user_choice == "6": # Exit
                logging.info("User selected: 6. Exit")
                break

            elif user_choice == "0": # Easter Egg (Sorry, I couldn't help myself)
                logging.info("User Selected: 0. Easter Egg Found!!!")
                print("Remember, whenever you walk into a room and forget why you went there, \n"
                      "it's entirely possible you just encountered an alien who had to erase your memory.")
                input("\nPress Enter when your brain is done buffering :D")

        except Exception as e:
            logging.exception("Unexpected error")
            print("An error occurred: " + str(e))
    


if __name__ == "__main__":
    main()
