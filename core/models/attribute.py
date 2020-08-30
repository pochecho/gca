
class Attribute:
	def __init__(self, nombre, tipo, visibilidad, displayName, nombreDB, metodoGet=1, metodoSet=1, requerido=1):
		self.visibilidad = visibilidad
		self.nombre = nombre
		self.displayName = displayName
		self.nombreDB = nombreDB
		self.tipo = tipo
		self.get = metodoGet
		self.set = metodoSet
		self.requerido = requerido

	def imprimir(self):
		return self.visibilidad+" "+self.nombre + " ["+self.displayName+" : "+self.nombreDB+"] "+": " + self.tipo + " {" + ("get" if self.get == 1 else "") + " : "+("set" if self.set == 1 else "")+" } " + ("Requerido" if self.requerido == 1 else "No requerido")
