'''
Create an address book that holds names, address, phone #'s', email, etc...
'''

class Person():


	def __init__(self):
		self.name = []
		self.address = []
		self.cellPhone = []
		self.busPhone = []
		self.email = []

	def name_entry(self):
		self.name_entry = input("Enter your name: ")

	def address_entry(self):
		self.address_entry = input("Enter the address for {}: ".format(self.name_entry))

	def cell_phone_entry(self):
		self.cell_phone_entry = input("Enter the cell phone number for {}: ".format(self.name_entry))

	def business_phone_entry(self):
		self.business_phone_entry = input("Enter the business phone number for {}: ".format(self.name_entry))

	def email_entry(self):
		self.email_entry = input("Enter the email address for {}: ".format(self.name_entry))




def new_entry():
	print("\n You selected create an entry")

'''
develop the menu
Menu options:
Create a new entry menu: 
1.this will pull up all entry options
2.update an entry's information: ****this will need to open up a new menu with all the entries as options
'''

def edit_info():
	print("\n You selected edit an entry")

'''
Update person's info menu:
1. name
2. address
3. cell phone
4. business phone
5. email
'''

def view_person():
	print("\n You selected View an entry")

'''
View person's info menu:
1. enter name to see all their info
2. give option to edit their info from here
'''


# 

def main():
	print("Address Book")
	print("\n")
	print("Please select an option from the following menu\n")
	print("--------------------")
	print("1. Create a new entry")
	print("2. Edit an existing entry")
	print("3. View an entry")
	print("--------------------\n")
	selection = int(input(">> "))
	if selection == 1:
		new_entry()
	elif selection == 2:
		edit_info()
	elif selection == 3:
		view_person()
	else:
		print("You've selected an incorrect option")
		main()

if __name__=="__main__":
	main()

#initial debugging 
# person01 = Person()
# person01.name_entry()
# person01.address_entry()
# person01.cell_phone_entry()
# person01.business_phone_entry()
# person01.email_entry()
# print(person01.name_entry + "\n")
# print(person01.address_entry + "\n")
# print(person01.cell_phone_entry + "\n")
# print(person01.business_phone_entry + "\n")
# print(person01.email_entry + "\n")