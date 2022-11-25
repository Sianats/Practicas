# Creo una función con una variable n que será el año a comprobar.

def esBisiesto(n):

  # Declaro la variable sol como booleano para que me devuelva una respuesta de True o False.

  sol = bool

  # Ajusto un bucle que tiene en cuenta la expeción: si un año es multiplo de 100,
  # no es bisiesto a no ser que tambien sea múltiplo de 400.

  if n%400==0:
    sol = True
  else:
    if n%100==0:
      sol = False
    else:
      if n%4==0:
        sol = True
      else:
        sol = False
  return sol

# Pruebo los ejemplos dados en clase con mi función pra que compruebe si son o no bisiestos:

print(esBisiesto(2022)) #False
print(esBisiesto(2021)) #False
print(esBisiesto(2020)) #True
print(esBisiesto(2019)) #False
print(esBisiesto(400))  #True
print(esBisiesto(1000)) #False
print(esBisiesto(4000)) #True