# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

# Alejandro Ruiz

lim_par_1 = int(input('dime el primer limite : '))
lim_par_2 = int(input('Dime el segundo limite : '))


if lim_par_1 // 2 != 0 and lim_par_1 != 2:
    lim_par_1 += 1


if lim_par_2 < lim_par_1:
    aux = lim_par_1
    lim_par_1 = lim_par_2
    lim_par_2 = limpar

for n in range(lim_par_1, lim_par_2 + 1, 2):
    print(n)
