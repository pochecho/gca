
from core.window import Window

from tkinter import Tk
# from tkinter import ttk

from tkinter import SUNKEN
from tkinter import RAISED
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import StringVar
from tkinter import IntVar
from tkinter import END
from tkinter import Text
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import Frame
from tkinter import LEFT, TOP
from tkinter.ttk import Notebook, Label, Entry, Button, Checkbutton
from tkinter import N,NE,NO, W, E, S, CENTER
import os
import re
import json
from pickle import dump, dumps, load, loads
import html
from core.models.clase import Clase
from core.models.entry_with_placeholder import EntryWithPlaceholder
from features.file_generator.domain.use_cases.file_generator_use_case import CodeGeneratorUseCase
# from core.models.attribute import  Attribute

from core.models.poo import Attribute, Class
from core.widgets.container_widget import ContainerWidget
from features.file_generator.access.tkinter.view.edit_token_view import WindowEditToken
from features.file_generator.access.tkinter.view.widgets.tabs_widget import TabsWidget
from features.file_generator.access.tkinter.view.widgets.left_panel_widget import LeftPanelWidget
from core.helpers.token_extractor.tokens_extractor import TokensExtractor
BASE_STRUCTURE = 'base_structure'

class IndexView(Window,ContainerWidget):

    def __init__(self, width, height):
        Window.__init__(self, width, height)
        ContainerWidget.__init__(self)

        
        self.svLanguage = StringVar()
        self.svLanguage.set("")

        self.class_definition = Class()

        # self.items = 0
        # self.itemsObjects = []

        self.sv_files = {}

        self.files = {}

        self.functions_buttons = []

        self.create_tab_panel()
        self.create_config_panel()
        # self.create_header()
        # self.crearFormularioAttributes()
        # self.crearPanelSeleccion()
        # self.create_main_buttons()

        extractor = TokensExtractor()
        self.generadorArchivos = CodeGeneratorUseCase(extractor)

    def get_base_structure_files(self,path):
        """
            Get all files inside the base structure folder, and create a array
            with the control variables for each file.
        """
        archivos = os.listdir("{}".format(path))
        for arc in archivos:
            self.sv_files[arc] = IntVar()
            self.files[arc] = path+'/'+arc
            self.sv_files[arc].set(1)

    def get_path_template(self):
        file_path_string = filedialog.askdirectory()
        self.paths[0].set(file_path_string)
        self.get_base_structure_files(file_path_string)
        self.create_files_items(self.components['general_panel'])
    
    def get_path_tokens(self):
        file_path_string = filedialog.askopenfilename()
        self.paths[1].set(file_path_string)

    def get_path_paths(self):
        file_path_string = filedialog.askopenfilename()
        self.paths[2].set(file_path_string)

    def create_tab_panel(self):
        self.components['notebook'] = LeftPanelWidget(self.window)
        self.components['notebook'].grid(row=0,column=0,sticky=W)


    def create_config_panel(self):
        self.components['general_panel'] = Frame(self.window)
        self.components['inputs_panel'] = Frame(self.components['general_panel'])

        self.create_main_buttons()


        self.components['general_panel'].config(bg="gray")  
        self.paths = [StringVar(),StringVar(),StringVar()]
        self.create_panel_routes_configuration(self.components['inputs_panel'],"Templates",None,0)
        self.create_panel_routes_configuration(self.components['inputs_panel'],"Tokens",None,1)
        self.create_panel_routes_configuration(self.components['inputs_panel'],"Paths",None,2)

        self.components['inputs_panel'].grid(column=0,row=1,sticky=N+S)
        self.components['general_panel'].grid(column=1,row=1,sticky=N+S)

    def create_panel_routes_configuration(self,general_panel,text,func,index):
        functions = [self.get_path_template,self.get_path_tokens,self.get_path_paths]
        panel_templates = Frame(general_panel)
        image = PhotoImage(file="assets/images/class.png")
        Button(panel_templates, text=text, image = image, command = functions[index], compound=LEFT ).grid(column=0,row=0,sticky=W,ipadx=10)
        Entry(panel_templates, textvariable = self.paths[index], width= 50).grid(column=1,row=0,sticky=W,ipadx=30)
        panel_templates.grid(column=0,row=index,sticky=N+S,padx=5,pady=5)

    def create_files_items(self,parent):
        frame = Frame(parent)
        for f in  self.sv_files.keys():
            Checkbutton(frame, text=self.files[f], variable=self.sv_files[f]).grid()
        frame.grid()
    

    def create_main_buttons(self):
        self.components['buttons_frame_widgets'] = Frame(self.components['general_panel'])
        Button(self.components['buttons_frame_widgets'],  command=self.generate_files, text="Generate").grid()
        self.components['buttons_frame_widgets'].grid(column=0,row=0,pady = 10)


    def generate_files(self):
        self.class_definition.from_json(self.components['notebook'].get_class_representation())
        tokens_functions = self.paths[1].get()
        routes =  self.paths[2].get()
        print(tokens_functions)
        print(routes)
        # tokens_functions = 'implementations/functions_tokens_config.json'
        # routes = 'implementations/path_config_tokens.json'
        config = 'gca.config.json'
        if(tokens_functions != '' and len(self.sv_files.keys()) > 0 and routes != ''):
            # print(tokens_functions)

            #Las funciones de tokens son
            with open(tokens_functions,'r') as tokens:
                functions_tokens = json.load(tokens)

            #El mapper de las rutas
            with open(routes,'r') as tokens:
                routes_definition = json.load(tokens)
            
            #El mapper de las rutas
            with open(config,'r') as tokens:
                config_definition = json.load(tokens)

            #Run pre scripts
            # 
            path_scripts = 'implementations/scripts.json'
            with open(path_scripts,'r') as target:
                content = target.read()
                json_content = json.loads(content)
                pre_commands = json_content['pre']
                post_commands = json_content['post']

            for pre_command in pre_commands:
                content = self.generadorArchivos(self.class_definition, pre_command,functions_tokens)
                os.system(content)        
            for f in self.sv_files.keys():
                if(self.sv_files[f].get() == 1):
                    with open(self.files[f],'r') as archivo:
                        content = self.generadorArchivos(self.class_definition, archivo.read(),functions_tokens)
                        final_route = self.generadorArchivos(self.class_definition, (routes_definition)[f],functions_tokens)
                        final_route_file = self.generadorArchivos(self.class_definition, f,functions_tokens)
                        self.make_files_in_route(
                            content,
                            (config_definition)['base'],
                            final_route,
                            final_route_file)
            #Run post scripts
            for post_command in post_commands:
                content = self.generadorArchivos(self.class_definition, post_command,functions_tokens)
                os.system(content)    
            print('done')
    def make_files_in_route(self,content,base_route,route,name_file):
        self.crearDirectorio(base_route,route)
        path = base_route+'/'+route+'/'+name_file
        with open(path,'w') as file:
            file.write(content)
    
    def formatearRuta(self, ruta, bo=False):
        if bo:
            return ruta.replace("\\", "/")
        else:
            return ruta.replace("/", "\\")

    def crearDirectorio(self, rutaRel,rutaDestino):
        rutaDestino = self.formatearRuta(rutaDestino, True)
        fragmentos = rutaDestino.split("/")
        for frag in fragmentos:
            try:
                os.mkdir(rutaRel+"/"+frag)
            except Exception as e:
                pass
            rutaRel += "/"+frag
    
    # def extraerAttributes(self):
    # 	self.update_files()
    # 	self.actualizarCamposPropiedades()
    # 	self.actualizarAttributesPropiedades()

    # def crearFormularioAttributes(self):

    # 	self.frameFormularioAttributes = Frame(
    # 		self.window, height=50, width=self.width-10,  relief=SUNKEN)
    # 	self.frameFormularioAttributes.place(x=5, y=100)

    # 	Label(self.frameEncabezado,
    # 		  text="Se debe especificar las características de los atributos de la entidad a representar").place(x=10, y=10)
    # 	opciones = ["", "+", "-"]
    # 	OptionMenu(self.frameFormularioAttributes,
    # 			   self.svVisibilidad, *opciones).place(x=5, y=20)

    # 	Label(self.frameFormularioAttributes, text="Attribute").place(x=50, y=5)

    # 	entryNombreAttribute = EntryWithPlaceholder(
    # 		self.frameFormularioAttributes, placeholder="Code")
    # 	entryNombreAttribute.configure(textvariable=self.svNombre)
    # 	entryNombreAttribute.place(x=50, y=23)

    # 	Label(self.frameFormularioAttributes,
    # 		  text="Display Name").place(x=180, y=5)

    # 	entryDisplayNameAttribute = EntryWithPlaceholder(
    # 		self.frameFormularioAttributes, placeholder="")
    # 	entryDisplayNameAttribute.configure(textvariable=self.svDisplayName)
    # 	entryDisplayNameAttribute.place(x=180, y=23)

    # 	Label(self.frameFormularioAttributes, text="Campo DB").place(x=310, y=5)

    # 	entryNombreDBAttribute = EntryWithPlaceholder(
    # 		self.frameFormularioAttributes, placeholder="CODIGO")
    # 	entryNombreDBAttribute.configure(textvariable=self.svNombreDB)
    # 	entryNombreDBAttribute.place(x=310, y=23)

    # 	Label(self.frameFormularioAttributes,
    # 		  text="Tipo de dato").place(x=440, y=5)

    # 	entryTipo = Combobox(self.frameFormularioAttributes)
    # 	entryTipo["values"] = ["string", "int",
    # 						   "float", "char", "enum", "double", "bool"]
    # 	entryTipo.config(textvariable=self.svTipo, width="20")
    # 	entryTipo.place(x=440, y=23)

    # 	Checkbutton(self.frameFormularioAttributes, text="G",
    # 				variable=self.svGet).place(x=590, y=23)

    # 	Checkbutton(self.frameFormularioAttributes, text="S",
    # 				variable=self.svSet).place(x=620, y=23)

    # 	Checkbutton(self.frameFormularioAttributes, text="R",
    # 				variable=self.svRequired).place(x=650, y=23)

    # 	Button(self.frameFormularioAttributes, style="SmallGB.TButton",
    # 		   text="+", command=self.agregarAttribute).place(x=700, y=16)

    # 	Button(self.frameFormularioAttributes, style="SmallGB.TButton",
    # 		   text="E", command=self.actualizarAttribute).place(x=750, y=16)

    # def agregarAttribute(self):
    # 	self.items += 1
    # 	self.clase.atributos.append(
    # 		Attribute(
    # 			self.svNombre.get(),
    # 			self.svTipo.get(),
    # 			self.svVisibilidad.get(),
    # 			self.svDisplayName.get(),
    # 			self.svNombreDB.get(),
    # 			self.svGet.get(),
    # 			self.svSet.get(),
    # 			self.svRequired.get()
    # 		)
    # 	)
    # 	self.update_files()

    # def actualizarAttribute(self):
    # 	self.items += 1
    # 	attr = self.clase.searchAttributeObject(self.svNombre.get())

    # 	attr.nombre = self.svNombre.get()
    # 	attr.tipo = self.svTipo.get()
    # 	attr.visibilidad = self.svVisibilidad.get()
    # 	attr.displayName = self.svDisplayName.get()
    # 	attr.nombreDB = self.svNombreDB.get()
    # 	attr.get = self.svGet.get()
    # 	attr.set = self.svSet.get()
    # 	attr.requerido = self.svRequired.get()
  

    # 	self.update_files()

    # def borrarItems(self):
    # 	for obj in self.itemsObjects:
    # 		obj.destroy()
    # 	self.itemsObjects.clear()

    # def crearItems(self):
    # 	i = 0
    # 	for atributo in self.clase.atributos:
    # 		self.crearItem(atributo, i)
    # 		i += 1

    # def crearPanelSeleccion(self):
    # 	y = 160
    # 	widthFrameEx = int(self.width*0.7)
    # 	widthFrame = int(self.width*0.28)
    # 	i = 0
    # 	for archivo in self.sv_files:
    # 		frame = Frame(self.window,  width=widthFrame, height=20)
    # 		frame.place(x=widthFrameEx, y=y+(22*i))
    # 		Checkbutton(frame, text=archivo,
    # 					variable=self.sv_files[archivo]).place(x=4, y=1)
    # 		i += 1

    # def crearItem(self, atributo, i):
    # 	y = 160
    # 	widthFrame = int(self.width*0.65)
    # 	frame = Frame(self.window, style="Blue.TFrame",
    # 				  width=widthFrame, height=30)
    # 	frame.place(x=10, y=y+(40*i))

    # 	Label(frame, style="Blue.TLabel",
    # 		  text=atributo.imprimir()).place(x=10, y=5)
    # 	Button(frame, text="-", command=lambda: self.eliminarAttribute(i),
    # 		   style="SmallRB.TButton").place(x=widthFrame-45, y=5)
    # 	Button(frame, text="E", command=lambda: self.editarAttribute(i),
    # 			style="SmallRB.TButton").place(x=widthFrame-80, y=5)
    # 	self.itemsObjects.append(frame)

    # def eliminarAttribute(self, i):
    # 	del self.clase.atributos[i]
    # 	self.items -= 1
    # 	self.update_files()
  
    # def editarAttribute(self, i):
    # 	attr = self.clase.atributos[i]
    # 	self.svNombre.set(attr.nombre)
    # 	self.svTipo.set(attr.tipo)
    # 	self.svVisibilidad.set(attr.visibilidad)
    # 	self.svDisplayName.set(attr.displayName)
    # 	self.svNombreDB.set(attr.nombreDB)
    # 	self.svGet.set(attr.get)
    # 	self.svSet.set(attr.set)
    # 	self.svRequired.set(attr.requerido)

    # 	self.update_files()
