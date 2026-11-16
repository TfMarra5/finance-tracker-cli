import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

try:
    with open("transaction.json", "r") as file:
        transaction = json.load(file)
except FileNotFoundError:
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

        # add list in memory
        transaction.append(new_transaction)
        print("✔ Transaction added successfully!\n")

        # save in file json
        with open("transaction.json", "w") as file:
                json.dump(transaction, file, indent=4)

    elif option == "2":
        if len(transaction) == 0:
            print("\nNo transactions registered yet.\n")
        else:

            # Table creation
            table = Table(title="Transaction History", show_header=True, header_style="bold magenta")

            # Column def
            table.add_column("Description", style="white")
            table.add_column("Amount", justify="right", style="green")
            table.add_column("Category", style="cyan")

            # Row -> transaction
            for t in transaction:
                table.add_row(t["description"], f"${t['amount']:.2f}", t["category"])

            # Table print
            console.print(table)

    elif option == "3":
        total = 0
        for t in transaction:
            total += t["amount"]

            console.print(Panel(f"[bold green]Total: ${total:.2f}[/bold green]", title="[bold]Funds Summary[/bold]", expand=False))
            console.print()
    elif option == "4":
        break

    else:
        print("Invalid option, please select between 1 and 4.\n")
