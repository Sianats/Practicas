import random

# esqueleto inicial
class MasterMindGame:
    # declaramos las variables que vamos a utilizar

    MMC = {}  # diccionario de colores válidos.

    secretCode = []  # código secreto que tenemos que adivinar.

    validColors = "rgybkw"  # colores mastermind permitidos

    maxTurns = 10  # máximo número de turnos para acertar la clave.
    currentTurn = 0  # turno actual.

    # construimos la función para iniciar la clase
    def __init__(self, combiCode: str = "nocombiCode"):
        # iniciamos el diccionario de colores
        self.MMC["red"] = "🔴"
        self.MMC["green"] = "🟢"
        self.MMC["yellow"] = "🟡"
        self.MMC["blue"] = "🔵"
        self.MMC["black"] = "⚫"
        self.MMC["white"] = "⚪"

        if combiCode == "nocombiCode":
            self.secretCode = self.randomCode(4)
        else:
            try:
                self.secretCode = self.toMasterMindColorCombination(combiCode)
            except:
                self.secretCode = self.randomCode(4)

    def randomCode(self, n: int) -> list:  # genera un código aleatorio
        
        colorsList = list(self.validColors)
        passCode = random.choices(colorsList, k=n)
        return self.toMasterMindColorCombination(passCode)


    def MasterMindColor(self, color:str):  # convertir cadenas en colores
        if color == 'r' or color == 'R' or color == "🔴":
            rcolor = self.MMC["red"]
        elif color == 'g' or color == 'G' or color == "🟢":
            rcolor = self.MMC["green"]
        elif color == 'y' or color == 'Y' or color == "🟡":
            rcolor = self.MMC["yellow"]
        elif color == 'b' or color == 'B' or color == "🔵":
            rcolor = self.MMC["blue"]
        elif color == 'k' or color == 'K' or color == "⚫":
            rcolor = self.MMC["black"]
        elif color == 'w' or color == 'W' or color == "⚪":
            rcolor = self.MMC["white"]
        else:
            raise KeyError(color)
        return rcolor

    def toMasterMindColorCombination(self, combi:str):  # obtener una cadena de colores mastermind
        return list(map(lambda n: self.MasterMindColor(n), combi))