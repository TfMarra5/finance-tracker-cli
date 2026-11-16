transaction = []
list = []
funds = []

while True:
    print ("1- Add transaction\n2- List transactions\n3- Funds\n4- Exit\n")
    option = (input("Choose an option: \n"))
    if option == 1:
        print("This is your transaction", transaction)
    elif option == 2:
            print("This is your transaction", list)
    elif option == 3:
                print("This is your transaction", funds)
    elif option == 4:
        print("This is your transaction", transaction)
        break
    else:
        print("Invalid option, please select between 1 and 4.\n")
