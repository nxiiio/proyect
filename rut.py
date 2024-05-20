try:
    rut = int(input("INGRESE RUT "))
except:
    print("error")

rut = str(rut)
rut_lis = list(rut)
asd = []

for i in range(len(rut)):
    asd.append(rut_lis[len(rut) - 1 - i])


print(asd)
