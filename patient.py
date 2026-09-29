# patient.py - the Patient class


class Patient:
    def __init__(self, patient_id, pharmacy):
        self.patient_id = patient_id
        self.pharmacy = pharmacy

    def view_medicines(self):
        totals = self.pharmacy.medicines_of(self.patient_id)
        if not totals:
            print('No medicines issued to you.')
            return
        print('Your medicines:')
        for med_id, quantity in totals.items():
            name = self.pharmacy.medicines[med_id]['name']
            print(f"{med_id}  -  {name}  x {quantity}")

    def view_history(self):
        records = self.pharmacy.history_of(self.patient_id)
        if not records:
            print('No history yet.')
            return
        print('Your medicine history:')
        print('================================================')
        for r in records:
            print(f"{r['time']}  |  {r['med_id']}  -  {r['name']}  x {r['quantity']}")

    def request_medicine(self, med_id, quantity):
        return self.pharmacy.issue_medicine(med_id, self.patient_id, quantity)
