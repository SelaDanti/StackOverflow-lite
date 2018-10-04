from .verify import Verify


class user(Verify):
	def __init__(self,first_name,last_name,email,password,role):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
		self.role = role

	def add_user(self):
		pass

	def remove_user(self,id):
		pass