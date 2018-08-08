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



person01 = Person()
person01.name_entry()
person01.address_entry()
person01.cell_phone_entry()
person01.business_phone_entry()
person01.email_entry()
print(person01.name_entry + "\n")
print(person01.address_entry + "\n")
print(person01.cell_phone_entry + "\n")
print(person01.business_phone_entry + "\n")
print(person01.email_entry + "\n")


