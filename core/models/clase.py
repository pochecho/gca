class Clase:
	def __init__(self, nombre, nombreDB="NONE", folderCrud="NONE", lenguaje=".NET-UCALDAS", key="", search=""):
		self.nombre = nombre
		self.nombreDB = nombreDB
		self.folderCrud = folderCrud
		self.lenguaje = lenguaje
		self.key = key
		self.search = search
		self.FormId = ""
		self.atributos = []

	def agregarAtributosBase(self):
		atributos = [
			["user_create", "nvarchar(50)", "+",
			 "Usuario creador", "user_create",1,1,1],
			["created_at", "datetime", "+", "Fecha de creación", "created_at",1,1,1],
			["user_update", "nvarchar(50)", "+",
			 "Usuario editor", "user_update",1,1,0],
			["updated_at", "datetime", "+", "Fecha de edición", "updated_at",1,1,0],
			["user_delete", "nvarchar(50)", "+",
			 "Usuario eliminador", "user_delete",1,1,0],
			["deleted_at", "datetime", "+", "Fecha de eliminación", "deleted_at",1,1,0]
		]
		for x in atributos:
			if(not self.searchAttribute(x[0])):
				self.atributos.append(Atributo(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7])
								  )
	def searchAttribute(self,name):
		respuesta = False
		for	att in self.atributos:
			respuesta = att.nombre == name
			if respuesta:
				break
		return respuesta
	def searchAttributeObject(self,name):
		respuesta = None
		for	att in self.atributos:
			respuesta = att.nombre == name
			if respuesta:
				respuesta =att
				break
		return respuesta
	def imprimir(self):
		cadena = ""
		for atributo in self.atributos:
			cadena += atributo.imprimir() + "\n"
		return self.nombre + "" + self.nombreDB + "\n" + cadena
