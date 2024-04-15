# Name: Daniel Canton
# Program Purpose: This program finds the cost of movie tickets
#	Price for one ticket: $10.99
#	Sales tax rate: 5.5%

import datetime

##### define global variables #####
# define tax rate and relief percentage
ANNUAL_TAX = .042
TAX_RELIEF = .33

# define global variables
assessed_value = 0
eligible_yn = "n"
annual_amt = 0
six_month = 0
relief_amt = 0
pre_relief = 0
total_due = 0

##### define program functions #####
def main():

	more = True

	while more:
		get_user_data()
		perform_calculations()
		display_results()

		yesno = input('\nIs there another vehicle? (Y or N)')
		if yesno == "N" or yesno == "n":
			more = False
			print('Personal Property Tax must be paid by due date')
	
def get_user_data():
	global assessed_value, eligible_yn
	assessed_value = int(input("What is the assessed value of the vehicle?:    "))
	eligible_yn = str(input("Is this vehicle eligible for tax relief? (Y or N)"))
	eligible_yn = eligible_yn.upper()

def perform_calculations():
	global annual_amt, six_month, pre_relief, relief_amt, total_due
	annual_amt = assessed_value * ANNUAL_TAX
	six_month = annual_amt / 2
	
	if eligible_yn == "Y":
		relief_amt = six_month * TAX_RELIEF

	else:
		relief_amt = 0

	total_due = six_month - relief_amt
	
def display_results():	
	moneyf = '8,.2f'
	line = ("-----------------------------------------------")


	print(line)
	print('**** CHARLOTTESVILLE, VIRGINIA PERSONAL PROPERTY TAX ****')
	print(line)
	print("ANNUAL TAX DUE:	"	+	format(annual_amt,moneyf))
	print("SIX MONTH TAX DUE:	"	+	format(six_month,moneyf))
	print("TAX RELIEF AMOUNT:	"	+	format(relief_amt,moneyf))
	print("CURRENT DUE AFTER RELIEF:	"	+	format(total_due,moneyf))
	print(str(datetime.datetime.now()))
	
##### call on main program to execute #####
main()