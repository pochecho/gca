from tkinter import Tk
from tkinter import SUNKEN
from tkinter import RAISED
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import StringVar
from tkinter import IntVar
from tkinter import END
from tkinter import Text
from tkinter import filedialog
from tkinter.ttk import *
import os
import re
import json
from pickle import dump, dumps, load, loads
import pyodbc
import html

"""
Definición de variables Globales
"""

bg = "white"
fg = "#3180FF"
bg2 = "#eee"
fg2 = "black"
bgb1 = "#3180FF"
fgb1 = "white"
bgb2 = "#FF2300"
fgb2 = "white"


class Ventana:
	"""docstring for Ventana"""

	def __init__(self, ancho, alto):
		self.ventana = Tk()
		self.ancho = ancho
		self.alto = alto
		self.configurarEstilosBotones()

		self.configurarVentana()

	def configurarVentana(self):
		self.ventana.geometry(str(self.ancho)+"x"+str(self.alto))
		self.ventana.configure(bg=bg)

	def iniciar(self):
		self.ventana.mainloop()

	def configurarEstilosBotones(self):
		style = Style()
		style.configure("ABC.TButton", width="10", height="100",
						background="#3180FF", foreground="white")
		style.configure("AB.TButton", background="#3180FF", foreground="white")
		style.configure("RB.TButton", background="#FF2300", foreground="white")
		style.configure("SmallRB.TButton", background="#FF2300",
						width=3, foreground="white")
		style.configure("Green.TFrame", background="#85FF8B",
						foreground="black")
		style.configure("Blue.TFrame", background="#1e90FF",
						foreground="black")
		style.configure("Green.TLabel", background="#85FF8B",
						foreground="black")
		style.configure("Blue.TLabel", background="#1e90FF",
						foreground="black")
		style.configure("SmallGB.TButton", background="green",
						width=3, foreground="white")


"""
Clase tomada de StackOverFlow, del usuario Nae
"""


class EntryWithPlaceholder(Entry):
	def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
		Entry.__init__(self, master)

		self.placeholder = placeholder
		self.placeholder_color = color
		self.default_fg_color = self['foreground']

		self.bind("<FocusIn>", self.foc_in)
		self.bind("<FocusOut>", self.foc_out)
		self.put_placeholder()

	def put_placeholder(self):
		self.insert(0, self.placeholder)
		self['foreground'] = self.placeholder_color

	def foc_in(self, *args):
		if str(self['foreground']) == self.placeholder_color:
			self.delete('0', 'end')
			self['foreground'] = self.default_fg_color

	def foc_out(self, *args):
		if not self.get():
			self.put_placeholder()


class VentanaModelo(Ventana):
	"""docstring for VentanaModelo"""

	def __init__(self, ancho, alto):
		Ventana.__init__(self, ancho, alto)
		self.ventana.config(bg=bg)

		self.svNombreCrud = StringVar()
		# self.svNombreCrud.set("Phase")

		self.svNombreTableDB = StringVar()
		# self.svNombreTableDB.set("GEN_FASE")

		self.svFolderCrud = StringVar()
		# self.svFolderCrud.set("Parameters")

		self.svKeyCrud = StringVar()
		# self.svKeyCrud.set("Id")

		self.svSearchCrud = StringVar()
		# self.svSearchCrud.set("Id")

		self.svVisibilidad = StringVar()
		self.svVisibilidad.set("-")

		self.svNombre = StringVar()
		# self.svNombre.set("Name")

		self.svDisplayName = StringVar()
		# self.svDisplayName.set("Nombre")

		self.svNombreDB = StringVar()
		# self.svNombreDB.set("NOMBRE")

		self.svTipo = StringVar()
		# self.svTipo.set("string")

		self.svGet = IntVar()
		self.svGet.set(1)

		self.svSet = IntVar()
		self.svSet.set(1)

		self.svRequired = IntVar()
		self.svRequired.set(1)

		self.svLanguage = StringVar()
		self.svLanguage.set("MIDIS")

		self.clase = Clase("NONE", "NONE")

		self.items = 0
		self.itemsObjects = []

		self.svArchivos = {}
		self.inicializarListadoArchivos()

		self.crearEncabezado()
		self.crearFormularioAtributos()
		self.crearPanelSeleccion()
		self.crearBotonesPrincipales()

		self.generadorArchivos = GeneradorArchivos()
		self.generadorCodigoSQL = GeneradorCodigoSQL()

	def inicializarListadoArchivos(self):
		ruta = os.getcwd()
		archivos = os.listdir(ruta+"\\Estructura Base")
		for arc in archivos:
			self.svArchivos[arc] = IntVar()
			self.svArchivos[arc].set(1)

	def crearEncabezado(self):
		self.frameEncabezado = Frame(
			self.ventana, height=80, width=self.ancho-10,   relief=SUNKEN)
		self.frameEncabezado.place(x=5, y=10)

		Label(self.frameEncabezado,
			  text="En esta sección se configuran los nombres globales para utlizar en el crud").place(x=10, y=5)

		Label(self.frameEncabezado, text="Nombre del CRUD").place(x=10, y=32)

		entryNameCrud = EntryWithPlaceholder(
			self.frameEncabezado,   placeholder="Phase")
		entryNameCrud.config(textvariable=self.svNombreCrud, width="25")
		entryNameCrud.place(x=10, y=52)

		Label(self.frameEncabezado, text="Tabla en la BD").place(x=180, y=32)

		entryNameTableDB = EntryWithPlaceholder(
			self.frameEncabezado,   placeholder="GEN_FASE")
		entryNameTableDB.config(textvariable=self.svNombreTableDB, width="25")
		entryNameTableDB.place(x=180, y=52)

		Label(self.frameEncabezado, text="Carpeta final").place(x=350, y=32)

		entryFolderCrud = EntryWithPlaceholder(
			self.frameEncabezado,   placeholder="Parameters")
		entryFolderCrud.config(textvariable=self.svFolderCrud, width="25")
		entryFolderCrud.place(x=350, y=52)

		Label(self.frameEncabezado, text="Atributo Primario").place(x=520, y=32)

		entryKeyCrud = EntryWithPlaceholder(
			self.frameEncabezado,   placeholder="ID")
		entryKeyCrud.config(textvariable=self.svKeyCrud, width="25")
		entryKeyCrud.place(x=520, y=52)

		Label(self.frameEncabezado, text="Atributo de Búsqueda").place(x=690, y=32)

		entryKeyCrud = EntryWithPlaceholder(
			self.frameEncabezado,   placeholder="PREGUNTA")
		entryKeyCrud.config(textvariable=self.svSearchCrud, width="25")
		entryKeyCrud.place(x=690, y=52)

		Label(self.frameEncabezado, text="Lenguaje").place(x=860, y=32)

		comboLanguage = Combobox(self.frameEncabezado)
		comboLanguage["values"] = ["MIDIS", "IONIC", "C", "C++", "PHP"]
		comboLanguage.config(textvariable=self.svLanguage, width="20")
		comboLanguage.place(x=860, y=52)

	def crearBotonesPrincipales(self):
		Button(self.ventana,  command=self.crearArchivos,
			   text="Crear").place(x=680, y=520)
		Button(self.ventana,  command=self.generarScript,
			   text="Script").place(x=770, y=520)
		Button(self.ventana,  command=self.abrirArchivo,
			   text="Abrir").place(x=680, y=560)
		Button(self.ventana,  command=self.guardarArchivo,
			   text="Guardar").place(x=770, y=560)
		Button(self.ventana,  command=self.cargarModelo,
			   text="Restore Modelo").place(x=860, y=560)
		Button(self.ventana,  command=self.editarTokens,
			   text="Editar Tokens").place(x=860, y=520)

	def actualizarCamposAtributos(self):
		self.borrarItems()
		self.crearItems()

	def abrirArchivo(self):
		file_path_string = filedialog.askopenfilename(
			filetypes=[('GCA files', '.CGA')])
		archivo = open(file_path_string, "br")
		self.clase = load(archivo)
		archivo.close()
		self.actualizarCamposAtributos()
		self.actualizarCamposPropiedades()

	def actualizarCamposPropiedades(self):
		self.svNombreCrud.set(self.clase.nombre)
		self.svNombreTableDB.set(self.clase.nombreDB)
		self.svFolderCrud.set(self.clase.folderCrud)
		self.svKeyCrud.set(self.clase.key)
		self.svSearchCrud.set(self.clase.search)
		self.svLanguage.set(self.clase.lenguaje)

	def actualizarAtributosPropiedades(self):
		self.clase.nombre = self.svNombreCrud.get()
		self.clase.nombreDB = self.svNombreTableDB.get()
		self.clase.folderCrud = self.svFolderCrud.get()
		self.clase.key = self.svKeyCrud.get()
		self.clase.search = self.svSearchCrud.get()
		self.clase.lenguaje = self.svLanguage.get()

	def guardarArchivo(self):
		self.actualizarAtributosPropiedades()
		file_path_string = filedialog.asksaveasfile(
			mode="w", defaultextension=".GCA", filetypes=[('GCA files', '.CGA')])
		archivo = open(file_path_string.name, "bw")
		dump(self.clase, archivo)
		archivo.close()

	def editarTokens(self):
		ventanaModelo = VentanaEditToken(1050, 600)
		ventanaModelo.iniciar()

	def generarScript(self):
		
		self.actualizarAtributosPropiedades()
		self.clase.agregarAtributosBase()
		self.generadorCodigoSQL.clase = self.clase
		self.generadorCodigoSQL.ventana = self.ventana
		self.generadorCodigoSQL.generarScript()

	def crearArchivos(self):
		self.actualizarAtributosPropiedades()
		self.generadorArchivos.generarDocumentos(self.clase, self.svArchivos)

	def convertFromSQLToPhp(self, value):
		if (value == "datetime"):
				return "date"
		elif("nvarchar" in value):
    			return "string"
		else:
			return value

	def cargarModelo(self):
		file_path_string = filedialog.askopenfilename(
			filetypes=[('SQL files', '.sql')])
		archivo = open(file_path_string, "r")
		contenido = archivo.read()
		archivo.close()
		patron2 = re.compile("CREATE TABLE [\[dbo\]\.]*[\[\"]*(\w+)[\]\"]*", re.I)
		#patron2 = re.compile("[CREATE TABLE]{1,1} ([\[dbo\]\.]*)", re.I)
		patron = re.compile("(.*,\n)")
  
		patronAtributos = re.compile("(.*,\n)")
		contentAtributos = patronAtributos.search(contenido).groups()[0]	
  
		respuesta2 = patron2.search(contenido).groups()[0]
		respuesta = patron.findall(contenido)
		print(respuesta2)
		print(respuesta)
		self.svNombreCrud.set(respuesta2)
		self.svNombreTableDB.set(respuesta2)
		self.svFolderCrud.set(respuesta2)

		for atrib in respuesta:
			frag = atrib.split(" ")
			nfrag = []
			pat = re.compile("\d*")
			for f in frag:	
				f= pat.sub(f,"")
				nfrag.append(f.replace("\t","").replace("[","").replace("]","").replace("(","").replace(")","").replace("\"",""))
			self.items += 1
			self.clase.atributos.append(
				Atributo(
					nfrag[0],
					self.convertFromSQLToPhp(nfrag[1]),
					"+",  # visibilidad,
					nfrag[0],
					nfrag[0],
					True,
					True,
					True
				)
			)
			self.actualizarCamposAtributos()

	def extraerAtributos(self):
		self.actualizarCamposAtributos()
		self.actualizarCamposPropiedades()
		self.actualizarAtributosPropiedades()

	def crearFormularioAtributos(self):

		self.frameFormularioAtributos = Frame(
			self.ventana, height=50, width=self.ancho-10,  relief=SUNKEN)
		self.frameFormularioAtributos.place(x=5, y=100)

		Label(self.frameEncabezado,
			  text="Se debe especificar las características de los atributos de la entidad a representar").place(x=10, y=10)
		opciones = ["", "+", "-"]
		OptionMenu(self.frameFormularioAtributos,
				   self.svVisibilidad, *opciones).place(x=5, y=20)

		Label(self.frameFormularioAtributos, text="Atributo").place(x=50, y=5)

		entryNombreAtributo = EntryWithPlaceholder(
			self.frameFormularioAtributos, placeholder="Code")
		entryNombreAtributo.configure(textvariable=self.svNombre)
		entryNombreAtributo.place(x=50, y=23)

		Label(self.frameFormularioAtributos,
			  text="Display Name").place(x=180, y=5)

		entryDisplayNameAtributo = EntryWithPlaceholder(
			self.frameFormularioAtributos, placeholder="")
		entryDisplayNameAtributo.configure(textvariable=self.svDisplayName)
		entryDisplayNameAtributo.place(x=180, y=23)

		Label(self.frameFormularioAtributos, text="Campo DB").place(x=310, y=5)

		entryNombreDBAtributo = EntryWithPlaceholder(
			self.frameFormularioAtributos, placeholder="CODIGO")
		entryNombreDBAtributo.configure(textvariable=self.svNombreDB)
		entryNombreDBAtributo.place(x=310, y=23)

		Label(self.frameFormularioAtributos,
			  text="Tipo de dato").place(x=440, y=5)

		entryTipo = Combobox(self.frameFormularioAtributos)
		entryTipo["values"] = ["string", "int",
							   "float", "char", "enum", "double", "bool"]
		entryTipo.config(textvariable=self.svTipo, width="20")
		entryTipo.place(x=440, y=23)

		Checkbutton(self.frameFormularioAtributos, text="G",
					variable=self.svGet).place(x=590, y=23)

		Checkbutton(self.frameFormularioAtributos, text="S",
					variable=self.svSet).place(x=620, y=23)

		Checkbutton(self.frameFormularioAtributos, text="R",
					variable=self.svRequired).place(x=650, y=23)

		Button(self.frameFormularioAtributos, style="SmallGB.TButton",
			   text="+", command=self.agregarAtributo).place(x=700, y=16)

		Button(self.frameFormularioAtributos, style="SmallGB.TButton",
			   text="E", command=self.actualizarAtributo).place(x=750, y=16)

	def agregarAtributo(self):
		self.items += 1
		self.clase.atributos.append(
			Atributo(
				self.svNombre.get(),
				self.svTipo.get(),
				self.svVisibilidad.get(),
				self.svDisplayName.get(),
				self.svNombreDB.get(),
				self.svGet.get(),
				self.svSet.get(),
				self.svRequired.get()
			)
		)
		self.actualizarCamposAtributos()

	def actualizarAtributo(self):
		self.items += 1
		attr = self.clase.searchAttributeObject(self.svNombre.get())

		attr.nombre = self.svNombre.get()
		attr.tipo = self.svTipo.get()
		attr.visibilidad = self.svVisibilidad.get()
		attr.displayName = self.svDisplayName.get()
		attr.nombreDB = self.svNombreDB.get()
		attr.get = self.svGet.get()
		attr.set = self.svSet.get()
		attr.requerido = self.svRequired.get()
  

		self.actualizarCamposAtributos()

	def borrarItems(self):
		for obj in self.itemsObjects:
			obj.destroy()
		self.itemsObjects.clear()

	def crearItems(self):
		i = 0
		for atributo in self.clase.atributos:
			self.crearItem(atributo, i)
			i += 1

	def crearPanelSeleccion(self):
		y = 160
		anchoFrameEx = int(self.ancho*0.7)
		anchoFrame = int(self.ancho*0.28)
		i = 0
		for archivo in self.svArchivos:
			frame = Frame(self.ventana,  width=anchoFrame, height=20)
			frame.place(x=anchoFrameEx, y=y+(22*i))
			Checkbutton(frame, text=archivo,
						variable=self.svArchivos[archivo]).place(x=4, y=1)
			i += 1

	def crearItem(self, atributo, i):
		y = 160
		anchoFrame = int(self.ancho*0.65)
		frame = Frame(self.ventana, style="Blue.TFrame",
					  width=anchoFrame, height=30)
		frame.place(x=10, y=y+(40*i))

		Label(frame, style="Blue.TLabel",
			  text=atributo.imprimir()).place(x=10, y=5)
		Button(frame, text="-", command=lambda: self.eliminarAtributo(i),
			   style="SmallRB.TButton").place(x=anchoFrame-45, y=5)
		Button(frame, text="E", command=lambda: self.editarAtributo(i),
				style="SmallRB.TButton").place(x=anchoFrame-80, y=5)
		self.itemsObjects.append(frame)

	def eliminarAtributo(self, i):
		del self.clase.atributos[i]
		self.items -= 1
		self.actualizarCamposAtributos()
  
	def editarAtributo(self, i):
		attr = self.clase.atributos[i]
		self.svNombre.set(attr.nombre)
		self.svTipo.set(attr.tipo)
		self.svVisibilidad.set(attr.visibilidad)
		self.svDisplayName.set(attr.displayName)
		self.svNombreDB.set(attr.nombreDB)
		self.svGet.set(attr.get)
		self.svSet.set(attr.set)
		self.svRequired.set(attr.requerido)

		self.actualizarCamposAtributos()


class VentanaEditToken(Ventana):
	"""docstring for VentanaEditToken"""

	def __init__(self, ancho, alto):
		Ventana.__init__(self, ancho, alto)
		self.ventana.config(bg=bg)
		self.svText = StringVar()
		self.svText.set("")

		self.svToken = StringVar()
		self.svToken.set("{}")

		self.svLanguage = StringVar()
		self.svLanguage.set("MIDIS")
		self.tokens = {}

		self.crearEncabezado()

		self.inicializarListadoTokens()

		self.crearBotonesPrincipales()

	def inicializarListadoTokens(self):
		ruta = os.getcwd()
		print(ruta+"\\configTokensFuncionesLenguajes.json")
		self.tokens = json.loads(
			open(ruta+"\\configTokensFuncionesLenguajes.json").read())

		self.typesTokens = []
		self.typeLanguaje = []

		for arc in self.tokens["tokens"]:
			if arc not in self.typesTokens:
				self.typesTokens.append(arc)
			for lan in self.tokens["tokens"][arc]:
				if lan not in self.typeLanguaje:
					self.typeLanguaje.append(lan)

		self.comboToken = Combobox(self.frameEncabezado, state="readonly",
								   textvariable=self.svToken, values=self.typesTokens, width="40")
		self.comboToken.bind("<<ComboboxSelected>>", self.updateContent)
		self.comboToken.place(x=10, y=25)

		self.comboLanguage = Combobox(self.frameEncabezado, state="readonly",
									  textvariable=self.svLanguage, values=self.typeLanguaje, width="40")
		self.comboLanguage.bind("<<ComboboxSelected>>", self.updateContent)
		self.comboLanguage.current(0)

		self.comboLanguage.place(x=10, y=52)

		self.text = Text(self.ventana, height=25, width=120)
		self.text.place(x=10, y=100)

		scrollb = Scrollbar(self.frameEncabezado, command=self.text.yview)
		self.text['yscrollcommand'] = scrollb.set

		scrollb2 = Scrollbar(self.frameEncabezado, command=self.text.xview)
		self.text['xscrollcommand'] = scrollb2.set

	def updateContent(self, params):
		self.text.delete("1.0", END)
		token = self.comboToken.current()
		language = self.comboLanguage.current()
		if token >= 0 and language >= 0:
			self.text.insert(
				END, self.tokens["tokens"][self.typesTokens[token]][self.typeLanguaje[language]])
		else:
			print("Error")

	def crearEncabezado(self):
		self.frameEncabezado = Frame(
			self.ventana, height=80, width=self.ancho-10,   relief=SUNKEN)
		self.frameEncabezado.place(x=5, y=10)

		Label(self.frameEncabezado,
			  text="En esta sección se configuran los tokens").place(x=10, y=5)

	def guardarToken(self):
		ruta = os.getcwd()
		content = (self.text.get("1.0", END))
		#content = repr(content)
		token = self.comboToken.current()
		language = self.comboLanguage.current()
		patronSimple = "[\\]{1,1}"
		patronDoble = "[\\]{2,2}"

		comillaPatronSimple = patronSimple+"[\"]{1,1}"
		comillaPatronDoble = patronDoble+"[\"]{1,1}"


		tabPatronSimple = patronSimple+"[\t]{1,1}"
		tabPatronDoble = patronDoble+"[\t]{1,1}"

		saltoPatronSimple = patronSimple+"[\n]{1,1}"
		saltoPatronDoble = patronDoble+"[\n]{1,1}"

		comillaPatronSimpleObj = re.compile(comillaPatronSimple)
		comillaPatronSimpleResult = comillaPatronSimpleObj.findall((content))

		comillaPatronDobleObj = re.compile(comillaPatronDoble)
		comillaPatronDobleResult = comillaPatronDobleObj.findall((content))


		''' content = content.replace("\"","\\\"")
		content = content.replace("\n","\\\n")
		content = content.replace("\t","\\\t") '''

		#content = (content.encode('raw_unicode_escape'))

		content = str(content)
		content = content.replace("\\\n", "\n")
		self.tokens["tokens"][self.typesTokens[token]
							  ][self.typeLanguaje[language]] = content

		with open(ruta+"\\configTokensFuncionesLenguajes.json", "w") as json_file:
			json.dump(self.tokens, json_file, ensure_ascii=False)

	def crearBotonesPrincipales(self):
		Button(self.ventana,  command=self.guardarToken,
			   text="Guardar").place(x=30, y=450)


class GeneradorArchivos:
	"""docstring for generadorArchivos"""

	def __init__(self):
		self.clase = None
		self.contenido = ""
		self.svArchivos = []

	def generarDocumentos(self, clase, svArchivos):
		self.clase = clase
		self.svArchivos = svArchivos
		archivo = open("configRutasTokens.json")
		rutas = json.loads(archivo.read())
		archivo.close()

		archivoConfigFunciones = open("configTokensFuncionesLenguajes.json")
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
		desde = "Estructura Base\\"+archivoTemplate
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
		archivo = open("config.txt", encoding="utf-8")
		rutaDestinoRaiz = archivo.read()

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


class GeneradorCodigoSQL:
	"""docstring for GeneradorCodigoSQL"""

	def __init__(self, clase=None, ventana=None):
		self.clase = clase
		self.ventana = ventana
		self.conexion = None
		self.abrirConexionSQL()

	def abrirConexionSQL(self):
		archivo = open("configDB.txt", "r")
		server, database, username, password = archivo.read().split("\n")
		archivo.close()
		self.conexion = ConectSQL(server, database, username, password)

	def generarScript(self):
		comandoCreateTable = self.generarScriptCreate()
		#comandoInsertMenu = self.generarScriptMenu()
		#comandoInsertMenuRol = self.generarScriptMenuRol()
		#comandoInsertMenuPermiso = self.generarScriptMenuPermiso()
		#comandoInsertMenuPermisoRol = self.generarScriptMenuPermisoRol()

		comandoFinal = comandoCreateTable
		''' + "\n\n" + comandoInsertMenu + "\n\n" + \
			comandoInsertMenuRol+"\n\n" + comandoInsertMenuPermiso + \
			"\n\n" + comandoInsertMenuPermisoRol '''

		arch = open("Script.sql", "w")
		arch.write(comandoFinal)
		arch.close()
		comandoFormId = "select max(ID_MENU) as mx from SEG_MENU;"
		answer = messagebox.askyesno(
			"Confirmación", "¿Desea continuar con la creación del modelo y establecimiento de seguridad?")
		if answer:
			messagebox.showinfo("Script", comandoFinal)
			self.conexion.ejecutarComando(comandoCreateTable)
			#self.conexion.ejecutarComando(comandoInsertMenu)
			#self.conexion.ejecutarComando(comandoInsertMenuRol)
			#self.conexion.ejecutarComando(comandoInsertMenuPermiso)
			#self.conexion.ejecutarComando(comandoInsertMenuPermisoRol)
			#self.conexion.ejecutarComando(comandoFormId, False)
			#self.clase.FormId = self.conexion.FormId

		else:
			messagebox.showinfo(
				"Cancelado", "No se generará ninguna transancción en la base de datos")

	def generarScriptCreate(self):
		scriptCreate = "CREATE TABLE [dbo].["+self.clase.nombreDB+"](\n"

		for atributo in self.clase.atributos:
			scriptCreate += "[" + atributo.nombreDB + "] "+(self.parseType(atributo.tipo))+" " + (
				"PRIMARY KEY " + ("IDENTITY(1,1) " if atributo.tipo == "int" else "")   if atributo.nombreDB == self.clase.key else "") + (" NOT NULL" if atributo.requerido == 1 else "")+",\n"
		scriptCreate = scriptCreate[:len(scriptCreate)-2]+");\n"+ "ALTER TABLE [dbo].["+self.clase.nombreDB+"] WITH CHECK ADD FOREIGN KEY([user_create]) "\
			"REFERENCES [dbo].[usuarios] ([id_pk]);\n"\
			"ALTER TABLE [dbo].["+self.clase.nombreDB+"]  WITH CHECK ADD FOREIGN KEY([user_update]) "\
			"REFERENCES [dbo].[usuarios] ([id_pk]); "\
			"ALTER TABLE [dbo].["+self.clase.nombreDB+"]  WITH CHECK ADD FOREIGN KEY([user_delete]) "\
			"REFERENCES [dbo].[usuarios] ([id_pk]); "
		return scriptCreate

	def generarScriptMenu(self):
		answer = simpledialog.askstring(
			"Input", "Ingrese el nombre del menú", parent=self.ventana)
		comandoInsertMenu = "INSERT [dbo].[SEG_MENU] ([NOMBRE], [ENLACE], [ID_MENU_PADRE], [IMAGEN_MENU], [ORDEN_MOSTRADO])"\
			" VALUES (N'"+answer+"', N'"+self.clase.nombre + \
			"/Index', 0, N'fa-shield', (select  TOP 10000  MAX([ORDEN_MOSTRADO])+1 as maximo from [SEG_MENU]));"

		return comandoInsertMenu

	def generarScriptMenuRol(self):
		comandoInsertMenuRol = "INSERT [dbo].[SEG_ROl_MENU] ([ROL_ID_ROL], [MEN_ID_MENU]) VALUES (1,  (select max(ID_MENU) from SEG_MENU));"
		return comandoInsertMenuRol

	def generarScriptMenuPermiso(self):
		comandoInsertMenuPermiso = "INSERT [dbo].[SEG_MENU_PERMISO] ([MEN_ID_MENU], [PER_ID_PERMISO]) VALUES ( (select max(ID_MENU) from SEG_MENU),1);"
		comandoInsertMenuPermiso += "INSERT [dbo].[SEG_MENU_PERMISO] ([MEN_ID_MENU], [PER_ID_PERMISO]) VALUES ( (select max(ID_MENU) from SEG_MENU),2);"
		return comandoInsertMenuPermiso

	def generarScriptMenuPermisoRol(self):
		comandoInsertMenuPermisoRol = "INSERT [dbo].[SEG_ROL_MENU_PERMISO] ([ROL_MEN_ID_ROL_MENU], [PER_ID_PERMISO]) VALUES ( (select max(ID_ROL_MENU) from SEG_ROL_MENU),1);"
		comandoInsertMenuPermisoRol += "INSERT [dbo].[SEG_ROL_MENU_PERMISO] ([ROL_MEN_ID_ROL_MENU], [PER_ID_PERMISO]) VALUES ( (select max(ID_ROL_MENU) from SEG_ROL_MENU),2);"
		return comandoInsertMenuPermisoRol

	def parseType(self, tipo):
		if tipo == "string":
			return "nvarchar(100)"
		else:
			return tipo


class Atributo:
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


class ConectSQL:

	def __init__(self, server, database, username, password):

		# Some other example server values are
		# server = 'localhost\sqlexpress' # for a named instance
		# server = 'myserver,port' # to specify an alternate port
		self.server = server
		self.database = database
		self.username = username
		self.password = password
		comando = 'DRIVER={SQL Server};SERVER='+server + \
			';DATABASE='+database+';UID='+username+';PWD=' + password
		print(comando)
		self.cnxn = pyodbc.connect(comando)
		self.cursor = self.cnxn.cursor()
		self.FormId = ""

	def ejecutarComando(self, comando, bandera=True):
		print("Comando", comando)
		try:
			row = self.cursor.execute(comando)
			if bandera:
				self.cnxn.commit()
			row = self.cursor.fetchone()

			while row:
				self.FormId = row[0]
				row = self.cursor.fetchone()
		except Exception as e:
			print(e)


ventanaModelo = VentanaModelo(1050, 600)
ventanaModelo.iniciar()
