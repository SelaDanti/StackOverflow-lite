import re

class Verifications:
	"""
	class to verify data before inserting to database
	"""
	def __init__(self):
		self.data_err = None

	# check if input is empty
	def is_empty(self,items):
		for item in items:
			if not item:
				self.error = {'result': 'Invalid input(Empty data)'}, 405
				return self.error
		return False

	# check if input contains only space
	def is_space(self,items):
		for item in items:
			if item.isspace() is True:
				self.error = {'result': 'Invalid input(Whitespace data)'}, 405
				return self.error
		return False

	# check if email input is empty
	def is_email(self,email):
		result = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
		if result is None:
			self.error = {'result': 'Invalid email'}, 405
			return self.error
		else:
			return False
