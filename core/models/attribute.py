
class Attribute:
    def __init__(self, nombre, tipo, visibilidad, displayName, nombreDB, metodoGet=1, metodoSet=1, requerido=1):
        self.visibilidad = visibilidad
        self.nombre = nombre
        self.displayName = displayName
        #Eliminar
        self.nombreDB = nombreDB

        self.features = []

        self.tipo = tipo
        self.get = metodoGet
        self.set = metodoSet
        self.requerido = requerido

    def get_features_by_name(self,index = 0):
        if(len(self.features) > index):
            return self.features[index]
        return ''
    def imprimir(self):
        return self.visibilidad+" "+self.nombre + " ["+self.displayName+" : "+self.nombreDB+"] "+": " + self.tipo + " {" + ("get" if self.get == 1 else "") + " : "+("set" if self.set == 1 else "")+" } " + ("Requerido" if self.requerido == 1 else "No requerido")
