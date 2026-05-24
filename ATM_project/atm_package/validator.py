def check_pin():
    correct_pin = 1234
    attempts = 3

    print("=" * 35)
    print("         ATM LOGIN")
    print("=" * 35)

    while attempts > 0:
        try:
            entered_pin = int(input("Enter 4-digit ATM PIN: "))

            if entered_pin == correct_pin:
                print("Login Successful!")
                return True

            else:
                attempts -= 1
                print(f"Incorrect PIN! Attempts left: {attempts}")

        except ValueError:
            print("Please enter numbers only.")

    print("\nToo many incorrect attempts.")
    print("Account temporarily blocked.")
    return False