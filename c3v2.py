n1 = float(input("ingresa tu nota: \n"))
n2 = float(input("ingresa tu nota: \n"))
n3 = float(input("ingresa tu nota: \n"))

def promedio(n1, n2, n3):
    promedio = (n1 + n2 + n3 ) / 3
    return promedio

promedioPersonal = promedio(n1, n2, n3)
print("tu promedio es: ", promedioPersonal)