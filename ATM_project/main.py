from atm_package.account import ATMAccount
from atm_package.validator import check_pin


def show_menu():
    print("\n" + "=" * 35)
    print("         WELCOME TO ATM")
    print("=" * 35)
    print("1. Show Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")
    print("=" * 35)


if check_pin():
    user_account = ATMAccount()

    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            user_account.show_balance()

        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                user_account.deposit_money(amount)
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                user_account.withdraw_money(amount)
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "4":
            user_account.show_transactions()

        elif choice == "5":
            print("\nThank you for using our ATM.")
            print("Visit Again!")
            break

        else:
            print("Invalid option! Please select correctly.")