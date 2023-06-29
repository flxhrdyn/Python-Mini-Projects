# A SIMPLE RESTAURANT ORDER SYSTEM 

def menu(): # menu function which will print out the menu list
    
    print("========Restaurant Menu========")
    print("1. Fried Rice       Rp 15,000")
    print("2. Shrimp Tempura   Rp 10,000")
    print("3. Dimsum           Rp 5,000")
    print("===============================")
    print("GET A 50% DISCOUNT IF YOU BUY A MENU IN THE MULTIPLES OF TWO!\n")

menu() # calls menu function

def main(): # main function 
    while True: # While true loop so if the user entered the wrong input the program will ask for the right input
        choice = int(input("Which menu do you want to buy? ")) # this is choice variable
        if choice == 1: # if the user choose menu 1, the following code will run
            price = 15000 # the price for The Fried Rice
            break

        elif choice == 2: # if the user choose menu 2, the following code will run
            price = 10000 # the price for The Shrimp Tempura
            break    

        elif choice == 3: # if the user choose menu 3, the following code will run
            price = 5000 # the price for The Dimsum   
            break

        else: # if the user doesn't choose either menu 1, 2, or 3 the following code will run
            print("Invalid Input!!! Please Enter a Valid Input Option (1, 2, or 3)!!!\n")
        
    quantity = int(input("How many? ")) # this is a quantity variable
    if isEven(quantity): # if the quantity is even then the menu is going to be discounted, quantity is the argument
        discount = price*0.5 # this is the 50% discount calculation
        total = round(quantity*(price - discount)) # total if the menu gets discounted
        print(f"\nYou Get a 50% Discount! \nYour Total Bill is Rp {total}") # print the total bill
    else:
        total = round(price * quantity) # total with normal price
        print(f"Your Total Bill is Rp {total}") # print the total bill
        print("Order quantity is not a multiple of two. No discount applied.")        
            
def isEven(evnum): # function to check whether a number is even or not, ev num is the parameter
    return evnum % 2 == 0 # even number will have a modulus of 0 if divided by 2

main() # calls main function
