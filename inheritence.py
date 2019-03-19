
class Abase:
	p="class A variable"
	def functionA(self):
		a="from function A"
		return a

class Bbase(Abase):
	q = "class B variable"
	def functionB(self):
		b="from function B"
		return b

class Cbase(Bbase):
	r = "class C variable"
	def functionC(self):
		c="from function C"
		return c

oc = Cbase()
print(oc.p+oc.q)
var1 = oc.functionA()
var2 = oc.functionB()
var3 = oc.functionC()

print(var1 + var2 + var3)