# pharmacy.py - the Pharmacy class (stock + issuing medicines)

from datetime import datetime

from storage import load_medicines, save_medicines, load_history, append_history


class Pharmacy:
    def __init__(self, filename, history_filename):
        self.filename = filename
        self.history_filename = history_filename
        self.medicines = load_medicines(filename)

    def show_available(self):
        print('Available medicines:')
        print('================================================')
        found = False
        for med_id, info in self.medicines.items():
            if info['stock'] > 0:
                print(f"{med_id}  -  {info['name']}  ({info['stock']} in stock)")
                found = True
        if not found:
            print('Nothing is available right now.')

    def issue_medicine(self, med_id, patient_id, quantity):
        # returns True if the medicine was issued, False if not
        if med_id not in self.medicines:
            print('No medicine found with that ID.')
            return False

        if quantity < 1:
            print('Quantity must be at least 1.')
            return False

        medicine = self.medicines[med_id]

        if medicine['stock'] == 0:
            print('Sorry, this medicine is out of stock.')
            return False

        if quantity > medicine['stock']:
            print(f"Sorry, only {medicine['stock']} piece(s) of {medicine['name']} left.")
            return False

        # all good - take it out of stock and save
        medicine['stock'] -= quantity
        save_medicines(self.filename, self.medicines)

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        append_history(self.history_filename, now, patient_id,
                       med_id, medicine['name'], quantity)

        print(f"{quantity} x {medicine['name']} issued to {patient_id} "
              f"({medicine['stock']} left)")
        return True

    def history_of(self, patient_id):
        # all records that belong to this patient
        mine = []
        for record in load_history(self.history_filename):
            if record['patient'] == patient_id:
                mine.append(record)
        return mine

    def medicines_of(self, patient_id):
        # adds up how many pieces of each medicine the patient has got
        totals = {}
        for record in self.history_of(patient_id):
            med_id = record['med_id']
            totals[med_id] = totals.get(med_id, 0) + record['quantity']
        return totals
