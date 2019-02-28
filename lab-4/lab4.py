# BANKKONTO
import datetime


# Account
class Account:
    """
    Attributes:
    name: Name of the person
    money: Amount of money on the account
    pin_code: The pin code needed to access the account
    transactions: List of the latest 10 transactions
    """

    def __init__(self, name, money, pin_code):
        """
        Creates a new account
        :param name: The name of the person
        :param money: The amount of money on the account
        :param pin_code: The pin code needed to access the acount
        """
        self.name = name
        self.money = int(money)
        self.pin_code = int(pin_code)
        self.transactions = []

    def __str__(self):
        """
        The Account information in a
        nice readable format for printouts
        :return: A nice string consisting of name, money and the transaction history of the account
        """
        printout = "Name: " + self.name + "\nMoney: " + str(self.money) + "\nTransaction history: \n" + "\n".join(
            self.transactions) + "\n"
        return printout

    def deposit(self, amount):
        """
        Used to add money to the account. Also updates the
        transaction history.
        :param amount: the amount of money to deposit
        :return: a string confirming the deposit.
        """
        self.money += amount
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S: ")
        self.transactions.append(date + str(amount) + " deposited.")
        if len(self.transactions) > 10:
            self.transactions = self.transactions.pop(0)
        return str(amount) + " successfully deposited."

    def withdrawal(self, amount, pin):
        """
        Used to withdraw money from the account, and update the transaction history.
        :param amount: the amount of money to withdraw
        :param pin: pin code for the account
        :return: a string confirming the withdrawal, or notifying the user if the pin is wrong, or if the account lacks funds.
        """
        if (amount > self.money):
            return "The account lacks the funds to withdraw " + str(amount)
        if (not self.ok_PIN(pin)):
            return "The pin entered is incorrect."
        else:
            self.money -= amount
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S: ")
            self.transactions.append(date + str(amount) + " withdrawn.")
            if len(self.transactions) > 10:
                self.transactions = self.transactions.pop(0)
            return str(amount) + " successfully withdrawn."

    def ok_PIN(self, pin):
        """
        Used to check if pin is correct
        :param pin: the pin code needed to access the account
        :return: Boolean value, returns True if the pin code is correct, False otherwise
        """
        return pin == self.pin_code

    def change_PIN(self, old_pin, new_pin):
        """
        Used to change pin code
        :param old_pin: the old pin code
        :param new_pin: the desired new pin code
        :return: a string confirming a successful change, or notifying the user that the old pin was incorrect.
        """
        if (old_pin == self.pin_code):
            self.pin_code = new_pin
            return "Pin code successfully changed to " + "*" * len(new_pin)
        else:
            return "Old pin is incorrect"


class PremiumAccount(Account):
    def withdrawal(self, amount, pin):
        """
        Used to withdraw money from the account, and update the transaction history.
        :param amount: the amount of money to withdraw
        :param pin: pin code for the account
        :return: a string confirming the withdrawal, or notifying the user if the pin is wrong, or if the account lacks funds.
        """
        if (amount > self.money):
            return "May I suggest a small loan of a MILLION DOLLARS SIR?"
        else:
            return Account.withdrawal(self,amount, pin)


def get_int_input(prompt_string):
    """
    Used to get an int from the user, asks again if the input is in an invalid format.
    :param prompt_string: the string explaining what to enter
    :return: the int that was asked for
    """
    while "Pigs" != "Fly":
        try:
            int_number = int(input(prompt_string))
        except ValueError:
            print("That is not a number! Try again.")
            continue
        else:
            break

    return int_number


def display_accounts(accounts):
    """
    Used to display all accounts and their info
    (Only for debugging purposes)
    :param accounts: a dictionary containing all accounts
    :return: (nothing)
    """

    for account in accounts.values():
        print(str(account))


def menu():
    """
    Used to display the menu:
        What would you like to do?
        1 - Set up a new account
        2 - Deposit
        3 - Withdrawal
        4 - Change pin
        5 - Display earlier transactions
        6 - Exit
    :return: (nothing)
    """
    print("What would you like to do?")
    print("1 - Set up a new account")
    print("2 - Deposit")
    print("3 - Withdrawal")
    print("4 - Change pin")
    print("5 - Display earlier transactions")
    print("6 - Exit")


def menu_choice():
    """
    Used to get input in what the user wants to do
    :return: an int, the chosen menu option
    """
    choice = get_int_input("Enter your choice: ")
    while (choice < 1) or (choice > 6):
        print("Enter a number between 1 and 6")
        choice = get_int_input("Enter your choice: ")

    return choice


# Execute functions
account_dict = {"Bullman": Account("Bullman", 500, 5555),
                "Herman": Account("Herman", 200, 1234),
                "Snusmumriken": Account("Snusmumriken", 9999, 6666),
                "Douglas": PremiumAccount("Douglas", 1000, 1234)}


def account_exists(account_name):
    return account_name in account_dict


def new_account():
    name = input("What is your name? ")
    money = get_int_input("How much money do you have? ")
    pin = get_int_input("Which pin code do you want? ")

    account_dict[name] = Account(name, money, pin)


def deposit():
    name = input("Which account? (name) ")
    if account_exists(name):
        amount = get_int_input("Amount: ")
        print(account_dict[name].deposit(amount))
    else:
        print("No such account exists.")


def withdraw():
    name = input("Which account do you want to withdraw from? (name) ")

    if not account_exists(name):
        print("No such account exists")
        return

    pin = get_int_input("What's the pin code for the given account? ")
    if not account_dict[name].ok_PIN(pin):
        print("The supplied pin is incorrect.")
    else:
        amount = get_int_input("How much do you want to withdraw?")
        print(account_dict[name].withdrawal(amount, pin))


def change_pin():
    name = input("Which account do you want to change the pin of? (name) ")
    if not account_exists(name):
        print("No such account exists.")
    else:
        old_pin = get_int_input("Enter your old pin: ")
        new_pin = get_int_input("Enter your new pin: ")
        print(account_dict[name].change_PIN(old_pin, new_pin))


def show_transactions():
    name = input("What account? (name) ")
    if not account_exists(name):
        print("No such account exists.")
    else:
        account = account_dict[name]
        pin = get_int_input("Enter your pin: ")
        if account.ok_PIN(pin):
            print(str(account))


def execute(choice):
    """
    Used to execute the option that the user chose
    :param choice: an int corresponding to the chosen option
    :return (nothing)
    """

    if choice == 1:
        new_account()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        change_pin()
    elif choice == 5:
        show_transactions()


def main():

    while "pigs" != "fly":
        menu()
        choice = menu_choice()
        if choice == 6:
            break
        elif choice < 1 or choice > 6:
            print("Not a valid choice.")
        else:
            execute(choice)


if __name__ == "__main__":
    main()
