import json
import os
class CodeGeneratorUseCase:
	"""docstring for generadorArchivos"""

	def __init__(self):
		self.clase = None
		self.contenido = ""
		self.svArchivos = []

	def generarDocumentos(self, clase, svArchivos):
		self.clase = clase
		self.svArchivos = svArchivos
		archivo = open("tokens_path_config.json")
		rutas = json.loads(archivo.read())
		archivo.close()

		archivoConfigFunciones = open("funtions_token_config.json")
		archivoFunciones = json.loads(archivoConfigFunciones.read())
		archivoFunciones = archivoFunciones["tokens"]

		rutasInfo = rutas["informacion"]
		for ruta in rutasInfo:
			if self.svArchivos[ruta["archivoOrigen"]].get() == 1:
				dirFinal = self.generarArchivoGuiadoRuta(
					ruta["rutaFinal"], ruta["archivoOrigen"])
				self.generarTokens(dirFinal, ruta["tokens"], archivoFunciones)

	def generarArchivoGuiadoRuta(self, ruta, archivoTemplate):
		nameArchivo = self.reemplazarNombreArchivo(archivoTemplate)
		desde = "base_structure\\"+archivoTemplate
		hacia = self.obtenerRutaFinalArchivo(ruta, nameArchivo)

		# Se crea el comando final
		comando = ("copy  \""+desde + "\" \""+hacia+"\"")
		# Se ejecuta el comando
		os.system(comando)
		return hacia

	def formatearRuta(self, ruta, bo=False):
		if bo:
			return ruta.replace("\\", "/")
		else:
			return ruta.replace("/", "\\")

	def crearDirectorio(self, rutaDestino, rutaRel):

		rutaDestino = self.formatearRuta(rutaDestino, False)
		rutaRel = self.formatearRuta(rutaRel.replace(
			"{NameCrud}", self.clase.nombre), False)
		rutaRel = rutaRel.replace("{Folder}", self.clase.folderCrud)
		fragmentos = rutaRel.split("\\")
		fragmentos = fragmentos[1:len(fragmentos)-1]
		for frag in fragmentos:
			try:
				os.mkdir(rutaDestino+"\\"+frag)
			except Exception as e:
				pass
				#print("Se trata de crear una carpeta que ya existe (" +rutaDestino+"\\"+frag+")")
			rutaDestino += "\\"+frag

	def reemplazarNombreArchivo(self, nameTemplate):
		frags = self.clase.nombre.split("_")
		token = ""
		for frag in frags:
			token +=frag.capitalize()
		nameTemplate = nameTemplate.replace("{NameCrudCapitalize}", token)
		return nameTemplate.replace("{NameCrud}", self.clase.nombre)

	def obtenerRutaFinalArchivo(self, ruta, nameArchivo):
		# Obtención de la dirección raiz de la solución en .NET
		archivo = open("gca.config.json", encoding="utf-8")
		rutaDestinoRaiz = archivo.read()
		rutaDestinoRaiz = json.loads(rutaDestinoRaiz)['base_path']

		# Se cierra el archivo del template
		archivo.close()

		# Se crean los directorios necesarios donde se alojará el archivo
		self.crearDirectorio(rutaDestinoRaiz, ruta)

		# Ruta absoluta final donde estará el archivo  en formato MS-DOS
		hacia = self.formatearRuta(
			rutaDestinoRaiz + ruta.replace("{NameCrud}", self.clase.nombre)+nameArchivo)
		hacia = hacia.replace("{Folder}", self.clase.folderCrud)
		return hacia

	def obtenerContenidoArchivoFinal(self, ruta):
		archivo = open(ruta, encoding="utf-8")
		contenido = archivo.read()
		archivo.close()
		return contenido

	def generarTokens(self, ruta, listadoTokens, archivoFunciones):
		self.contenido = self.obtenerContenidoArchivoFinal(ruta)
		for token in listadoTokens:
			# obtener la funcion a ejecutar para el token correspondiente
			functionEval = archivoFunciones[token][self.clase.lenguaje]
			try:
				t = exec(functionEval)
				print(t)
			except SyntaxError as identifier:
				print(identifier.lineno)
			#self.contenido = self.contenido.replace("\'", "\"")
			#print("Despues del token " + token + " el contenido queda " + contenido)
		self.escribirContenidoArchivoFinal(ruta, self.contenido)

	def escribirContenidoArchivoFinal(self, ruta, contenido):
		archivo = open(ruta, "w", encoding="utf-8")
		#contenido = contenido[1:]
		archivo.write(contenido)
		archivo.close()
