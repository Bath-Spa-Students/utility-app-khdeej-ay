### ASSESSMENT 2: UTILITY APP 
### VENDING MACHINE

# import the datetime module (to get the prcise date&time for the receipt)
from datetime import datetime
# import the time module (to use the time.sleep function)
import time
# import the sys module (to use the sys.exit function)
import sys

# function to use the time.sleep function
def small_pause():
    time.sleep(0.5)     # 0.5-second break

# function to use the time.sleep function
def pause():
    time.sleep(1)    # 1-second break

# function to add a break between different selections
def separator():
    # a separating line made up of hyphens
    print("\n\t--------------------------------------------------------")

# function to print a styled box asking for user's preffered payment method
def payment_method():
    print("""
               ╔═══════════════════════════════════════╗
               ║        \033[1mCHOOSE A PAYMENT METHOD\033[0m        ║
               ╠═══════════════════════════════════════╣
               ║           CASH\033[3m[1]\033[0m | CARD\033[3m[2]\033[0m           ║
               ╚═══════════════════════════════════════╝""")
    pause()

# funtion to print a styled box asking user to choose a category
def category(): 
    print("""     
              ╔══════════════════════════════════════════╗
              ║          \033[1mCHOOSE A MENU CATEGORY\033[0m          ║
              ╠══════════════════════════════════════════╣
              ║  SNACKS\033[3m[1]\033[0m | BEVERAGES\033[3m[2]\033[0m | DESSERTS\033[3m[3]\033[0m  ║
              ╚══════════════════════════════════════════╝""")
    small_pause()     # 1-second break

# function to display the selected menu and it's items
def display_menu(menu_items, menu_type):   
    # print the formatted header of the menu selected with it's items and their details
    print(f"""
          ┌───────────────────────────────────────────────────┐
          │ \033[1;35m{menu_type.upper():^49}\033[0m │
          ├─────┬──────────────────────────┬──────────┬───────┤ 
          │ \033[0;38;2;0;255;128mNo.\033[0m │ \033[0;38;2;0;255;128mItem\033[0m                     │ \033[0;38;2;0;255;128mPrice\033[0m    │ \033[0;38;2;0;255;128mStock\033[0m │
          ├─────┼──────────────────────────┼──────────┼───────┤   """)
    # loops through a copy of menu_items to avoid modifying it directly during iteration
    for item in menu_items.copy():    
        # if the stock of each item is less than - is never less - or equal to zero 
        if item['stock'] <= 0:    
            # remove that item (with 0 stock)
            menu_items.remove(item)
        # whatever items have stock more than 0 will have their details printed in columns with proper spacing
        else:    
            print(f"\t  │ {item['code']}  │ {item['item']:<24} │ AED {item['price']:.2f} │ {item['stock']:^5} │")    
    print("\t  └─────┴──────────────────────────┴──────────┴───────┘")

# function to store user's selected menu category
def menu_choice():
    # set the selected category to global
    global menu_selected
    # loop begins (to ensure correct value is entered)
    while True: 
        # user is prompted to select category
        category = input("\n\t\t    \033[1;34mSELECT A CATEGORY ( EXIT[0] ):\033[0m ").strip()
        pause()       # 1-second break
        # if user enters 0
        if category == "0":   
            # program ends
            sys.exit()     
        # if user enters 1    
        elif category == "1":            
            # snacks menu is printed
            display_menu(snacks, "SNACKS")
            # menu_selected is set to snacks list
            menu_selected = snacks  
            # break out of while loop        
            break  
        # if user enters 2
        elif category == "2": 
            # beverages menu is printed
            display_menu(beverages, "BEVERAGES")
            # menu_selected is set to beverages list
            menu_selected = beverages
            # break out of while loop        
            break
        # if user enters 3
        elif category == "3": 
            # desserts menu is displayed
            display_menu(desserts, "DESSERTS")
            # menu_selected is set to desserts list
            menu_selected = desserts
            # break out of while loop        
            break
        # runs when invalid category is entered (not 1, 2 or 3)
        else: 
            print("\n\t\t  \033[0;31mIncorrect category. Please try again.\033[0m ")
            # loop starts again (asks user to select category again)
            continue

# function to print item dispensed message and add item to cart (for receipt)
def item_dispensed(cart, choice):
    # set item_selected to the chosen item
    item_selected = choice['item']
    # append the empty cart list to include the dict of the chosen item
    cart.append(choice)
    # stores the item dispensed message
    dispense = f"Your {item_selected} has/have been dispensed."
    # prints cyan-bold dispense message formatted to the center (using the center method)
    print(f'\n\t\033[1;36m{dispense.center(56)}\033[0m')    

# function to update the items stock when one is dispensed
def update_stock(menu_items, item_num):
    # for loop iterates through items in the selected menu 
    for item in menu_items:
        # select the item whose code the user has entered
        if item_num == str(item['code']):
            # deduct the stock for that specific item by 1 
            item['stock'] -= 1           
            # break out of the loop (once selected item stock is deducted)
            break

# function for personalised suggestions (depending on the item selected)
def suggestions(menu_selected): 
    # set item_selected to the chosen item 
    item_selected = choice['item']
    # set item_code to the code of the chosen item
    item_code = str(choice['code'] )
    # if the selected menu is snacks
    if menu_selected is snacks: 
        # match the item_code with the item selected by the user
        # gives personalised suggestions for each snack selected
        match item_code:
            case "11": 
                suggest = "Would you like a Hazelnut Chocolate"
            case "12": 
                suggest = "Would you like a Brown Sugar Milk Tea"
            case "13":
                suggest = "Would you like a Caramel Macchiato"
            case "14": 
                suggest = "Would you like some Takis Crisps"
            case "15":
                suggest = "Would you like a Peach Juice"
    # if the selected menu is beverages
    elif menu_selected is beverages:
        # match the item_code with the item selected by the user
        # gives personalised suggestions for each beverage selected
        match item_code:
            case "21":
                suggest = "Would you like some Takis Crisps"
            case "22":
                suggest = "Would you like some Caramel Popcorn"
            case "23":
                suggest = "Would you like a Caramel Fudge Brownie"
            case "24":
                suggest = "Would you like a Glazed Donut"
            case "25":
                suggest = "Would you like some Chunko's Cookies"
    # if the selected menu is desserts
    elif menu_selected is desserts: 
        # match the item_code with the item selected by the user
        # gives personalised suggestions for each beverage selected
        match item_code:
            case "31":
                suggest = "Would you like some Haribo Happy Cola Jelly"
            case "32":
                suggest = "Would you like a Caramel Macchiato"
            case "33":
                suggest = "Would you like a Brown Sugar Milk Tea"
            case "34":
                suggest = "Would you like some Takis Crisps"
            case "35":
                suggest = "Would you like some Chunko's Cookies"
    # prints yellow-italicized suggestion formatted to the center
    print(f'\n\t\033[3;33m{suggest.center(56)}\033[0m')
    another = f"with your {item_selected}?"
    print(f"\t\033[3;33m{another.center(56)}\033[0m")

# function to print the receipt for the purchase(s) and the transaction(s)
def invoice(cart, cash, change): 
    # current variable stores the datetime class
    current = datetime.now()
    # print formatted receipt 
    print("\n\t\t\t\t \033[1;36mRECEIPT\033[0m")
    # print("\t\t----------------------------------------")
    print("\t\t────────────────────────────────────────")
    # prints date and time as day/month/year and hour:minute:second
    print(f"\t\t Date: {current.strftime('%d/%m/%Y')}        Time: {current.strftime('%H:%M:%S')}")
    print("\t\t────────────────────────────────────────")
    print("\t\t Item(s)                     │ Price  ")
    print("\t\t────────────────────────────────────────")
    # for loop iterates through items in the cart
    for item in cart: 
        # print each item the user bought along with it's price
        print(f"\t\t {item['item']:<27} | AED {item['price']:.2f}")
    print("\t\t────────────────────────────────────────")
    print("\t\t\t\t \033[1;36mINVOICE\033[0m")
    print("\t\t────────────────────────────────────────")
    # calculate the total price for all items in the cart using the built-in sum function
    print(f"\t\t\t\t       TOTAL: AED {sum(item['price'] for item in cart):.2f}")
    # if cash was used, print the total amount of money the user inserted
    if card_used is False: 
        print(f"\t\t\t\t\tCASH: AED {cash:.2f}")
    # if change was more than zero, print the change
    if change > 0: 
        print(f"\t\t\t\t      CHANGE: AED {change:.2f}")
    pause()

# MAIN function for user item selection
def selection(card_used, money, cash):
    # initialize change to zero
    change = 0
    # set choice as a global variable (can be used by other functions)
    global choice
    # call category and menu_choice functions to choose the menu category
    category()    # displays the styled box for menu categories
    menu_choice()     # asks user to choose one category then displays selected menu
    pause()     # 1-second delay
    separator()      # line break
    # loop begins
    while True: 
        pause()     # 1-second delay
        # ask user to enter the code of their chosen item
        number = input("\n\t\t\t   \033[1;34mCHOOSE AN ITEM:\033[0m ").strip()
        # loop iterates through the items in the menu selected
        for item in menu_selected:
            # if the number entered by the user matches with an item code from the menu selected
            if number == str(item['code']):
                # set choice as the item selected (chocie stores all the details of the item)
                choice = item
                pause()     # 1-second break
                # if cash was chosen as the preferred payment method
                if card_used == False:
                    # loop starts when the money inserted is less than the item price
                    while money < choice['price']:
                        print("\n\t\t    \033[1;31mMoney inserted is insufficient. \033[0m")
                        while True: 
                            small_pause()      # 0.5-second break
                            # ask user to insert the specific amount of money required more
                            more_money = input("\t     " + "Please insert \033[1;31mAED " + str(choice['price'] - money) + "\033[0m more ( EXIT[0] ): AED ").strip()
                            small_pause()      # 0.5-second pause
                            try: 
                                # 
                                more = float(more_money)
                                # if money inserted again is less than or equal to 0, user exits program
                                if more == 0:
                                    # ends program
                                    sys.exit()
                                # if money entered is less than 0, user is asked to enter money more than 0
                                elif more < 0: 
                                    print("\n\t\t \033[1;31mPlease enter an amount greater than 0.\033[0m")
                                    # begins loop again (user is asked to enter more money again)
                                    continue
                                else: 
                                    # add the money inserted again to the money inserted in the beginning
                                    money += more
                                    # add the money inserted again to the total amount of money inserted into the machine
                                    cash += more
                                    # print the new balance the user has left to use when (all princes in the receipt are rounded to 2 decimal places)
                                    print(f"\n\t\t\t \033[1;32mNew balance: \033[0mAED {money:.2f}")
                                break
                            # handles error in inserting more money (if money can't be converted to float)
                            except ValueError:
                                pause()     # 1-second
                                # print invalid input and asks user to enter appropriate amount
                                print("\n\t      \033[1;31mInvalid input. Please enter a valid amount.\033[0m") 
                    # if the money inserted more than the price of the  item
                    if money > choice['price']: 
                        # subtract the item price from the money inserted
                        money -= choice['price']
                        # set the change to the money left
                        change = money
                        pause()      # 1-second break
                        # function dispenses item and adds it to the cart
                        item_dispensed(cart, choice)
                        # updates item stock (deducts stock by 1)
                        update_stock(menu_selected, number)
                        # print remaining cash after item price is deducted
                        print(f"\t\t\t\033[1;32mCash Remaining: \033[0mAED {money:.2f}")
                        # break out of loop
                        break
                    # if the money inserted is equal to the price of the item
                    elif money == choice['price']:
                        # set money to 0 (no change)
                        money = 0
                        # set change to money (again zero)
                        change = money
                        separator()     # line break
                        # function dispenses item and adds it to the cart
                        item_dispensed(cart, choice)
                        pause() # 1-second break
                        # updates item stock (deducts stock by 1)
                        update_stock(menu_selected, number)
                        # break out of loop
                        break
                # if user chose to pay with a card
                elif card_used == True:
                    ## makes the transaction seem more realistic 
                    # card is being connected with the bank
                    print(f"\n\t\tYour purchase is beingt555t authenticated{small_pause()}.{small_pause()}.{small_pause()}.")
                    small_pause()     # 0.5-second break
                    # print message that item has been purchased
                    print("\t\t     The payment has been deducted. ")
                    pause()     # 1-second break
                    # function dispenses item and adds it to the cart
                    item_dispensed(cart, choice)
                    # updates item stock (deducts stock by 1)
                    update_stock(menu_selected, number)
                    # break out of loop
                    break
        # runs when user doesn't enter a valid item code 
        else: 
            print("\n\t\t \033[0;31mInvalid item number. Please try again.\033[0m")
            # redirects to main while loop (to enter a valid item code)
            continue
        # break out of the main while loop
        break
    pause()     # 1-second break
    separator()     # line break
    pause()     # 1-second break
    # call the suggestions function (shows a personalised suggestion based on the item purchased)
    suggestions(menu_selected)
    pause()
    # loop begins
    while True: 
        # ask user if they want to purchase another item
        contd = input("\n\t      \033[1;34mCONTINUE PURCHASING? ( Yes[1] | No[2] ):\033[0m ").strip()
        # if user wants to purchase another item
        if contd == "1":
            separator()     # line break
            pause()     # 1-second break
            # calls the selection function again 
            selection(card_used, money, cash)
            # break out of loop
            break
        # if user chooses not to continue purchasing
        elif contd == "2":
            # if user chose to use a card
            if card_used is True: 
                pause()     # 1-second break
                # user is prompted to remove their card from the reader
                print("\n\t\t     You may remove your card now.")
                pause()     # 1-second break
            separator()     # line break
            pause()     # 1-second break
            # calls the invoice function (prints a formatted receipt for user's purchase(s))
            invoice(cart, cash, change)
            # break out of loop
            break
        # runs when user enters something other than 1 or 2 (invalid option)
        else:
            # loop continues till user enters a valid option
            print("\n\t\t    \033[0;31mInvalid input. Please try again.\033[0m")

# function to display the thank you and bye message
def thank_you():
    pause()      # 1-second break
    print("\n\t\t      \033[1;33m ♡ Thanks for purchasing! ♡ ")
    small_pause()
    print("\t\t\t\tGoodbye!\033[0m\n")


### START OF PROGRAM

# variable cart as an empty list
cart = []
# initialise variable money to zero
money = 0

# print title of vending machine in ASCII art
print("""\n\033[1;32m
            ╔══════════════════════════════════════════════╗
            ║  ╦  ╦╔═╗╔╗╔╔╦═╗╔╔╗╔╔═╗  ╔╦╗╔═╗╔═╗╦ ╗╗╔╗╔╔═╗  ║
            ║  ╚╗╔╝║╣ ║║║ ║ ║║║║║║ ╦  ║║║╠═╣║  ╠═╣║║║║║╣   ║
            ║   ╚╝ ╚═╝╝╚╝═╩═╝╝╝╚╝╚═╝  ╩ ╩╩ ╩╚═╝╩ ╝╝╝╚╝╚═╝  ║
            ╚══════════════════════════════════════════════╝\033[0m""")  

pause()     # 1-second break

# print a welcome message
print("\n\t\t\t\t\033[1;38;2;128;0;255mWELCOME!\033[0m")
pause()      # 1-second break
separator()     # line break

# list of snack menu
snacks = [
    {"item": "Takis Fuego Crisps", "code": 11, "price": 4, "stock": 3},
    {"item": "Chocolate Pocky", "code": 12, "price": 2, "stock": 3},
    {"item": "Chunko's Cookies", "code": 13, "price": 2.50, "stock": 3},
    {"item": "Haribo Happy Cola Jelly", "code": 14, "price": 5, "stock": 4},
    {"item": "Caramel Popcorn", "code": 15, "price": 3.50, "stock": 2}
]

# list of beverage menu
beverages = [
    {"item": "Water bottle", "code": 21, "price": 1.50, "stock": 5},
    {"item": "Peach Juice", "code": 22, "price": 2, "stock": 2},
    {"item": "Strawberry Milkshake", "code": 23, "price": 3, "stock": 3},
    {"item": "Brown Sugar Milk Tea", "code": 24, "price": 4.50, "stock": 4},
    {"item": "Caramel Macchiato", "code": 25, "price": 5, "stock": 4}
]

# list of dessert menu
desserts = [
    {"item": "Hazelnut Chocolate", "code": 31, "price": 2, "stock": 2},
    {"item": "Plain Glazed Donut", "code": 32, "price": 3, "stock": 3},
    {"item": "Chocolate Mousse", "code": 33, "price": 3.50, "stock": 2},
    {"item": "Caramel Fudge Brownie", "code": 34, "price": 4.50, "stock": 3},
    {"item": "Salted Caramel Ice cream", "code": 35, "price": 4, "stock": 4}
]

# print a styled box asking user for their preferred payment method
payment_method()

# while loop to ensure valid payment method is entered
while True: 
    # ask user if they want to use cash or card
    payment = input("\n\t\t\t \033[1;34mCASH[1] OR CARD[2]?:\033[0m ").strip()   
    # if user inputs 1, payment method is cash 
    if payment == "1":  
        # set variable card_used to False
        card_used = False  
        # while loop to ensure valid amount is inserted
        while True:
            # ask user to insert money (strip removes extra spaces)
            money_inserted = input("\n\t\t   \033[1;33mInsert an amount of money:\033[0m AED ").strip()
            # tests this block of code
            try:
                # money inserted is converted to float and set to money variable
                money = float(money_inserted)
                # if money is more than 0
                if money > 0:
                    pause()     # 1-second break
                    # set cash equal to money 
                    cash = money
                    separator()     # line break
                    # call the pause() function
                    pause()     # 1-second break
                    # break out of while loop
                    break
                # if money inserted is less than or equal to 0
                else:
                    # print enter amount more than 0
                    print("\n\t\t \033[0;31mPlease enter an amount greater than 0.\033[0m")
            # handles error in inserting money
            except ValueError:
                # print enter a valid amount of money
                print("\n\t      \033[0;31mInvalid input. Please enter a valid amount.\033[0m")    
        # break out of outer while loop
        break       

    # if user inputs 2, payment method is card
    elif payment == "2":         
        # set cash to 0
        cash = 0
        # these statements are used to make the program seem more realistic
        print("\n\t\t Place your card into the card reader.")
        pause()
        print("\t\t    Communicating with your bank...")
        pause()
        print("\t\t      Your card has been approved.") 
        # set card_used to True
        card_used = True
        pause()     # 1-second break
        # more realistic (even though there is no physical card)
        print("\n\t\t Please proceed with your purchase(s).")
        separator()     # line break
        pause()     # 1-second break
        # break out of outer while loop
        break  
    # runs when invalid payment method is entered  
    else:        
        print("\n\t \033[0;31mInvalid choice. Please enter 1 for cash or 2 for card.\033[0m")

# MAIN FUNCTION CALLED | selection function as a whole is called (with it's 3 paramters)
selection(card_used, cash, money)
separator()     # line break
# call thank_you function after the receipt to thank the user and say bye
thank_you()