# 📑 Is project mein aap use karenge:

# 🎯Features:         |  📚 Concepts: 
# 1.🔐 PIN Check      |   while loop
# 2.💰Balance Check    |   if-else
# 3.💵Deposit          |   functions
# 4.💸Withdraw         |   variables
# 5.🚪Exit             |       


# --------------------------
# 🏧 ATM Machine
# --------------------------

# --------------------------
# ➕ Add  feature Function
# --------------------------

pin = 13456
Balance = 1000

# --------------------------
#  🔐 Add pin check Function
# --------------------------

def pin_check():
    user_pin = int(input("Enter your pin :",))
    if user_pin == pin :
        print("pin Correct.")
    else :
        print("wrong pin.")



# --------------------------
# 💰 Add balance check Function
# --------------------------

def Balance_check():
    print("Current Balance:",Balance)


# --------------------------
# 💵 Add Deposit Function
# --------------------------

def Deposit():
    global Balance
    user_amount = int(input("Enter your deposit amount :" ,))
    Balance = Balance + user_amount
    print("Current Balance:", Balance)
    print("Deposit Successful!")


# --------------------------
# 💸 Add Withdraw Function
# --------------------------

def  withdraw():
    global Balance
    user_amount = int(input("Enter withdraw amount :" ,))
    if user_amount <= Balance :
        Balance = Balance - user_amount
        print("Current Balance:", Balance)
        print("Withdraw Successful!")
    else:
        print("Insufficient Balance!")


# ==========================================
# 🏠 Main Menu
# ==========================================

while True:
    print("1. pin check ")
    print("2. balance_check")
    print("3. deposit")
    print("4. withdraw")
    print("5. Exit")
    choice = input("enter your choice :" ,)


    if choice == "1":
        pin_check()
    elif choice == "2":
        Balance_check()
    elif choice == "3":
        Deposit()
    elif choice == "4":
        withdraw()
    elif choice == "5":
        print("Exiting your program ...")

        break

    else:
        print("invalid choice. please try again.")