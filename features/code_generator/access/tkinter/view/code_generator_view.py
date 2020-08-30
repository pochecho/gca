
from core.window import Window

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
import html
from core.models.clase import Clase
from core.models.entry_with_placeholder import EntryWithPlaceholder
from features.code_generator.domain.use_cases.code_generator_use_case import CodeGeneratorUseCase
from core.models.attribute import  Attribute
from features.code_generator.access.tkinter.view.edit_token_view import WindowEditToken
BASE_STRUCTURE = 'base_structure'

class IndexView(Window):

	def __init__(self, width, height):
		Window.__init__(self, width, height)

		self.svNombreCrud = StringVar()

		self.svNombreTableDB = StringVar()

		self.svFolderCrud = StringVar()
		self.svKeyCrud = StringVar()
		self.svSearchCrud = StringVar()

		self.svVisibilidad = StringVar()
		self.svVisibilidad.set("-")

		self.svNombre = StringVar()
		self.svDisplayName = StringVar()
		self.svNombreDB = StringVar()
		self.svTipo = StringVar()
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

		self.sv_files = {}
		self.get_base_structure_files()

		self.create_header()
		self.crearFormularioAttributes()
		self.crearPanelSeleccion()
		self.create_main_buttons()

		self.generadorArchivos = CodeGeneratorUseCase()

	def get_base_structure_files(self):
		path = os.getcwd()
		archivos = os.listdir("{}\\{}".format(path,BASE_STRUCTURE))
		for arc in archivos:
			self.sv_files[arc] = IntVar()
			self.sv_files[arc].set(1)

	def create_header(self):
		self.frameEncabezado = Frame(
			self.window, height=80, width=self.width-10,   relief=SUNKEN)
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

		Label(self.frameEncabezado, text="Attribute Primario").place(x=520, y=32)

		entryKeyCrud = EntryWithPlaceholder(
			self.frameEncabezado,   placeholder="ID")
		entryKeyCrud.config(textvariable=self.svKeyCrud, width="25")
		entryKeyCrud.place(x=520, y=52)

		Label(self.frameEncabezado, text="Attribute de Búsqueda").place(x=690, y=32)

		entryKeyCrud = EntryWithPlaceholder(
			self.frameEncabezado,   placeholder="PREGUNTA")
		entryKeyCrud.config(textvariable=self.svSearchCrud, width="25")
		entryKeyCrud.place(x=690, y=52)

		Label(self.frameEncabezado, text="Lenguaje").place(x=860, y=32)

		comboLanguage = Combobox(self.frameEncabezado)
		comboLanguage["values"] = ["MIDIS", "IONIC", "C", "C++", "PHP"]
		comboLanguage.config(textvariable=self.svLanguage, width="20")
		comboLanguage.place(x=860, y=52)

	def create_main_buttons(self):
		Button(self.window,  command=self.crearArchivos,
			   text="Crear").place(x=680, y=520)
		Button(self.window,  command=self.generarScript,
			   text="Script").place(x=770, y=520)
		Button(self.window,  command=self.open_model_file,
			   text="Abrir").place(x=680, y=560)
		Button(self.window,  command=self.guardarArchivo,
			   text="Serialize").place(x=770, y=560)
		Button(self.window,  command=self.editarTokens,
			   text="Tokens").place(x=860, y=520)

	def update_files(self):
		self.borrarItems()
		self.crearItems()

	def open_model_file(self):
		file_path_string = filedialog.askopenfilename(
			filetypes=[('GCA files', '.CGA')])
		archivo = open(file_path_string, "br")
		self.clase = load(archivo)
		archivo.close()
		self.update_files()
		self.actualizarCamposPropiedades()

	def actualizarCamposPropiedades(self):
		self.svNombreCrud.set(self.clase.nombre)
		self.svNombreTableDB.set(self.clase.nombreDB)
		self.svFolderCrud.set(self.clase.folderCrud)
		self.svKeyCrud.set(self.clase.key)
		self.svSearchCrud.set(self.clase.search)
		self.svLanguage.set(self.clase.lenguaje)

	def actualizarAttributesPropiedades(self):
		self.clase.nombre = self.svNombreCrud.get()
		self.clase.nombreDB = self.svNombreTableDB.get()
		self.clase.folderCrud = self.svFolderCrud.get()
		self.clase.key = self.svKeyCrud.get()
		self.clase.search = self.svSearchCrud.get()
		self.clase.lenguaje = self.svLanguage.get()

	def guardarArchivo(self):
		self.actualizarAttributesPropiedades()
		file_path_string = filedialog.asksaveasfile(
			mode="w", defaultextension=".GCA", filetypes=[('GCA files', '.CGA')])
		archivo = open(file_path_string.name, "bw")
		dump(self.clase, archivo)
		archivo.close()

	def editarTokens(self):
		ventanaModelo = WindowEditToken(1050, 600)
		ventanaModelo.init()

	def generarScript(self):
		
		self.actualizarAttributesPropiedades()
		self.clase.agregarAttributesBase()


	def crearArchivos(self):
		self.actualizarAttributesPropiedades()
		self.generadorArchivos.generarDocumentos(self.clase, self.sv_files)

	def extraerAttributes(self):
		self.update_files()
		self.actualizarCamposPropiedades()
		self.actualizarAttributesPropiedades()

	def crearFormularioAttributes(self):

		self.frameFormularioAttributes = Frame(
			self.window, height=50, width=self.width-10,  relief=SUNKEN)
		self.frameFormularioAttributes.place(x=5, y=100)

		Label(self.frameEncabezado,
			  text="Se debe especificar las características de los atributos de la entidad a representar").place(x=10, y=10)
		opciones = ["", "+", "-"]
		OptionMenu(self.frameFormularioAttributes,
				   self.svVisibilidad, *opciones).place(x=5, y=20)

		Label(self.frameFormularioAttributes, text="Attribute").place(x=50, y=5)

		entryNombreAttribute = EntryWithPlaceholder(
			self.frameFormularioAttributes, placeholder="Code")
		entryNombreAttribute.configure(textvariable=self.svNombre)
		entryNombreAttribute.place(x=50, y=23)

		Label(self.frameFormularioAttributes,
			  text="Display Name").place(x=180, y=5)

		entryDisplayNameAttribute = EntryWithPlaceholder(
			self.frameFormularioAttributes, placeholder="")
		entryDisplayNameAttribute.configure(textvariable=self.svDisplayName)
		entryDisplayNameAttribute.place(x=180, y=23)

		Label(self.frameFormularioAttributes, text="Campo DB").place(x=310, y=5)

		entryNombreDBAttribute = EntryWithPlaceholder(
			self.frameFormularioAttributes, placeholder="CODIGO")
		entryNombreDBAttribute.configure(textvariable=self.svNombreDB)
		entryNombreDBAttribute.place(x=310, y=23)

		Label(self.frameFormularioAttributes,
			  text="Tipo de dato").place(x=440, y=5)

		entryTipo = Combobox(self.frameFormularioAttributes)
		entryTipo["values"] = ["string", "int",
							   "float", "char", "enum", "double", "bool"]
		entryTipo.config(textvariable=self.svTipo, width="20")
		entryTipo.place(x=440, y=23)

		Checkbutton(self.frameFormularioAttributes, text="G",
					variable=self.svGet).place(x=590, y=23)

		Checkbutton(self.frameFormularioAttributes, text="S",
					variable=self.svSet).place(x=620, y=23)

		Checkbutton(self.frameFormularioAttributes, text="R",
					variable=self.svRequired).place(x=650, y=23)

		Button(self.frameFormularioAttributes, style="SmallGB.TButton",
			   text="+", command=self.agregarAttribute).place(x=700, y=16)

		Button(self.frameFormularioAttributes, style="SmallGB.TButton",
			   text="E", command=self.actualizarAttribute).place(x=750, y=16)

	def agregarAttribute(self):
		self.items += 1
		self.clase.atributos.append(
			Attribute(
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
		self.update_files()

	def actualizarAttribute(self):
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
  

		self.update_files()

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
		widthFrameEx = int(self.width*0.7)
		widthFrame = int(self.width*0.28)
		i = 0
		for archivo in self.sv_files:
			frame = Frame(self.window,  width=widthFrame, height=20)
			frame.place(x=widthFrameEx, y=y+(22*i))
			Checkbutton(frame, text=archivo,
						variable=self.sv_files[archivo]).place(x=4, y=1)
			i += 1

	def crearItem(self, atributo, i):
		y = 160
		widthFrame = int(self.width*0.65)
		frame = Frame(self.window, style="Blue.TFrame",
					  width=widthFrame, height=30)
		frame.place(x=10, y=y+(40*i))

		Label(frame, style="Blue.TLabel",
			  text=atributo.imprimir()).place(x=10, y=5)
		Button(frame, text="-", command=lambda: self.eliminarAttribute(i),
			   style="SmallRB.TButton").place(x=widthFrame-45, y=5)
		Button(frame, text="E", command=lambda: self.editarAttribute(i),
				style="SmallRB.TButton").place(x=widthFrame-80, y=5)
		self.itemsObjects.append(frame)

	def eliminarAttribute(self, i):
		del self.clase.atributos[i]
		self.items -= 1
		self.update_files()
  
	def editarAttribute(self, i):
		attr = self.clase.atributos[i]
		self.svNombre.set(attr.nombre)
		self.svTipo.set(attr.tipo)
		self.svVisibilidad.set(attr.visibilidad)
		self.svDisplayName.set(attr.displayName)
		self.svNombreDB.set(attr.nombreDB)
		self.svGet.set(attr.get)
		self.svSet.set(attr.set)
		self.svRequired.set(attr.requerido)

		self.update_files()
