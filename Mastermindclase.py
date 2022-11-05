import random

from MasterMind01 import MasterMindGame

validColors = 'rgybkw'

m1 = MasterMindGame ()
m2 = MasterMindGame (validColors)
m3 = MasterMindGame ('iiii')

print('clave secreta por defecto:', m1.secretCode)

print('clave secreta valid colors:', m2.secretCode)

print('clave secreta ¿Pero esto qué es?, Toma una combi válida:', m3.secretCode)

validColors = 'rgybkw'

print ('Combinación aleatoria random choices', random.choices('rgbky'))

secretCode = random.choices(validColors, k=4)

print(mm.toMasterMindColorCombination)












    self.MMC["white"] = "⚪"

def randomCode(self, n: int) -> list: #Genera un código aleatorio

    colorsList = list(self.validColors)
    passCode = random.choices(colorsList, k=n)

    return self.toMasterMindColorCombination(passCode)

def MasterMindColor(self, color: str): #Convertir cadenas en colores