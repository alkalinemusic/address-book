'''
Create an address book that holds names, address, phone #'s', email, etc...
'''

# Imports
import os
import time
import csv

def checkFilePath():
	file_path = os.path.join(os.path.expanduser('~'),"Your_Address_Book.csv")
	if os.path.isfile(file_path) == False:
		print("This file does not exist") # debug line
		time.sleep(5) # debug line
		with open(os.path.join(os.path.expanduser('~'),"Your_Address_Book.csv"), "a") as csvFile:
			file_writer = csv.writer(csvFile, delimiter=",",
								quotechar="|", quoting=csv.QUOTE_MINIMAL)
			file_writer.writerow(['First', 'Last', 'Address', 'Cell Phone', 'Business Phone', 'Email'])	


	else:
	
		print("File already exists!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") # debug line
		time.sleep(2) # Debug line
		main()




# with open(os.path.join(os.path.expanduser('~'),"Your_Address_Book.csv"), "a") as csvFile:
# 	file_writer = csv.writer(csvFile, delimiter=",",
# 						quotechar="|", quoting=csv.QUOTE_MINIMAL)
# 	file_writer.writerow(['ID', 'First', 'Last', 'Address', 'Cell Phone', 'Business Phone', 'Email'])




clear = lambda: os.system('cls') # call this using clear()

class Person(): # Person class

	# person_id = 0 # This is the initializaion of the counter that will give each new entry a Unique ID FIXME will probably be taken out, no ID # needed

	def __init__(self, first_name, last_name, address, cellPhone, busPhone, email):
		self.first_name = first_name
		self.last_name = last_name
		self.address = address
		self.cellPhone = cellPhone
		self.busPhone = busPhone
		self.email = email

		# Person.person_id += 1 # when calling this below to create the person's ID #, use (Person.person_id) FIXME removing ID from entire program
		# unique_ID = Person.person_ # FIXME probably taking out the ID from the program
		# full_entry = ""
		# full_entry += str(unique_ID) # FIXME probably taking out the ID from the program

	def full_name(self):
		return '{} {}'.format(self.first_name, last_name) #creating a full name

	
def first_name(): # simple entry for first name
	first_name = input("Enter the first name: ")
	return first_name

def last_name(): # simple entry for last name
	last_name = input("Enter the last name: ")
	return last_name

def address_entry(): # simple entry for address
	address_entry = input("Enter the address: ")
	return address_entry

def cell_phone_entry(): # simple entry for cell phone
	cell_phone_entry = input("Enter the cell phone number: ")
	return cell_phone_entry

def business_phone_entry(): # simple entry for business phone
	business_phone_entry = input("Enter the business phone number: ")
	return business_phone_entry

def email_entry(): # simple entry for email
	email_entry = input("Enter the email address: ")
	return email_entry


'''
work on the above section, how to call class instances that were just created 
by the create_new_entry function
'''

''' 
	this function prompts for all the new entry fields, all calling individual functions
	then creating the new Person instance from the Person class
'''

'''
develop the menu
Menu options:
Create a new entry menu: 
give the user multiple ways to search for the entry they'd like to edit
1.this will pull up all entry options
2.update an entry's information: ****this will need to open up a new menu with all the entries as options
'''
def new_entry():
 	
	# unique_ID = Person.person_id  #FIXME probably removing ID from the program

	print("\nYou selected create an entry")
	first = first_name()
	last = last_name()
	address = address_entry()
	cell = cell_phone_entry()
	business =business_phone_entry()
	email = email_entry()

	print()
	entry = Person(first, last, address, cell, business, email)
	

	print(entry.email) # Debug line
	print() # Debug line
	# print(first + "'s ID number is " + str(unique_ID)) # Debug line FIXME: This ID number will most likely be taken out
# open the csv file and write the data for the current entry to it
	with open(os.path.join(os.path.expanduser('~'),"Your_Address_Book.csv"), "a") as csvFile:
		file_writer = csv.writer(csvFile, delimiter = ',',
								  quotechar='"', quoting=csv.QUOTE_MINIMAL)
		file_writer.writerow([entry.first_name, entry.last_name, entry.address, entry.cellPhone,
							  entry.busPhone, entry.email])
	# create_csv_entry()
	time.sleep(5) # Debug line
	main() # returns to the main menu function



'''Update person's info menu:
1. name
2. address
3. cell phone
4. business phone
5. email
'''

def edit_info():
	edit_list_options = [1, 2, 3, 4, 5, 6]
	print("\nYou selected edit an entry\n") # debug line
	while True:
		try:
			clear()
			print(" How would you like to search for the entry you'd like to edit?\n")
			print(" --------------------")
			print(" 1. First name")
			print(" 2. Last name")
			print(" 3. Address")
			print(" 4. Cell Phone #")
			print(" 5. Business Phone #")
			print(" 6. Email")
			print(" 7. Quit program")
			print(" --------------------")
			search_entry = int(input(">> "))
			print()
			print("Selection is {}".format(search_entry)) # Debug line
			if int(search_entry) not in edit_list_options:
				continue
			if int(search_entry) in edit_list_options:
				if search_entry == 1:
					first = first_name()
					print('You entered: %s' % first) # debug line - remove
					time.sleep(2) # debug line - remove
					# FIXME: call function to edit existing entry
				if search_entry == 2:
					last = last_name()
					print('You entered: %s' % last)
					time.sleep(2) # debug line - remove
					#FIXME:
				if search_entry == 3:
					address = address_entry()
					print('You entered: %s' % address)
					time.sleep(2) # debug line - remove
					#FIXME:
				if search_entry == 4:
					cell = cell_phone_entry()
					print('You entered: %s' % cell)
					time.sleep(2) # debug line - remove
					#FIXME:
				if search_entry == 5:
					business = business_phone_entry()
					print('You entered: %s' % business) # debug line - remove
					time.sleep(2) # debug line - remove
					#FIXME:
				if search_entry == 6:
					email = email_entry()
					print('You entered: %s' % email) # debug line - remove
					time.sleep(2) # debug line - remove
					#FIXME:
				if search_entry == 7:
					quit_program()
		except ValueError:  # handling of user entries other than integers
			clear()
			print("You've selected an incorrect option\n")
			continue
		else:
			break
		# time.sleep(5)
		# main()



'''
View person's info menu:
1. enter name to see all their info
2. give option to edit their info from here
'''


def view_person():
	view_list_options = [1, 2, 3, 4, 5, 6, 7]
	clear()
	print("\nYou selected View an entry\n")
	while True: 
		try:
			print(" How would you like to search for the entry you wish to view?\n")
			print(" --------------------")
			print(" 1. First name")
			print(" 2. Last name")
			print(" 3. Address")
			print(" 4. Cell Phone #")
			print(" 5. Business Phone #")
			print(" 6. Email")
			print(" 7. Quit Program")
			print(" --------------------\n")
			view_selection = int(input(">> "))
			print()	
			print("You selected {}".format(view_selection))
			time.sleep(2)
			clear()
			if int(view_selection) not in view_list_options:
				continue
			if int(view_selection) in view_list_options:
				if view_selection == 1:
					first = first_name()
					print('You entered: %s' % first) # debug line - remove
					time.sleep(2) # debug line - remove
					view_entry_search(first)
				elif view_selection == 2:
					last = last_name()
					print('You entered: %s' % last) # debug line - remove
					time.sleep(2) # debug line - remove
					view_entry_search(last)
				elif view_selection == 3:
					address = address_entry()
					print('You entered: %s' % address) # debug line - remove
					time.sleep(2) # debug line - remove
					view_entry_search(address)
				elif view_selection == 4:
					cell = cell_phone_entry()
					print('You entered: %s' % cell) # debug line - remove
					time.sleep(2) # debug line - remove
					view_entry_search(cell)
				elif view_selection == 5:
					business = business_phone_entry()
					print('You entered: %s' % business) # debug line - remove
					time.sleep(2) # debug line - remove
					view_entry_search(business)
				elif view_selection == 6:
					email = email_entry()
					print('You entered: %s' % email) # debug line - remove
					time.sleep(2) # debug line - remove
					view_entry_search(email)
				elif view_selection == 7:
					quit_program()
				pass
		except ValueError:
			clear()
			print("You entered an incorrect option\n")
			continue
		else:
			break

		time.sleep(5)
		main()

'''
search_entry_missing function handles any user entry from the view_person function that is not found 
in the view_entry_search function. Flow is then redirected back to the view_person function to try again

this seems to be triggered by the view_entry_search funtion if I put it in as an else statement
need to figure out how to handle for the wrongly entered entries
'''

def search_entry_missing():
	clear()
	print('\nThat entry does not appear to exist in the address book.\n' \
		  'Please check your spelling. Remember capitalization counts.')
	time.sleep(5)
	view_person()

'''
View entry function
will open csv file and search the file for the user's preferred choice of search. i.e. first name, last name, phone, etc
if the entry from view_person function is not found in the DB search, flow is redirected to the search_entry_missing function

'''

def view_entry_search(entry_choice):
	
	with open("C:\\Users\\ashep\\Your_Address_Book.csv", "r") as csv_file:
	    csv_file_reader = csv.reader(csv_file)
	    for row in csv_file_reader:
	        for field in row:
	            if field == entry_choice:
	                print('%-20s | %-20s | %-50s \n' \
	                 '%-20s | %-20s | %-35s' \
	                      % (row[0], row[1], row[2], row[3], row[4], row[5])) # FIXME: need to re-format how this reads
	                time.sleep(5) # Debug line, may need to change or put in condition to let user leave the printed line


	main()

'''
Edit entry function
will open csv file and search the file for the entry choice of search(first, last, etc.)
Function will then print out the matching entry and ask user to confirm. 
Once confirmed, will need to build a menu to ask what specifically they'd like to edit.
This will continue until all desired entries are edited.

'''





def quit_program():
	print("you chose to exit")  # Debug line
	exit()


def main():
	list_options = [1, 2, 3, 4]
	selection = 0
	while True:
		try:
			clear()
			print(" Address Book")
			print(" \n")
			print(" Please select an option from the following menu\n")
			print(" --------------------")
			print(" 1. Create a new entry")
			print(" 2. Edit an existing entry")
			print(" 3. View an entry")
			print(" 4. Quit program")
			print(" --------------------\n")
			selection = int(input(">> "))
			print("selection is {}".format(selection)) # Debug handling of user entries as ints but not available in the menu
			if int(selection) not in list_options:
				continue
			if int(selection) in list_options:
				if int(selection) == 1:
					new_entry()
				elif int(selection) == 2:
					edit_info()
				elif int(selection) == 3:
					view_person()
				elif int(selection) == 4:
					quit_program()

		except ValueError:  # handling of user entries other than integers
			clear()
			print("You've selected an incorrect option\n")
			continue
		else:
			break




if __name__=="__main__":
	checkFilePath()
	main()
