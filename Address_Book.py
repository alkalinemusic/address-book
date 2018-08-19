'''
Create an address book that holds names, address, phone #'s', email, etc...
'''

# Imports
import os
import time



clear = lambda: os.system('cls') # call this using clear()

class Person(): # Person class

	person_id = 0 # This is the initializaion of the counter that will give each new entry a Unique ID

	def __init__(self, first_name, last_name, address, cellPhone, busPhone, email):
		self.first_name = first_name
		self.last_name = last_name
		self.address = address
		self.cellPhone = cellPhone
		self.busPhone = busPhone
		self.email = email

		Person.person_id += 1 # when calling this below to create the person's ID #, use (Person.person_id)

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

''' this function prompts for all the new entry fields, all calling individual functions
	then creating the new Person instance from the Person class
'''
def new_entry():

	print("\nYou selected create an entry")
	first = first_name()
	last = last_name()
	address = address_entry()
	cell = cell_phone_entry()
	business =business_phone_entry()
	email = email_entry()

	print()
	entry = Person(first, last, address, cell, business, email)
	unique_ID = Person.person_id
	print(entry.email) # Debug line
	print() # Debug line
	print(first + "'s ID number is " + str(unique_ID)) # Debug line
	time.sleep(5) # Debug line
	main() # returns to the main menu function

'''
develop the menu
Menu options:
Create a new entry menu: 
give the user multiple ways to search for the entry they'd like to edit
1.this will pull up all entry options
2.update an entry's information: ****this will need to open up a new menu with all the entries as options
'''

def edit_info():
	edit_list_options = [1, 2, 3, 4, 5, 6]
	print("\nYou selected edit an entry\n") # debug line
	while True:
		try:
			clear()
			print("How would you like to search for the entry you'd like to edit?\n")
			print("--------------------")
			print("1. First name")
			print("2. Last name")
			print("3. Address")
			print("4. Cell Phone #")
			print("5. Business Phone #")
			print("6. Email")
			print("--------------------")
			search_entry = int(input(">> "))
			print()
			print("Selection is {}".format(search_entry)) # Debug line
			if int(search_entry) not in edit_list_options:
				continue
			if int(search_entry) in edit_list_options:
				pass   # pick this up for later
		except ValueError:  # handling of user entries other than integers
			clear()
			print("You've selected an incorrect option\n")
			continue
		else:
			break
		# time.sleep(5)
		# main()

'''Update person's info menu:
1. name
2. address
3. cell phone
4. business phone
5. email
'''

def view_person():
	view_list_options = [1, 2, 3, 4, 5, 6]
	clear()
	print("\nYou selected View an entry\n")
	while True: 
		try:
			print("How would you like to search for the listing you wish to view?\n")
			print("--------------------")
			print("1. First name")
			print("2. Last name")
			print("3. Address")
			print("4. Cell Phone #")
			print("5. Business Phone #")
			print("6. Email")
			print("--------------------\n")
			view_selection = int(input(">> "))
			print()	
			print("You selected {}".format(view_selection))
			if int(view_selection) not in view_list_options:
				continue
			if int(view_selection) in view_list_options:
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
View person's info menu:
1. enter name to see all their info
2. give option to edit their info from here
'''

def quit_program():
	print("you chose to exit")  # Debug line
	exit()

# 

def main():
	list_options = [1, 2, 3, 4]
	selection = 0
	while True:
		try:
			clear()
			print("Address Book")
			print("\n")
			print("Please select an option from the following menu\n")
			print("--------------------")
			print("1. Create a new entry")
			print("2. Edit an existing entry")
			print("3. View an entry")
			print("4. Quit program")
			print("--------------------\n")
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
	main()




#initial debugging 
# person01 = Person()
# person01.full_name()
# person01.address_entry()
# person01.cell_phone_entry()
# person01.business_phone_entry()
# person01.email_entry()
# print(person01.full_name + "\n")
# print(person01.address_entry + "\n")
# print(person01.cell_phone_entry + "\n")
# print(person01.business_phone_entry + "\n")
# print(person01.email_entry + "\n")
