# storage.py - reading and writing the text files
#
# medicines.txt  ->  ID|Name|Stock
# history.txt    ->  Time|PatientID|MedicineID|MedicineName|Quantity

import os

# only used if medicines.txt is missing (first run)
# id: (name, stock)
DEFAULT_MEDICINES = {
    '101': ('Paracetamol 500mg', 50),
    '102': ('Amoxicillin 250mg', 40),
    '103': ('Ibuprofen 400mg', 40),
    '104': ('Cetirizine 10mg', 40),
    '105': ('Azithromycin 500mg', 30),
    '106': ('Metformin 500mg', 40),
    '107': ('Omeprazole 20mg', 40),
    '108': ('Pantoprazole 40mg', 40),
    '109': ('ORS Sachet', 60),
    '110': ('Cough Syrup 100ml', 25),
    '111': ('Vitamin C 500mg', 60),
    '112': ('Insulin Pen', 15),
}


MEDICINES_HEADER = '''# Medicine list - one medicine per line
# format: ID|Name|Stock
# stock is how many pieces are left. change it here to restock.
'''

HISTORY_HEADER = '''# History of every medicine issued - newest at the bottom
# format: Time|PatientID|MedicineID|MedicineName|Quantity
# 'N/A' as the time means it was issued before history was added
'''


def save_medicines(filename, medicines):
    # write everything back to the file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(MEDICINES_HEADER)
        for med_id, info in medicines.items():
            f.write(f"{med_id}|{info['name']}|{info['stock']}\n")


def load_medicines(filename):
    # if there is no file yet, make one from the defaults
    if not os.path.exists(filename):
        medicines = {}
        for med_id, (name, stock) in DEFAULT_MEDICINES.items():
            medicines[med_id] = {'name': name, 'stock': stock}
        save_medicines(filename, medicines)
        return medicines

    medicines = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line == '' or line.startswith('#'):
                continue  # ignore empty lines and comments
            med_id, name, stock = line.split('|')
            medicines[med_id] = {'name': name, 'stock': int(stock)}
    return medicines


def append_history(filename, time, patient_id, med_id, med_name, quantity):
    # just add one line at the bottom (with the header if the file is new)
    is_new = not os.path.exists(filename)
    with open(filename, 'a', encoding='utf-8') as f:
        if is_new:
            f.write(HISTORY_HEADER)
        f.write(f"{time}|{patient_id}|{med_id}|{med_name}|{quantity}\n")


def load_history(filename):
    records = []
    if not os.path.exists(filename):
        return records  # no history yet

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line == '' or line.startswith('#'):
                continue
            time, patient_id, med_id, name, quantity = line.split('|')
            records.append({
                'time': time,
                'patient': patient_id,
                'med_id': med_id,
                'name': name,
                'quantity': int(quantity),
            })
    return records
