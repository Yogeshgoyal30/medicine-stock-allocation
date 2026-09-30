# Medicine Stock Allocation and Pharmacy Management System

## Project Overview

The Medicine Stock Allocation and Pharmacy Management System is a simple Python-based command-line application designed to manage medicine stock and allocate medicines to patients.

The main idea behind the project is to make basic pharmacy stock management easier. Instead of maintaining everything manually, the system keeps track of available medicines, updates stock when a medicine is issued, and maintains a record of each patient's medicine history.

## Problem Statement

In a pharmacy, keeping track of medicine stock manually can become difficult. Staff may need to check how many medicines are available, make sure that a requested quantity is actually in stock, and maintain records of medicines given to different patients.

This project provides a simple digital solution for these tasks using Python and file-based storage.

## Objectives

* To manage medicine stock digitally.
* To allocate available medicines to patients.
* To prevent issuing more medicine than the available stock.
* To maintain a record of medicines issued to patients.
* To provide a simple and easy-to-use interface.
* To demonstrate the practical use of Python classes, functions, file handling and validation.

## Features

* Patient ID input
* Display available medicines
* Request medicines by medicine ID
* Quantity validation
* Out-of-stock checking
* Automatic stock reduction
* View medicines received by a patient
* View patient medicine history
* Automatic creation of medicine and history files
* Persistent storage using text files

## Functional Modules

### 1. Medicine Stock Management

The system reads medicine information from `medicines.txt` and displays medicines that are currently available.

### 2. Medicine Allocation

A patient can request a medicine by entering its ID and the required quantity. The system checks whether the requested quantity is available before issuing it.

### 3. Patient History

The system stores each successful medicine issue with the patient ID, medicine ID, medicine name, quantity and time. Patients can later view their medicine history.

## Technologies Used

* Python 3
* Python Classes and Objects
* Functions
* File Handling
* Text File Storage
* Git and GitHub

## Project Structure

```text
medicine-stock-allocation/
│
├── main.py
├── pharmacy.py
├── patient.py
├── storage.py
├── medicines.txt
├── history.txt
├── README.md
└── statement.md
```

### File Description

* `main.py` - Starts the application and handles the main menu.
* `pharmacy.py` - Handles medicine stock and medicine allocation.
* `patient.py` - Handles patient-related operations.
* `storage.py` - Reads and writes medicine and history data.
* `medicines.txt` - Stores medicine IDs, names and stock quantities.
* `history.txt` - Stores records of medicines issued.
* `statement.md` - Contains the project problem statement, scope and features.

## How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

### Step 2: Download or clone the repository

```bash
git clone https://github.com/Yogeshgoyal30/medicine-stock-allocation.git
```

### Step 3: Open the project folder

```bash
cd medicine-stock-allocation
```

### Step 4: Run the program

```bash
python main.py
```

No external Python libraries are required.

## How the System Works

1. The program starts and asks for a patient ID.
2. The patient can view the available medicines.
3. The patient selects a medicine using its ID.
4. The requested quantity is checked against the available stock.
5. If enough stock is available, the medicine is issued.
6. The stock quantity is automatically reduced.
7. The transaction is saved in the history file.
8. The patient can view their medicines and previous medicine history.

## Testing

The system was tested using different input situations, including:

* Valid patient ID
* Empty patient ID
* Valid medicine ID
* Invalid medicine ID
* Valid quantity
* Quantity greater than available stock
* Zero or invalid quantity
* Out-of-stock medicine
* Viewing history when no records are available
* Viewing history after successfully requesting a medicine

The system displays suitable messages for invalid inputs instead of stopping unexpectedly.

## Limitations

The current version is a command-line application and uses text files instead of a database. It does not include a separate pharmacist login or a graphical user interface.

## Future Enhancements

Some improvements that can be added in the future are:

* Pharmacist/admin login
* Add and remove medicines through the application
* Restocking through the application
* Search medicines by name
* Medicine return functionality
* SQLite or another database for storage
* Graphical user interface
* Better reporting and analytics

## Conclusion

This project demonstrates how basic Python programming concepts can be used to solve a practical inventory management problem. It combines classes, functions, file handling, validation and data processing to create a simple medicine allocation system.

The project can also be extended further into a larger pharmacy management application by adding a database, user roles and a graphical interface.
