transaction = []

while True:
    print ("1- Add transaction\n2- List transactions\n3- Funds\n4- Exit\n")
    option = input("Choose an option: \n").strip()

    if option == "1":
        # user types the data
        description = input("Enter description: ")
        amount = float(input("Enter amount (e.g. 50.0): "))
        category = input("Enter category (e.g. Food, Salary): ")

        new_transaction = {
            "description": description,
            "amount": amount,
            "category": category
        }

        # save the list
        transaction.append(new_transaction)
        print("✔ Transaction added successfully!\n")

    elif option == "2":
        if len(transaction) == 0:
            print("\nNo transactions registered yet.\n")
        else:
            print("\n--- Transactions List ---")
            for t in transaction:
                print(f"• {t['description']} | ${t['amount']:.2f} | Category: {t['category']}")
            print("-------------------------\n")

    elif option == "3":
        total = 0
        for t in transaction:
            total += t["amount"]

        print("\n--- Total Funds ---")
        print(f"Total: ${total:.2f}")
        print("-------------------\n")

    elif option == "4":
        print("This is your transaction", transaction)
        break

    else:
        print("Invalid option, please select between 1 and 4.\n")
