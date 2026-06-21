import json
from datetime import datetime
from tabulate import tabulate
from machine import Machine
import logging
from paths import ALLOWED_VALUES_FILE, INSTANCES_FILE


def load_allowed_values() -> dict:
    logging.info("Loading allowed values from configuration file.")

    with open(ALLOWED_VALUES_FILE, "r") as file:
        return json.load(file)
    
def ask_user_choice(question: str, options: list) -> str:
    string_options = [str(option) for option in options]
    while True:
        print(question)
        print("Options: " + ", ".join(string_options))
        answer = input("Your choice: ")
        if answer in string_options:
            return answer
        print("Invalid entry: " + answer + ". Please select an option from the list.")

def machine_name_is_available(name: str) -> bool:
    machines = load_machines()

    for machine in machines:
        if machine["name"].lower() == name.lower() and machine["status"] == "active":
            return False
    
    return True

def get_machine_details_from_user() -> Machine:
    logging.info("Starting to collect machine requirements.")

    allowed_values = load_allowed_values()

    while True:
        name = input("Please enter machine name: ")

        if machine_name_is_available(name):
            break

        print("An active machine with this name already exists.")
        logging.warning("Duplicate machine name detected: " + name)

    os_type = ask_user_choice(
        "Choose an OS type:",
        allowed_values["os_types"]
    )

    cpu = ask_user_choice(
        "How many CPU cores should the machine have?",
        allowed_values["cpu_options"]
    )

    ram = ask_user_choice(
        "How much RAM should the machine have, in GB?",
        allowed_values["ram_options_gb"]
    )

    machine = Machine(name=name, os_type=os_type, cpu=cpu, ram=ram)

    logging.info("Machine requirements collected for: " + name)
    return machine

def load_machines() -> list:
    if not INSTANCES_FILE.exists(): #If file doesn't exist
        logging.info("Instances file does not exist. Starting with an empty list.")
        return []
    try:
        with open(INSTANCES_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError: # If file is empty or bad
        logging.warning("Instances file is empty or contains invalid JSON. Starting with an empty list.")
        return []

def create_machine():
    machines = load_machines()
    new_machine = get_machine_details_from_user()

    machines.append(new_machine.model_dump(mode="json"))

    write_machines_to_file(machines)
    message = "Machine " + new_machine.name + " created successfully."
    logging.info(message)
    print(message)

def write_machines_to_file(machines: list):
    with open(INSTANCES_FILE, "w") as file:
        json.dump(machines, file, indent=4)
    logging.info("Instances file updated successfully.")

def delete_machine():
    name = input("What is the name of the machine you would like to delete? ")
    machines = load_machines()
    deleted = False
    for machine in machines:
        if machine["name"].lower() == name.lower() and machine["status"] == "active":
            machine["status"] = "deleted"
            machine["date_deleted"] = datetime.now().isoformat() 
            deleted = True
            break
    if not deleted:
        message = "No active machine named " + name + " was found."
        logging.warning(message)
        print(message)
    else:
        write_machines_to_file(machines)
        message = "Deleted machine " + name
        logging.info(message)
        print(message)

def display_existing_machines(status: str | None = None):
    machines = load_machines()

    if status is not None:
        filtered_machines = []

        for machine in machines:
            if machine["status"] == status:
                filtered_machines.append(machine)
        machines = filtered_machines

    if len(machines) == 0:
        logging.info("No machines found to display")
        print("No machines found.")
        return

    print(tabulate(machines, headers="keys", tablefmt="grid"))

    if status is None:
        logging.info("Displayed all machines")
    else:
        logging.info("Displayed machines with status: " + status)