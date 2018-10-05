from .verify import Verifications


class User(Verifications):
	users = []
	def __init__(self,first_name,last_name,email,password,role,log):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
		self.role = role
		self.log = log

	def check_data(self):
		lst = [self.first_name,self.last_name,self.email,self.password,self.role]
		if self.is_empty(lst) is True:
			return self.display_error
		elif self.is_space(lst) is True:
			return self.display_error
		elif self.is_email(self.email):
			return self.display_error
		else:
			data = {
			'first_name': self.first_name,
			'last_name': self.last_name,
			'email': self.email,
			'password': self.password,
			'role': self.role,
			'log': False,
			'id':len(self.users)
			}
			self.users.append(data)
			return ({'result': 'Account created'},200)

	@property
	def add_user(self):
		if self.check_data() is not True:
			return self.check_data()
		else:
			return False

	@classmethod
	def show_all_user(cls):
		if len(cls.users) == 0:
			return ({'result':'Non Found'},404)
		else:
			return cls.users

	@classmethod
	def show_one_user(cls,id):
		try:
			return cls.users[id]
		except IndexError:
			return ({'result':'Non Found'},404)

	@classmethod
	def login(cls,email,password):
		for i in cls.users:
			if i['email'] == email and i['password'] == password:
				return True
				break
		return ({'result':'Invalid email or password'},401)
