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

#indexes------>0,    1,      2,      3
PIZZA_SIZE = ("S",  "M",    "L",    "X")
PIZZA_PRICE = (9.99, 12.99, 17.99, 21.99)

DRINK_PRICE = 3.99
STICKS_PRICE = 6.99
SALES_TAX_RATE = 0.055

# define global variable

num_pizzas = 0
num_drinks = 0
num_breadstix = 0

cost_pizzas = 0
cost_drinks = 0
cost_breadstix = 0

subtotal = 0
taxamt = 0
total = 0

##############  define program functions  ###############
def main():

    more = True

    while more:
        get_user_data()
        perform_calculation()
        display_results()

        askAgain = input("\nWould you like to order more pizza? (Y/N)? ")
        if askAgain.upper() == "N" or askAgain == "n":
            more = False
            print("Enjoy your hot pizza!")
        

def get_user_data():
    global type_pizza, num_pizzas, num_drinks, num_breadstix

    part1 = "Size of pizza you would like to order: "
    part2 = "\n\tS for Small \n\tM for Medium \n\tL for Large \n\tX for Extra Large\nSize:  "
    type_pizza = input(part1 + part2)
    type_pizza = type_pizza.upper()

    num_pizzas = int(input("How many pizzas would you like to order? "))
    num_drinks = int(input("Number of drinks:   "))
    num_breadstix = int(input("Number of breadsticks:   "))


def perform_calculation():

    global size, cost_pizza, cost_drinks, cost_breadstix, taxamt, total, subtotal

    for i in range(len(PIZZA_SIZE)):
        if type_pizza == PIZZA_SIZE[i]:
            cost_pizzas = num_pizzas * PIZZA_PRICE[i]

    cost_drinks = num_drinks * DRINK_PRICE
    cost_breadstix = num_breadstix * STICKS_PRICE

    subtotal = cost_pizzas + cost_drinks + cost_breadstix
    taxamt = subtotal * SALES_TAX_RATE
    total = subtotal + taxamt

def display_results():
    currency = '8,.2f'
    dt_full = str(datetime.datetime.now())
    dt_short = dt_full[1:16]
    line = '-----------------------------'

    print(line)
    print('**** PALERMO PIZZA ****')
    print('Piping Hot Pizzas and Ice Cold Drinks!')
    print('         '   ,   dt_short)
    print(line)
    print('Pizza Pies   $   '   +   format(cost_pizzas,currency))
    print('Drinks   $   '   +   format(cost_drinks,currency))
    print('Breadsticks  $   '   +   format(cost_breadstix,currency))
    print('Subtotal $   '   +   format(subtotal,currency))
    print('Sales Tax    $   '   +   format(taxamt,currency))
    print('Total Price  $   '   +   format(total,currency))
    print(line)


##############  call on main program to execute  ##############
main()











          

