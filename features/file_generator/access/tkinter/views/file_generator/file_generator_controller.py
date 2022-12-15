from tkinter import Canvas, Scrollbar
from tkinter import RIGHT, Y, NW, LEFT
from .imports.file_generator_controller_imports import *


class FileGeneratorController:
    name = 'FileGeneratorView'

    def __init__(self, view):
        self.view = view
        extractor = TokensExtractor()
        self.generadorArchivos = CodeGeneratorUseCase(extractor)
        self.paths = [StringVar(), StringVar(), StringVar()]

        self.class_definition = Class()
        self.sv_files = {}
        self.files = {}

    def get_base_structure_files(self, path):
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
        self.create_files_items(
            self.view.components['{}.general_panel'.format(self.name)])

    def get_path_tokens(self):
        file_path_string = filedialog.askopenfilename()
        self.paths[1].set(file_path_string)

    def get_path_paths(self):
        file_path_string = filedialog.askopenfilename()
        self.paths[2].set(file_path_string)

    def create_panel_routes_configuration(self, text, func, index, color):
        functions = [self.get_path_template,
                     self.get_path_tokens, self.get_path_paths]
        template = {
            'type': Frame,
            'children': [
                {
                    'type': Button,
                    'properties': {
                        'text': text,
                        'command': functions[index],
                        'bg': color,
                        'fg': 'black',
                        'height': '1'
                    },
                    'grid':{
                        'column': 0,
                        'row': 1,
                        'sticky': W,
                        'ipadx': 0,
                    }
                },
                {
                    'type': Entry,
                    'properties': {
                        'textvariable': self.paths[index],
                        'width':70,
                    },
                    'grid':{
                        'column': 0,
                        'row': 0,
                        'sticky': W,
                        'ipadx': 30,
                    }
                }
            ],
            'grid': {
                'column': 0,
                'row': index,
                'sticky': N+S,
                'padx': 5,
                'pady': 5
            }
        }
        return template

    def create_files_items(self, parent):
        frame = Frame(parent)
        color = '#fff'

        scroll = Scrollbar(frame, orient='vertical',)
        scroll.pack(side=RIGHT, fill=Y, expand=False)

        canvas = Canvas(frame, yscrollcommand=scroll.set)
        canvas.config(bg=color)
        canvas.pack()

        scroll.config(command=canvas.yview)

        row = 0
        column = 0
        max_row = 16
        for f in self.sv_files.keys():
            text = (self.files[f].split(
                '/').pop())
            Checkbutton(canvas, text=text, variable=self.sv_files[f], bg=color, fg='black').grid(
                row=row, column=column, sticky=W)
            row += 1
            if(max_row == row):
                column += 1
                row = 0

        frame.pack()

    def generate_files(self):
        self.class_definition.from_json(
            self.view.components['{}.leftPanel'.format(self.name)].get_class_representation())
        tokens_functions = self.paths[1].get()
        routes = self.paths[2].get()
        # tokens_functions = 'implementations/functions_tokens_config.json'
        # routes = 'implementations/path_config_tokens.json'
        config = 'gca.config.json'
        if(tokens_functions != '' and len(self.sv_files.keys()) > 0 and routes != ''):
            # print(tokens_functions)

            # Las funciones de tokens son
            with open(tokens_functions, 'r') as tokens:
                functions_tokens = json.load(tokens)

            # El mapper de las rutas
            with open(routes, 'r') as tokens:
                routes_definition = json.load(tokens)

            # El mapper de las rutas
            with open(config, 'r') as tokens:
                config_definition = json.load(tokens)

            # Run pre scripts
            #
            path_scripts = 'implementations/scripts.json'
            with open(path_scripts, 'r') as target:
                content = target.read()
                json_content = json.loads(content)
                pre_commands = json_content['pre']
                post_commands = json_content['post']

            for pre_command in pre_commands:
                content = self.generadorArchivos(
                    self.class_definition, pre_command, functions_tokens)
                os.system(content)
            for f in self.sv_files.keys():
                if(self.sv_files[f].get() == 1):
                    with open(self.files[f], 'r') as archivo:
                        content = self.generadorArchivos(
                            self.class_definition, archivo.read(), functions_tokens)
                        final_route = self.generadorArchivos(
                            self.class_definition, (routes_definition)[f], functions_tokens)
                        final_route_file = self.generadorArchivos(
                            self.class_definition, f, functions_tokens)
                        self.make_files_in_route(
                            content,
                            (config_definition)['base'],
                            final_route,
                            final_route_file)
            # Run post scripts
            for post_command in post_commands:
                content = self.generadorArchivos(
                    self.class_definition, post_command, functions_tokens)
                os.system(content)
            print('done')

    def make_files_in_route(self, content, base_route, route, name_file):
        self.crearDirectorio(base_route, route)
        path = base_route+'/'+route+'/'+name_file
        with open(path, 'w') as file:
            file.write(content)

    def formatearRuta(self, ruta, bo=False):
        if bo:
            return ruta.replace("\\", "/")
        else:
            return ruta.replace("/", "\\")

    def crearDirectorio(self, rutaRel, rutaDestino):
        rutaDestino = self.formatearRuta(rutaDestino, True)
        fragmentos = rutaDestino.split("/")
        for frag in fragmentos:
            try:
                os.mkdir(rutaRel+"/"+frag)
            except Exception as e:
                pass
            rutaRel += "/"+frag
