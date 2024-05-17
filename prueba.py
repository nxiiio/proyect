import os
counter_money = 0
while True:
    counter_desc = 0
    print("----- Bienvenido -----\n* Seleccione una opcion.")
    try:
        seleccion = int(input("[1] Auto\n[2] Camioneta\n[3] Camion\n[4] Motocicleta\n----------\n---> "))
        if seleccion == "4125":
            print("Apagando...")
            break
        elif seleccion < 1 or seleccion > 4:
            os.system("cls")
            print("Seleccione una opcion valida.")
            continue
    except:
        print("Ocurrio un error, Intenta poner numeros")
        continue
    os.system("cls")
    while True:
        email = input("Ingrese su correo electronico \n---> ")
        if len(email) < 8 or len(email) > 30:
            os.system("cls")
            print("el correo tiene que tener 8 y 30 caracteres, intente de nuevo.")
            continue
        else:
            os.system("cls")
            break
        
    for i in email:
        if i =="@":
            break
        elif i == "a": counter_desc += 1
        elif i == "z": counter_desc += 0.3
        elif i == "l": counter_desc -= 0.2
        elif i == "b": counter_desc += 0.7
        elif i == "m": counter_desc += 1.3
        elif i == "o": counter_desc -= 0.2
        elif i == "e": counter_desc -= 1
        elif i == "u": counter_desc += 0.5
        elif i == "s": counter_desc -= 1
        elif i == "x": counter_desc += 2
        elif i == "u": counter_desc += 2.1
        elif i == "i": counter_desc += 6
    if counter_desc > 0:
        print(f"Tienes un descuento del {counter_desc}% debido a tu correo!")       #######################
        counter_desc = counter_desc / 100
    while True:
        try:

            money_user = int(input("Ingrese efectivo.\n---- Esta maquina solo acepta montos de $500 y $10000 ----\n---> "))
            if money_user < 500 or money_user > 10000:
                os.system("cls")
                print("Dinero no aceptado")
            else:
                break
        except:
            os.system("cls")
            print("Ocurrio un error.")
    os.system("cls")
    match seleccion:
        case 1:
            if money_user > 1000:
                if counter_desc > 0:
                    money_user = money_user - (1000 * counter_desc)
                    
                else:
                    money_user = money_user - 1000
                    
            else:
                print("Dinero insuficiente, realize otra vez el proceso.")
                continue
        case 2:
            if money_user > 2000:
                if counter_desc > 0:
                    money_user = money_user - (2000 * counter_desc)
                    print(f"Se te ha devuelto {money_user}")
                    
                else:
                    money_user = money_user - 2000
                    
                    
            else:
                print("Dinero insuficiente, Realize otra vez el proceso")
        case 3:
            if money_user > 3000:
                if counter_desc > 0:
                    money_user = money_user - (3000 * counter_desc)
                    
                else:
                    money_user = money_user - 3000
                    
        case 4:
            if money_user > 4000:
                if counter_desc > 0:
                    money_user = money_user - (4000 * counter_desc)
                    
                else:
                    money_user = money_user - 4000

    counter_money += money_user
    print(f"Se te ha devuelto {int(money_user)}")
    print("Se ha imprimido un ticket")
    continue