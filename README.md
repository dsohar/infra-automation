# Infrastructure Simulator

## Overview

Infrastructure Simulator is a Python command-line application that simulates the management of virtual machine instances.

The application allows users to:

* Create machine instances
* Delete machine instances
* Display active machine instances
* Display all machine instances
* Execute an installation script
* Record application activity in a log file

Machine definitions are stored in JSON format and include:

* Machine name
* Operating system
* CPU count
* RAM size
* Status
* Creation date
* Deletion date

---

## Requirements

### Python Version

This project was developed and tested using:

Python 3.14.4

Verify your Python version:

```bash
python3 --version
```

---

## Supported Operating Systems

The application can be executed on:

* Linux
* macOS
* Windows Subsystem for Linux (WSL)

Most application features work on any operating system supported by Python.

The **Run Install Script** feature requires Bash and therefore can only be executed from:

* Linux
* macOS
* WSL

Attempting to run the installation script from native Windows will result in an error.

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository_url>
cd infra-automation
```
<!-- TODO -->
Replace `<repository_url>` with the actual repository URL.

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

Linux / macOS / WSL:

```bash
source .venv/bin/activate
```
### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Required Python Packages

The project uses the following external packages:

```text
pydantic==2.13.4
tabulate==0.10.0
```

These packages will be installed automatically when running:

```bash
pip install -r requirements.txt
```

---

## Running the Application

From the project root directory:

```bash
python3 src/infra_simulator.py
```

---

## Available Menu Options

```text
1. Create a machine
2. Delete a machine
3. Display all active machines
4. Display all machines
5. Run install script
6. Exit
```

---

## Configuration File

### allowed_values.json

Contains the valid options available when creating machine instances.

---

## Data Storage

### instances.json

Stores all machine instances created by the application.

Deleted machines are not removed from the file. Instead, they are marked with:

```json
{
  "status": "deleted"
}
```

and a deletion timestamp is recorded.

If the file does not exist, it will be created automatically when the first machine is added.

---

## Logging

Application events are written to:

```text
logs/provisioning.log
```
The application automatically creates the log directory if it does not already exist.

---

## Notes

* Machine names must be unique among active machines.
* Deleted machine names may be reused.
* The installation script must exist in the `scripts` directory.
* The installation script feature requires Linux, macOS, or WSL.
* The project uses JSON files for persistence and does not require a database.

```
```
