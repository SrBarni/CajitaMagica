import numpy as np

def val_ingreso(inf,sup,error,que):
    n = int(input(que))
    while n < inf or n > sup:
        n = int(input(error))
    return n 

n = val_ingreso(0,50,"error ingrese una cantidad valida: ","¿cuantos alumnos?: ")

A = np.full((n,n),0)
print(A)

nombres = A
c = 1
print(nombres)
for x in range(n):
    nombres[x,0]=(str(input(f"nombre del alumno {c}: ")))
    c += 1

n_nota = 1
for i in range(1,n):
    for j in range(1,3):
        A[i,j] = float(input(f"ingrese nota {n_nota}:\n"))
        n_nota += 1
print(A)