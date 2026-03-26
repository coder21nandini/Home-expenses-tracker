import os

FILENAME = "expenses.txt"

# ------------------ Login ------------------
def login():
    print("==== Home Expenses Management ====")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "202403103510122" and password == "User21":
        print("Login successful!\n")
        menu()
    else:
        print("Invalid credentials. Try again.\n")
        login()

# ------------------ Menu ------------------
def menu():
    while True:
        print("\n==== Main Menu ====")
        print("1. Add Expense/Income")
        print("2. View Transactions & Summary")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            update_transaction()
        elif choice == "4":
            delete_transaction()
        elif choice == "5":
            print("Logged out.\n")
            break
        else:
            print("Invalid choice. Try again.")

# ------------------ Add ------------------
def add_transaction():
    date = input("Enter date (YYYY-MM-DD): ")
    trans_type = input("Enter type (d for Debit / c for Credit): ").lower()
    if trans_type not in ['d', 'c']:
        print("Invalid type. Use 'd' or 'c'.")
        return

    amount = input("Enter amount: ")
    category = input("Enter category: ")
    note = input("Enter note (optional): ")

    with open(FILENAME, "a") as file:
        file.write(f"{date},{trans_type},{amount},{category},{note}\n")
    
    print("Transaction added!")

# ------------------ View with Summary ------------------
def view_transactions():
    print("\n==== Transactions List ====")
    if not os.path.exists(FILENAME):
        print("No transactions found.")
        return

    total_debit = 0
    total_credit = 0

    with open(FILENAME, "r") as file:
        lines = file.readlines()

    if not lines:
        print("No transactions found.")
        return

    for idx, line in enumerate(lines):
        date, trans_type, amount, category, note = line.strip().split(",")
        amount = float(amount)
        if trans_type == "d":
            total_debit += amount
            t_type = "Debit"
        else:
            total_credit += amount
            t_type = "Credit"

        print(f"{idx + 1}. {t_type} | Date: {date}, Amount: {amount}, Category: {category}, Note: {note}")

    balance = total_credit - total_debit

    print("\n==== Summary ====")
    print(f"Total Debits : {total_debit}")
    print(f"Total Credits: {total_credit}")
    print(f"Balance      : {balance}")

# ------------------ Update ------------------
def update_transaction():
    view_transactions()
    line_num = int(input("\nEnter transaction number to update: ")) - 1

    with open(FILENAME, "r") as file:
        lines = file.readlines()

    if 0 <= line_num < len(lines):
        date = input("Enter new date (YYYY-MM-DD): ")
        trans_type = input("Enter new type (d/c): ").lower()
        amount = input("Enter new amount: ")
        category = input("Enter new category: ")
        note = input("Enter new note: ")

        lines[line_num] = f"{date},{trans_type},{amount},{category},{note}\n"

        with open(FILENAME, "w") as file:
            file.writelines(lines)

        print("Transaction updated.")
    else:
        print("Invalid number.")

# ------------------ Delete ------------------
def delete_transaction():
    view_transactions()
    line_num = int(input("\nEnter transaction number to delete: ")) - 1

    with open(FILENAME, "r") as file:
        lines = file.readlines()

    if 0 <= line_num < len(lines):
        del lines[line_num]
        with open(FILENAME, "w") as file:
            file.writelines(lines)
        print("Transaction deleted.")
    else:
        print("Invalid number.")

# ------------------ Start ------------------
login()