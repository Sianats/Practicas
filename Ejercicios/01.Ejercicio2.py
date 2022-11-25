#cuenta cuantas veces aparece cada nombre en la lista y devuelve un diccionario
def countNames(names):
    counter = dict()
    for name in names:
        if name in counter.keys():
            counter[name] = counter[name] + 1
        else:
            counter[name] = 1

    return counter

#llamamos a la función countNames para que cuente los nombres
cNames = countNames(["pedro", "ana", "javier", "ana", "ana", "pablo", "pablo"])

#{'pedro': 1, 'ana': 3, 'javier': 1, 'pablo': 2} es el resultado esperado
print(cNames, 'Es el diccionario resultado de contar los nombres')

#comprobamos que nos devuelve un diccionario de nombres
print(type(cNames), 'Comprobamos que el resultado es de tipo diccionario')

#mostramos el contenido del diccionario con un formato diferente
def printNamesDictionary(names):
    for key, value in names.items():
        print(f"{key} => {value}")

#llamamos a la función printNamesDictionary pasando el diccionario
printNamesDictionary(cNames)

#escribe aquí la función para encontrar el nombre más repetido
#como parámetro de entrada recibe un diccionario: dnames
#y devuelve una tupla (maxn, maxc)
#maxn es el nombre más repetido
#maxc es el número de veces que el nombre está repetido
def maxRepeat(dnames):
    maxc = max(dnames.values())
    maxn = max(dnames, key = dnames.get)
    return (maxn, maxc)

#mostramos el resultado de aplicar la función maxRepeat sobre nuestro diccionario cNames
#el nombre más repetido es Ana que aparece tres veces: ('ana', 3)
print(maxRepeat(cNames), 'Es el nombre más repetido')