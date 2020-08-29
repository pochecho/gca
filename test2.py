contenido = "{CreateCrud}"
nombre = "UNO"
token = ""
atributos = ["Cola", "Pierna"]
visibilidad = "-"
tipo = "String"
requerido = 1
displayName = "Cola"
get = 1
sett = 1
page="TUTU"

func = "tokenSTR = ''\nfor atributo in atributos:\n\ttokenSTR+='\\t\\t\\t\\t\\tdbRecord.'+atributo+' = dbModel.'+atributo+';\\n'"

t = 18.0841666

f = 25.2533333333

print(t-f)