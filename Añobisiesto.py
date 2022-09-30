
def esBisiesto (n):

    


print(f"400 Sí es bisiesto 400%4: {400%4}")
print(f"1000 No es bisiesto 1000%100: {1000%100}")
print(f"1000 Sí es bisiesto 4000%400: {4000%400}")

print(esBisiesto(2022)) #False
print(esBisiesto(2021)) #False
print(esBisiesto(2020)) #True
print(esBisiesto(2019)) #False
print(esBisiesto(400))  #True
print(esBisiesto(1000)) #False
print(esBisiesto(4000)) #True