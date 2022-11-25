# Escribe aquí tu código
def gcd(x, y):
    #condición de parada
    a = max(x,y)
    b = min(x,y)
    r = a-b
    while r !=0:
        r = a-b
        if (r !=0):
            a = max(b,r)
            b = min(b,r)
    #llamada recursiva
    return b

#casos de prueba
print(gcd(270,192)) # 6

print(gcd(9, 6)) # 3

print(gcd(30, 75)) # 15

print(gcd(2366, 273)) #91