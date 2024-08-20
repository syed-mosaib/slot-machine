MAX_LINES = 3

def deposit():
    lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?")")
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount
deposit()

def get_number_of_lines():


def main():
    balance = deposit()
