# Pharmacy Management System

A small command-line program in Python for a hospital pharmacy. You enter your patient ID, see what medicines are in stock, ask for as many pieces as you need, and look back at what you've been given before. Everything is saved in text files, so nothing is lost when you close it.

## What it can do

- Asks for your patient ID when it starts (like `P101`)
- Shows the medicines that are in stock, with how many pieces are left
- Lets you request a medicine by its ID and pick how many pieces you want
- Says "out of stock" when a medicine has run out, and tells you how many are left if you ask for too many
- Shows the total pieces of each medicine you've been given
- Shows your full history with the date and time
- Makes `medicines.txt` and `history.txt` by itself the first time you run it

## Files

```
pharmacy_system/
├── main.py         # the menu and user input
├── pharmacy.py     # Pharmacy class - stock and issuing medicines
├── patient.py      # Patient class - request, view medicines, view history
├── storage.py      # reads and writes the text files
├── medicines.txt   # medicine list with stock
└── history.txt     # record of everything issued
```

## How to run

You need Python 3.6 or newer. Nothing else to install.

```
python main.py
```

On Mac/Linux use `python3 main.py`.

## The menu

```
===== PHARMACY MENU =====
1. Display available medicines
2. Request a medicine
3. View my medicines
4. View my medicine history
5. Exit
```

Example:

```
Enter choice: 2
Enter medicine ID to request: 105
How many pieces do you want? 5
5 x Azithromycin 500mg issued to P101 (24 left)
```

## The text files

**medicines.txt** - one medicine per line: `ID|Name|Stock`

```
105|Azithromycin 500mg|30
```

**history.txt** - one issue per line: `Time|PatientID|MedicineID|MedicineName|Quantity`

```
2026-09-29 18:26:09|P101|105|Azithromycin 500mg|5
```

Lines starting with `#` are comments and the program ignores them. Don't put a `|` inside a name, because that's what the program splits each line on.

## Changing things

- **Add a medicine:** add a new line to `medicines.txt` with a new ID and a stock number
- **Restock:** change the stock number in `medicines.txt`
- **Different starting stock:** edit `DEFAULT_MEDICINES` in `storage.py` (only used if `medicines.txt` is missing)

## Ideas for later

- A pharmacist menu to restock and add or remove medicines
- A way to return a medicine
- Search by medicine name
- Use SQLite instead of text files
