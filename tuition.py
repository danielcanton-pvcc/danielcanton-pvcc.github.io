# Name: Wesley Murray, Dan Canton
# Program Purpose: Calculating tuition and fees at PVCC
# Pythonic
#[Comments 1st]
#[Define global variables and constants]
#[next all the functions] defname like variables, but with parentheses at the end () just at the end
#def then indent, first one is def main() then put main() with no space which is last thing in program
#all upper case makes it a constant lowercase makes it a variable


import datetime

##############  define global variable  ##############
# define tax rate and prices

RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# define global variable

inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarship_amt = 0

tuition_amt = 0
inst_fee = 0
cap_fee = 0
act_fee = 0
total = 0
balance = 0

##############  define program functions  ###############
def main():

    more = True

    while more:
        get_user_data()
        perform_calculation()
        display_results()

        yesno = input("\nwould you like to calculate tuition & fees for another student? (Y/N)? ")
        if yesno == "n" or yesno == "N":
            another_student = False
            print("Thank you for enrolling at PVCC. Enjoy the semester!")
        

def get_user_data():
    global inout, numcredits, scholarship_amt
    print('**** PIEDMONT VIRGINIA COMM COLLEGE Tuition & Fees ****')
    inout = int(input("Enter a 1 for IN_STATE; enter a 2 for OUT_OF_STATE: "))
    numcredits = int(input("number of credits registered for: "))
    scholarship_amt = int(input("Scholarship amount received: ")) 

def perform_calculation():
    global tuition, inst_fee, cap_fee, act_fee, total, balance

    if inout == 1:
        tuition = numcredits * RATE_TUITION_IN
        cap_fee = 0

    else:
        tuition = numcredits * RATE_TUITION_OUT
        cap_fee = numcredits * RATE_CAPITAL_FEE

    inst_fee = numcredits * RATE_INSTITUTION_FEE
    act_fee = numcredits * RATE_ACTIVITY_FEE

    total = tuition + cap_fee + inst_fee + act_fee
    balance = total - scholarship_amt
#calculations for the other fees, total, and balance go here

def display_results():
    currency = '8,.2f'
    line = '-----------------------------'

    print(line)
    print('**** PIEDMONT VIRGINIA COMM COLLEGE ****')
    print(' Tuition and Fees Report')
    print(str(datetime.datetime.now()))
    print(line)
    print('Tuition  $   '   +   format(tuition,currency))
    print('Capital Fee  $ '    +   format(cap_fee,currency))
    print('Institution Fee  $   '   +   format(inst_fee,currency))
    print('Activity Fee $   '   +   format(act_fee,currency))
    print('Total Cost   $   '   +   format(total,currency))
    print('Cost covered by Scholarship  $   '   +   format(scholarship_amt,currency))
    print('Remaining Balance    $   '   +   format(balance,currency))
    print(line)

#print statements for the other fees, total, and balance go here

##############  call on main program to execute  ##############
main()











          

