# Infrastructure Simulator

## Overview

Infrastructure Simulator is a Python command-line application that simulates the management of virtual machine instances.

The application allows users to create, delete and display virtual machine definitions stored in JSON files. It also includes the ability to execute an installation script, providing a foundation for future infrastructure automation.

---

## Features

* Create virtual machine instances
* Delete existing machine instances
* Display active machine instances
* Display all machine instances
* Execute an installation script
* Log application activity and errors
* Store machine definitions in JSON format

---

## System Requirements

### Python

This project was developed and tested using **Python 3.14.4**.

Verify your Python version:

```bash
python3 --version
```

### Operating System

The application supports:

* Linux
* macOS
* Windows

**Note:** The **Run Install Script** option requires Bash and therefore only works on:

* Linux
* macOS
* Windows Subsystem for Linux (WSL)

All other application features work on native Windows.

---

## Installation

### 1. Clone the repository

```bash
git clone git@github.com:dsohar/infra-automation.git
cd infra-automation
```

### 2. Create a virtual environment

Linux / macOS / WSL

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

The project depends on:

* pydantic 2.13.4
* tabulate 0.10.0

---

## Project Structure

```text
infra-automation/
│
├── configs/
│   ├── allowed_values.json
│   └── instances.json
│
├── logs/
│   └── provisioning.log
│
├── scripts/
│   └── install.sh
│
├── src/
│   ├── infra_simulator.py
│   ├── machine.py
│   ├── machine_manager.py
│   ├── paths.py
│   └── script_runner.py
│
├── requirements.txt
└── README.md
```

### File Description

| File                    | Purpose                                                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **infra_simulator.py**  | Main application entry point. Displays the menu and handles user interaction.                                              |
| **machine.py**          | Defines the `Machine` data model using Pydantic.                                                                           |
| **machine_manager.py**  | Contains the business logic for creating, deleting and displaying machines.                                                |
| **script_runner.py**    | Executes the installation shell script and handles related validation.                                                     |
| **paths.py**            | Stores all project file and directory paths.                                                                               |
| **allowed_values.json** | Defines the valid operating systems, CPU options and RAM options available to users.                                       |
| **instances.json**      | Stores all machine instances created by the application. Deleted machines remain in the file with a status of `"deleted"`. |
| **install.sh**          | Sample shell script executed through the application.                                                                      |
| **requirements.txt**    | Lists the external Python packages required by the project.                                                                |
| **README.md**           | Project documentation and installation guide.                                                                              |
| **provisioning.log**          | Stores event logging for different events. The log file and directory are created automatically if they do not already exist.                                                        |

---

## Running the Application

From the project root directory:

```bash
python3 src/infra_simulator.py
```

---

## Menu Options

```
1. Create a machine
2. Delete a machine
3. Display all active machines
4. Display all machines
5. Run install script
6. Exit
```

(There may also be a small hidden easter egg.)

---

## Logging

The application writes log messages to:

```
logs/provisioning.log
```

The log file and directory are created automatically if they do not already exist.

Examples of logged events include:

* Application startup
* Machine creation
* Machine deletion
* Script execution
* Warnings
* Errors

---

## Notes

* Machine names must be unique among active machines. (Deleted machine names may be reused)
* Machine definitions are stored in JSON files.
* The installation script must exist in the `scripts` directory.
