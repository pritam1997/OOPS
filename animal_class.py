class Animal:
	def __init__(self,name,Class):
		self.name = name
		self.Class = Class

class Acquitic(Animal):
	def __init__(self):
		super().__init__(name,Class)

class Amphibion(Animal):
	def __init__(self,name, Class, age):
		super().__init__(name,Class)

	def behave(self):
		return f"{self.name} is able to"
		return 1
deer = Animal("Deer","amphibion")
o = Amphibion(20)
print(o.behave())