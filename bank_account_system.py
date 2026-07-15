accounts = {
    "malak": {
        "password": "123456",
        "balance": 1000
    },
    "ahmed": {
        "password": "654321",
        "balance": 3000
    }
}


def main_menu():
    while True:
        print('========== Welcome To Python Bank ==========')
        print('1. Register')
        print('2. Login')
        print('3. Exit')
        choice = int(input(''))
        if choice == 1:
            register()
        elif choice == 2:
            login()
        else:
            break


def register():
    username = input('Username: ')
    while (username in accounts) or len(username) == 0:
        print('This username does exist')
        username = input('Enter a new username: ')

    password = input('Password: ')
    while len(password) < 6:
        print('The password must be at least 6 characters long.')
        password = input('Enter new password: ')

    accounts[username] = {
        'password': password,
        'balance': 0
    }
    print('Account created successfully.')
    return bank_menu(username)


def login():
    for i in range(3):
        username = input("Username: ")

        if username not in accounts:
            print("The username is wrong or doesn't exist.")
            continue

        password = input("Password: ")

        if password != accounts[username]["password"]:
            print("The password is wrong.")
            continue

        return bank_menu(username)

    print("You have exceeded the maximum number of login attempts." )

def bank_menu(username):
    print(f"Welcome to you account your balance = {accounts[username]['balance']}")
    while True:
        print('========== Bank Menu ==========')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Transfer')
        print('5. Change Password')
        print('6. Logout')
        choice = int(input(''))
        if choice == 1:
            check_balance(username)
        elif choice == 2:
            deposit(username)
        elif choice == 3:
            withdraw(username)
        elif choice == 4:
            transfer(username)
        elif choice == 5:
            change_password(username)
        else:
            break


def check_balance(username):
    print(accounts[username]['balance'])


def deposit(username):
    x = accounts[username]['balance']
    add = int(input('Enter the amount to add to the account: '))
    while add <= 0:
        print('The amount must be greater than zero. ')
        add = int(input('Enter the amount to add to the account: '))
    accounts[username]['balance'] = x + add
    print('the amount is deposited successfully')


def withdraw(username):
    x = accounts[username]['balance']
    withdrawn = int(input('Enter the amount to add to the account: '))
    while withdrawn <= 0:
        print('The amount must be greater than zero. ')
        withdrawn = int(input('Enter the amount to add to the account: '))
    while withdrawn > x:
        print('The balance must be sufficient.')
        withdrawn = int(input('Enter the amount to add to the account: '))
    accounts[username]['balance'] = x - withdrawn
    print('the amount is withdrawn successfully')


def transfer(username):
    reciptant = input('Enter the reciptant')
    while reciptant not in accounts:
        print("this user doesn't exist")
        reciptant = input('Enter existing reciptant: ')
    while username == reciptant:
        print("A transfer to the same account is not allowed. ")
        reciptant = input('Enter different reciptant: ')

    x = accounts[username]['balance']
    y = accounts[reciptant]['balance']
    transfer_amount = int(input('Enter the amount to transfer: '))
    while transfer_amount <= 0:
        print('The amount must be greater than zero. ')
        transfer_amount = int(input('Enter the amount to transfer: '))
    while transfer_amount > x:
        print('The balance must be sufficient.')
        transfer_amount = int(input('Enter the amount to transfer: '))

    accounts[username]['balance'] = x - transfer_amount
    accounts[reciptant]['balance'] = y + transfer_amount
    print('The transfer is succesful')
    print(f'You tranfared {x} from account {username} to {reciptant}')


def change_password(username):
    current = input('Enter your current password: ')
    while current != accounts[username]['password']:
        print('this password is wrong')
        current = input('Enter your current password: ')

    new = input('Enter your new password: ')
    while len(new) < 6:
        print('The password must be at least 6 characters long.')
        new = input('Enter new password: ')
    accounts[username]['password'] = new


main_menu()