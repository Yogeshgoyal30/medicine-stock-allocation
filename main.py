# main.py - run this file to start the pharmacy program
#
# medicines.txt - medicine list (ID|Name|Stock)
# history.txt   - record of everything issued
# storage.py    - loads/saves the files
# pharmacy.py   - Pharmacy class (stock and issuing)
# patient.py    - Patient class (what the user can do)

import os

from pharmacy import Pharmacy
from patient import Patient

# files are kept next to main.py so it works from any folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDICINES_FILE = os.path.join(BASE_DIR, 'medicines.txt')
HISTORY_FILE = os.path.join(BASE_DIR, 'history.txt')

MENU = '''
===== PHARMACY MENU =====
1. Display available medicines
2. Request a medicine
3. View my medicines
4. View my medicine history
5. Exit
'''


def ask_patient_id():
    # keep asking until we get a proper ID
    # no blanks and no '|' because that is what we split the file on
    while True:
        patient_id = input('Enter your patient ID: ').strip().upper()
        if patient_id != '' and '|' not in patient_id:
            return patient_id
        print("Invalid ID. It can't be blank or contain '|'.")


def ask_quantity():
    text = input('How many pieces do you want? ').strip()
    if not text.isdigit():
        print('Please enter a whole number.')
        return None
    return int(text)


def main():
    print('----Pharmacy Management System----')
    pharmacy = Pharmacy(MEDICINES_FILE, HISTORY_FILE)
    patient = Patient(ask_patient_id(), pharmacy)

    while True:
        print(MENU)
        choice = input('Enter choice: ').strip()

        if choice == '1':
            pharmacy.show_available()

        elif choice == '2':
            med_id = input('Enter medicine ID to request: ').strip()
            if med_id not in pharmacy.medicines:
                print('No medicine found with that ID.')
                continue
            quantity = ask_quantity()
            if quantity is not None:
                patient.request_medicine(med_id, quantity)

        elif choice == '3':
            patient.view_medicines()

        elif choice == '4':
            patient.view_history()

        elif choice == '5':
            print('Goodbye, get well soon!')
            break

        else:
            print('Invalid choice, enter a number from 1 to 5.')


if __name__ == '__main__':
    main()
