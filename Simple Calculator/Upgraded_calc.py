def menu(): # function to print the menu
    print("======CALCULATOR======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("======================")

menu() # calls the menu function

def main(): # function main to calculate teh number input
    while True: # while loop so if the user entered the wrong choice, the program will ask for the choice again
        choice = int(input("What Do You Want? ")) # accept user's choice input
        if choice == 1: # if the choice is 1 
            x, y = num_input() # declare x and y as num_input function
            print(f"X + Y is {x+y}") # print x + y
            break # break the while loop so the program stops after showing the result

        elif choice == 2: # if the choice is 2
            x, y = num_input()
            print(f"X - Y is {x-y}") # print x - y
            break

        elif choice == 3: # if the choice is 3
            x, y = num_input()
            print(f"X * Y is {x*y}") # print x * y
            break

        elif choice == 4: # if the choice is 4
            x, y = num_input()
            print(f"X / Y is {x/y}") # print x / y
            break

        elif choice == 5: # if the choice is 5
            x, y = num_input()
            print(f"X % Y is {x%y}") # print x % y
            break

        else: # if the choice is none of the above 
            print("Input a Valid Choice!!!") # print str that tells if the choice is invalid
            continue # continue the loop if the choice is still invalid

def num_input(): # function for user input
    x = int(input("What's X? ")) # x is the first number
    y = int(input("What's Y? ")) # y is the second number
    return x, y # return the value of x and y

main() # calls the main function