t = tokenSTR ="\"\"\nfor atributo in self.clase.atributos:\n\ttokenSTR += '\t\t'+('private' if atributo.visibilidad == '-' else 'public')+' ' +atributo.tipo+' '+(atributo.nombre[0]).lower() +(atributo.nombre[1:]) +';\\n\\n'\n\tif atributo.get == 1 or atributo.set == 1:\n\t\ttokenSTR += '\t\tpublic '+ atributo.tipo+' '+atributo.nombre+'\\n\t\t{\\n'\n\t\ttokenSTR += '\t\t\tget { return ' +(atributo.nombre[0]).lower() +(atributo.nombre[1:]) +'; }\\n' if atributo.get ==1 else ' '\n\t\ttokenSTR += '\t\t\tset { ' +(atributo.nombre[0]).lower() +(atributo.nombre[1:]) +' = value; } \\n' if atributo.set == 1 else ''\n\t\ttokenSTR += '\t\t}\\n\\n'\nself.contenido = self.contenido.replace('{ModelDB}', tokenSTR)"
print(t)
