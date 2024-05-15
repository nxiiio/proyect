import os
pik = 0
ota = 0
pul = 0
ang = 0
total = 0
desc_real = False
while True:
    try:
        print("****************\n*    Bienvenido")
        print(f"* Productos en el carro: {pik + ota + pul + ang}\n*")
        print("* [1] Pikachu Roll $4500\n* [2] Otaku Roll $5000\n* [3] Pulpo Venenoso Roll $5200\n* [4] Anguila Eléctrica Roll $4800")
        print("* [5] Codigo de descuento")
        print("* [6] Pagar")
        seleccion = int(input("****************\n---> "))
    except:
        os.system("cls")
        print("Ocurrio un error, trata de poner numeros")
        continue
    match seleccion:
        case 1:
            os.system("cls")
            print(f"Pikachu Roll añadido al carro")
            pik += 1
            total += 4500
        case 2:
            os.system("cls")
            print("Otaku Roll añadido al carro")
            ota += 1
            total += 5000
        case 3:
            os.system("cls")
            print("Pulpo Venenoso añadido al carro")
            pul += 1
            total += 5200
        case 4:
            os.system("cls")
            print("Anguila Eléctrica añadido al carro")
            ang += 1
            total += 4800
        case 5:
            os.system("cls")
            desc_user = input("Ingrese codigo de descuento\n---> ")
            if desc_user == "soyotaku":
                print("Descuento aplicado!")                             ### Mejorar
                desc_real = True
            else:
                print("Descuento incorrecto o ya usado")

        case 6:
            os.system("cls")
            print("****************************")
            print(f"TOTAL PRODUCTO A COMPRAR: {pik + ota + pul + ang}")
            print("****************************")
            print(f"* Pikachu Roll: {pik}\n* Otaku Roll {ota}\n* Pulpo Venenoso Roll: {pul}\n* Anguila Electrica Roll: {ang}")
            print("****************************")
            print(f"Subtotal a pagar: {total}")
            if desc_real:
                total = total * 1.1
                print("Descuento por codigo: ")          ### Mejorar
        case __:
            print("Numero incorrecto")
