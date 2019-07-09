class Account:
	def __init__(self,first_name,second_name,balance):
		self.firstname=first_name
		self.second_name=second_name
		self.balance=balance
	def deposit(self.amount)
		self.balance=self.balance+amount
		return "hello  {} {} ,you have succefuly deposited {} into yor account"

	def withdraw (self,amount):
		if self.balance>amount:
			self.balance=self.balance
			return "Dear {} {},you have withdraw sh  {} from your account"
		else:
			return "sorry you have insufficient balance for you transaction to be reached"

	def check_accountbalance(self):
		return "Dear {} {} ,your balance is {}".format(self.balance)
