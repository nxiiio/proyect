# En un delivery de Sushi vende 4 tipos de Sushi:
# 1. Pikachu Roll $4500
# 2. Otaku Roll $5000
# 3. Pulpo Venenoso Roll $5200
# 4. Anguila Eléctrica Roll $4800
# La empresa le ha solicitado a usted, que genere una pequeña aplicación en Python para tomar el pedido de un
# cliente el cuál puede ir agregando Rolls a través de un menú uno por uno con solo seleccionar la opción (1 a 4)
# La aplicación debe mostrar en un menú los Rolls que agregará el usuario, esto se debe repetir hasta que el usuario
# decida que su pedido está completo.
# Luego de ello, debe preguntar al usuario si posee un código de descuento. En caso de que posea el código, deberá
# ingresarlo. Si el código ingresado es “soyotaku”, debe realizar un 10% de descuento al total del pedido, en caso
# contrario enviar el mensaje “código no válido” y dar al usuario la opción de reingresar el código o volver al menú
# tecleando “X”
# Una vez realizado los pasos anteriores, debe mostrar el detalle del pedido contabilizando el total de productos y la
# cantidad de cada uno de ellos y si aplica o no el descuento
# *********************




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
        print("Ocurrio un error, trata de poner numeros")
        continue
    match seleccion:
        case 1:
            os.system("cls")
            print(f"---> Pikachu Roll añadido al carro <---")
            pik += 1
            total += 4500
        case 2:
            os.system("cls")
            print("---> Otaku Roll añadido al carro <---")
            ota += 1
            total += 5000
        case 3:
            os.system("cls")
            print("---> Pulpo Venenoso añadido al carro <---")
            pul += 1
            total += 5200
        case 4:
            os.system("cls")
            print(" ---> Anguila Eléctrica añadido al carro <---")
            ang += 1
            total += 4800
        case 5:
            os.system("cls")
            while True:
                desc_user = input("Ingrese codigo de descuento\n[X] Volver al menu de compra \n---> ")
                desc_user.upper()
                if desc_user == "soyotaku" and desc_real == False:
                    os.system('cls')
                    print("**** Descuento aplicado! ****")
                    desc_real = True
                    break
                elif desc_user == 'x':
                    os.system('cls')
                    break
                else:
                    os.system('cls')
                    print("**** Descuento incorrecto o ya usado ****\n")
        case 6:
            os.system("cls")
            print("****************************")
            print(f"TOTAL PRODUCTO A COMPRAR: {pik + ota + pul + ang}")
            print("****************************")
            print(f"* Pikachu Roll: {pik}\n* Otaku Roll {ota}\n* Pulpo Venenoso Roll: {pul}\n* Anguila Electrica Roll: {ang}")
            print("****************************")
            print(f" ---> Subtotal: ${total}")
            if desc_real:
                total = int(total * 0.9)
                print(f" ---> Descuento por codigo: ${int(total * 0.1)}")
            
            seleccion = int(input(f"\n ---> Total a pagar: ${total} <---\n [1] Realizar otro pedido\n [2] Salir\n ---> "))
            if seleccion == 1:
                os.system('cls')
                pik = 0
                ota = 0
                pul = 0
                ang = 0
                total = 0
                    
            elif seleccion == 2:
                    break
        case __:
            os.system("cls")
            print("Numero incorrecto")
    print("")
