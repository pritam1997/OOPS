class user:
	user_list = 0
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		if age > 0 and age < 80:
			self._age = age
		else:
			print("Enter valid age, please..!!")
		user.user_list += 1

	def logout(self):
		user.user_list -= 1
		return user.user_list

	# def show_age():


	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0].upper()}.{self.last[0].upper()}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def bday(self):
		self.age += 1
		return f"Happy {self.age}th bday {self.first}"

	def active_user(self):
		return user.user_list

class Moderator(user):
	mod_list = 0
	def __init__(self, first, last, age, community):
		super().__init__(first, last, age)
		self.community = community
		Moderator.mod_list += 1

	def active_mods(self):
		return Moderator.mod_list

	def remove(self):
		return f"{self.first} removed the post being the moderator of {self.community} community"


u1 = user('pritam1','vishwakarma',46)
u2 = user('pritam2','vishwakarma',45)
u3 = user('pritam3','vishwakarma',48)
jasmine = Moderator('jasmine','lopez',55, 'programmers')

# print(jasmine.full_name())
# print(jasmine.initials())
# print(jasmine.remove())
print(u1.active_user())
print(jasmine.active_mods())
print(jasmine._age)