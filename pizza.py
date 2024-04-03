# Name: Dan, Caleb 
# Program Purpose: Calculate the price of an order at Palermo Pizza
# Pythonic
#[Comments 1st]
#[Define global variables and constants]
#[next all the functions] defname like variables, but with parentheses at the end () just at the end
#def then indent, first one is def main() then put main() with no space which is last thing in program
#all upper case makes it a constant lowercase makes it a variable


import datetime

##############  define global variable  ##############
# define pizza prices and sales tax

SMALL = 9.99
MEDIUM = 12.99
LARGE = 17.99
EXTRA_LARGE = 21.99
DRINK = 3.99
BREADSTICK = 6.99
SALES_TAX = 0.055

# define global variable

num_pizza = 0
num_drinks = 0
num_breadstick = 0
drink_total = 0
bread_total = 0
pizza_total = 0
sales_tax_amt = 0
subtotal = 0
total = 0


##############  define program functions  ###############
def main():

    more = True

    while more:
        get_user_data()
        perform_calculation()
        display_results()

        yesno = input("\nWould you like to order more pizza? (Y/N)? ")
        if yesno == "n" or yesno == "N":
            more = False
            print("Enjoy your hot pizza!")
        

def get_user_data():
    global num_breadstick, num_drinks, num_pizza, pizza_size

    pizza_size = input("\What size pizza would you like? (S/M/L/XL)?:   ")
    if pizza_size == "s" or pizza_size == "S":
        pizza_size = SMALL

    elif pizza_size == "m" or pizza_size == "M":
        pizza_size = MEDIUM

    elif pizza_size == "l" or pizza_size == "L":
        pizza_size = LARGE

    elif pizza_size == "xl" or pizza_size == "XL":
        pizza_size = EXTRA_LARGE


    num_pizza = int(input("How many pizzas would you like?: "))
    num_breadstick = int(input("How many breadsticks would you like?:   "))
    num_drinks = int(input("How many drinks would you like?:    "))


def perform_calculation():
    global subtotal, total, sales_tax_amt, pizza_total, drink_total, bread_total

    if pizza_size == SMALL:
        pizza_total = SMALL * num_pizza

    elif pizza_size == MEDIUM:
        pizza_total = MEDIUM * num_pizza

    elif pizza_size == LARGE:
        pizza_total = LARGE * num_pizza

    elif pizza_size == EXTRA_LARGE:
        pizza_total = EXTRA_LARGE * num_pizza

    drink_total = DRINK * num_drinks
    bread_total = BREADSTICK * num_breadstick

    subtotal = pizza_total + drink_total + bread_total
    sales_tax_amt = subtotal * SALES_TAX
    
    total = subtotal + sales_tax_amt

def display_results():
    currency = '8,.2f'
    line = '-----------------------------'

    print(line)
    print('**** PALERMO PIZZA ****')
    print('Piping Hot Pizzas and Ice Cold Drinks!')
    print(str(datetime.datetime.now()))
    print(line)
    print('Pizza Pies   $   '   +   format(pizza_total,currency))
    print('Drinks   $   '   +   format(drink_total,currency))
    print('Breadsticks  $   '   +   format(bread_total,currency))
    print('Subtotal $   '   +   format(subtotal,currency))
    print('Sales Tax    $   '   +   format(sales_tax_amt,currency))
    print('Total Price  $   '   +   format(total,currency))
    print(line)


##############  call on main program to execute  ##############
main()











          

