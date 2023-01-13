class su_edad:
	def __init__(self):
		self._edad = 0
    
	@property
	def edad(self):
		print("metodo de llamado")
		return self._edad
	
	@edad.setter
	def edad(self, a):
		if(a < 18):
			raise ValueError("no cumple la edad")
		print("metodo de agregado")
		self._edad = a

una_persona = su_edad()

una_persona.edad = 19

print(una_persona.edad)
