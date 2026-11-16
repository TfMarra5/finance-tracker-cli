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

        print(transaction)

    elif option == "3":
        print("This is your transaction", transaction)

    elif option == "4":
        print("This is your transaction", transaction)
        break

    else:
        print("Invalid option, please select between 1 and 4.\n")
