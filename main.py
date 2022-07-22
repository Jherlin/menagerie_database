import time
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor = mydb.cursor()
mycursor.execute("USE bank")


def main():
    print('''
             _._._                       _._._
        _|   |_                     _|   |_
        | ... |_._._._._._._._._._._| ... |
        | ||| |  o NATIONAL BANK o  | ||| |
        | """ |  """    """    """  | """ |
   ())  |[-|-]| [-|-]  [-|-]  [-|-] |[-|-]|  ())
  (())) |     |---------------------|     | (()))
 (())())| """ |  """    """    """  | """ |(())())
 (()))()|[-|-]|  :::   .-"-.   :::  |[-|-]|(()))()
 ()))(()|     | |~|~|  |_|_|  |~|~| |     |()))(()
    ||  |_____|_|_|_|__|_|_|__|_|_|_|_____|  ||
 ~ ~^^ @@@@@@@@@@@@@@/=======\@@@@@@@@@@@@@@ ^^~ ~
      ^~^~                                ~^~^
    ''')

    print(f"Welcome to National Bank\n"
          f"\n1. Log in\n"
          f"2. Create an account\n")
    choice = int(input("Enter a selection: "))

    if choice == 1:
        login()
    elif choice == 2:
        create_account()


def main_menu(name):
    print(f"\nPlease Select a Transaction\n"
          f"\n1. Deposit Money\n"
          f"2. Withdraw Money\n"
          f"3. View Balance\n"
          f"4. End Transaction\n")
    while True:
        choice = int(input("Enter a selection: "))
        print("")

        if choice == 1:
            deposit(name)
        elif choice == 2:
            withdraw(name)
        elif choice == 3:
            view_balance(name)
        elif choice == 4:
            mycursor.close()
            print("\nThank you for banking with us.")
            break
        else:
            print("\nInvalid Input.")


def create_account():
    name = input("Enter your name: ").lower()
    pin = int(input("Enter a pin: "))

    sql = "INSERT INTO account_info (name, pin, balance) VALUES (%s,%s,%s)"
    val = [(name, pin, 0)]

    mycursor.executemany(sql, val)
    mydb.commit()

    login()


def login():
    while True:
        print("\nAccount Login")
        name = input("Enter your name: ").lower()
        pin = int(input("Enter your pin: "))
        print("")

        mycursor.execute(f"SELECT * FROM account_info WHERE name ='{name}'")
        account_data = mycursor.fetchall()
        try:
            if pin == account_data[0][1]:
                loading()
                print("You are logged in.")
                main_menu(name)
                break
            else:
                loading()
                print("Invalid pin. Try again.\n")
        except IndexError:
            print("Invalid pin. Try again.\n")


def deposit(name):
    amount = float(input("Enter deposit amount: "))

    mycursor.execute(f"SELECT * FROM account_info WHERE name ='{name}'")
    account_data = mycursor.fetchall()
    balance = account_data[0][2]
    amount = balance + amount
    sql = f"UPDATE account_info SET balance='{amount}' WHERE name='{name}'"

    mycursor.execute(sql)
    mydb.commit()

    view_balance(name)


def withdraw(name):
    amount = float(input("Enter withdrawal amount: "))
    print("")

    mycursor.execute(f"SELECT * FROM account_info WHERE name ='{name}'")
    account_data = mycursor.fetchall()
    balance = account_data[0][2]
    amount = balance - amount
    sql = f"UPDATE account_info SET balance='{amount}' WHERE name='{name}'"

    mycursor.execute(sql)
    mydb.commit()

    view_balance(name)


def view_balance(name):
    mycursor.execute(f"SELECT * FROM account_info WHERE name ='{name}'")
    account_data = mycursor.fetchall()
    balance = account_data[0][2]
    print(f"Account balance is ${balance:,.2f}")


def loading():
    print("*", end=" ")
    time.sleep(1)
    print("*", end=" ")
    time.sleep(1)
    print("*", end=" ")


main()
