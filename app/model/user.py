from .verify import Verifications


class User(Verifications):
	def __init__(self,first_name,last_name,email,password,role,log):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
		self.role = role
		self.log = log

	@property
	def add_user(self):
		pass

	def remove_user(self,id):
		pass

	def login(self):
		pass