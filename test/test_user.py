import unittest

from app.model.user import User


class TestUser(unittest.TestCase):
	def setUp(self):
		self.correct_data = User('kwame','asiago','kwame@gmail.com','123','admin',False)
		self.not_email = User('kwame','asiago','kwamegmail.com','123','admin',False)
		self.empty_data = User('kwame','asiago','kwame@gmail.com','123','',False)
		self.space_data = User('kwame','asiago','kwame@gmail.com','123','  ',False)

	def tearDown(self):
		self.correct_data = None
		self.not_email = None
		self.empty_data = None
		self.space_data = None
		User.users.clear()

	def test_is_empty(self):
		test = self.empty_data.add_user
		self.assertEqual(test,({'error': 'Input empty'}, 405))

	def test_is_space(self):
		test = self.space_data.add_user
		self.assertEqual(test,({'error': 'input contains only Whitespace)'}, 405))

	def test_is_email(self):
		test = self.not_email.add_user
		self.assertEqual(test,({'error':'Invalid email'},405))

	def test_correct_data(self):
		test = self.correct_data.add_user
		self.assertEqual(test,({'result':'Account created'},200))

	def test_zero_user_found(self):
		test = User.show_all()
		print(test)
		self.assertEqual(test,({'result': 'Non Found'}, 404))

	def test_user_found(self):
		self.correct_data.add_user
		test = len(User.users)
		self.assertNotEqual(test,0)