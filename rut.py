rut = input("INGRESE RUT ")


fact = []
for digito in rut:                              #Indexa cada elemento de la variable rut, el indice se convierte en un entero para luego insertarlo en una lista nueva
    fact.append(int(digito))                   


real_rut = []                                   #########################
for i in range(len(rut)):                       #Invierte la lista sin reverse()
    real_rut.append(fact[len(rut) - 1 - i])     #########################

mult = 2
counter = 0
for i in real_rut:
    if mult >= 8: mult = 2
    i = i * mult
    real_rut[counter] = i
    counter += 1
    mult += 1

result = 0
for i in real_rut: result += i
result = abs(abs((int(result / 11) * 11) - result) - 11)
print(result)
