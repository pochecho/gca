
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
from core.window import Window

class WindowEditToken(Window):
	"""docstring for WindowEditToken"""

	def __init__(self, width, height):
		Window.__init__(self, width, height)
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
		print(ruta+"\\funtions_token_config.json")
		self.tokens = json.loads(
			open(ruta+"\\funtions_token_config.json").read())

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

		self.text = Text(self.window, height=25, width=120)
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
			self.window, height=80, width=self.width-10,   relief=SUNKEN)
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

		with open(ruta+"\\funtions_token_config.json", "w") as json_file:
			json.dump(self.tokens, json_file, ensure_ascii=False)

	def crearBotonesPrincipales(self):
		Button(self.window,  command=self.guardarToken,
			   text="Guardar").place(x=30, y=450)
