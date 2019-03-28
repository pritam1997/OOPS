class BankAccount:
	def __init__(self, name, balance=500):
		self.__name = name
		self.__balance = balance

	def getbalance(self):
		print(f"Total Amount is : {self.__balance}")

	def withdrawl(self, value):
		if value < self.__balance:
			self.__balance = self.__balance - value
			print("Remaining Amount : ",self.__balance)
		else:
			print("You not have enough Amount!!!")

	def deposit(self,value):
		self.__balance = self.__balance + value
		print("Total Amount is {}".format(self.__balance))

python1 = BankAccount("Python1")
print("Welcome To Anonymous Bank")
print("Check balance with 1")
print("Withdraw funds with 2")
print("Deposit funds with 3")
print("For Exit type '0'")
while True:
	i = int(input())
	if i == 1 : 
		python1.getbalance()
	elif i == 3:
		n = int(input("Enter deposit Amount : "))
		python1.deposit(n)
	elif i==2:
		n = int(input("How much you want to Withdraw  : "))
		python1.withdrawl(n)
	elif i == 0:
		exit()
	else:
		print("invalid input")
