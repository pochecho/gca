import json
import os
class CodeGeneratorUseCase:
    """docstring for generadorArchivos"""
    def __init__():
        self.content = None

    def __call__(self,model,template,functions):
        """
            The model parameters contains all data from your model, this is the class you are building.
            It is a json
            Example:
            {
                "properties": {
                    "name":"cat"
                },
                "attributes": {
                    "name":"cat"
                }

            }
            The template parameter is the layout to generate new files.
                hola {[griego]}
                hola {[romano]}
        """
        self.content = template
        token_list = self.token_extractor(template)
        for token in token_list:           
            function_to_eval = functions[token]
            try:
                exec(function_to_eval)
            except SyntaxError as identifier:
                print("Error",identifier)
        return self.content
        
    def replace_token(self,name_token,template,function):
        pass
    def __init__(self,token_extractor):
        self.token_extractor = token_extractor


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



    #Este queda pero en realidad es el call de esta clase
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

    def get_snake_content(self,data):
        return data.replace('-','_')
    def get_lower_camel_content(self,data):
        name = data.split('-')
        con = ''.join(list(map(lambda x:x.capitalize(),name[1:] )))
        return name[0]+con
    
    def get_upper_camel_content(self,data):
        name = data.split('-')
        con = ''.join(list(map(lambda x:x.capitalize(),name )))
        return con
    def escribirContenidoArchivoFinal(self, ruta, contenido):
        archivo = open(ruta, "w", encoding="utf-8")
        #contenido = contenido[1:]
        archivo.write(contenido)
        archivo.close()
