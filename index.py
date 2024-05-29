import time

def check_balance():
    global balance
    print("Your Current Balance is: $", balance)
    forward(pin)

def deposit():
    global balance
    damount = int(input("Enter your Deposit amount: "))
    balance += damount
    print("Successfully Deposited")
    forward(pin)

def withdraw():
    global balance
    amount = int(input("Enter the Withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print("Transaction Successful")
        print("Current balance left is: $", balance)
        forward(pin)
    else:
        print("Insufficient Balance")
        forward(pin)

def details():
    global pin
    confirm_pin = int(input("Enter Your Pin: "))
    if pin == confirm_pin:
        print("Card Details:\n")
        print("Name: Marcellino Jefferson")
        print("Card Number: 1234 5678 9101 1121")
        print("Date of Expiration: 09/26")
        print("CVC: 929")
        forward(pin)
    else:
        details()

def pin_reset():
    global pin
    yn = input("Are you sure you want to reset your Pin? (y/n)")
    if yn.lower() == "y":
        confirm_pin = int(input("Enter Your Pin: "))
        if pin == confirm_pin:
            new_pin = int(input("Enter new Pin: "))
            pin = new_pin
            print("Pin successfully changed")
            forward(pin)
        else:
            print("Incorrect PIN.")
            forward(pin)
    else:
        print("Incorrect current PIN. Pin reset failed.")
        time.sleep(1)
        menu()

def forward(pin):
    yesno = input(str("Do you want to continue? (y/n)"))
    if yesno.lower() == "y":
        menu(pin)
    elif yesno.lower() == "n":
        print("Thank you for using ABC ATM")
        time.sleep(3)

def menu(pin):
    print("Enter 1 for Balance Check")
    print("Enter 2 for Money Withdrawal")
    print("Enter 3 for Money Deposit")
    print("Enter 4 for Account Details")
    print("Enter 5 for PIN Reset")

    option = int(input("Select an option (1/2/3/4/5): "))

    if option == 1:
        check_balance()
    elif option == 2:
        withdraw()
    elif option == 3:
        deposit()
    elif option == 4:
        details()
    elif option == 5:
        pin_reset()
    else:
        print("Invalid Option")
        menu(pin)

def main():
    global balance
    global pin
    pin = 1234
    balance = 1000000

    confirm_pin = int(input("Welcome to ABC ATM, Please insert your Pin: "))
    if pin == confirm_pin:
        menu(pin)
    else:
        print("Incorrect PIN.")

if __name__ == "__main__":
    main()