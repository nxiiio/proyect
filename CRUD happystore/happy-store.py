import json
import os

def opi(p):
    print('*' * 25)
    for pos, i in enumerate(p,start=1):
        print(f'{pos} - {i}')
    print('*' * 25)
    return int(input('---> '))

def read_archive_and_print_archive(yeison, imprimir= False):
    if imprimir == False:
        with open('Ejercicio lala/compras.json', 'r') as archivo:
                dicc = json.load(archivo)
                return dicc
    else:
        with open('Ejercicio lala/compras_nuevo.json', 'w') as archivo:
            json.dump(yeison, archivo, indent=4)

def update(shop, priority, id):
    print('Que quieres modificar?')
    for pos, index in enumerate(shop[priority][0], start=0):
        if index == 'id':
            continue
        print(f'[{pos}] {index.capitalize()}')
    num = int(input('---> '))
    for pos, indx in enumerate(id):
        if num == pos:
            num = indx
    if type(num) == int or num == 'id':
        return print('Error: has ingreso un numero que no existe en las opciones')
    edit = input(f'Dato a modificar:\n{id[num]}\nIngrese nuevo dato: ')
    id[num] = edit if type(id[num]) == str else int(edit)
    print('Dato actualizado!')

def listados(lista, priority, ok_id= None):
    id = int(input('Ingrese ID: ')) if ok_id is None else ok_id
    buscador = 'id_boleta' if priority == 'boletas' else 'id'
    founder = None
    if priority == 'formas_pago':
        founder = 'Forma de pago: Debito' if ok_id == 0 else 'Forma de pago: Credito'
        return  founder
    for index in lista[priority]:
        if id == index[buscador]:
            founder = index
    return founder

def create(shop, priority, id):
    print('Dato a agregar:')
    plantilla = {}
    plantilla['id'] = id
    for index in shop[priority][0]:
        if index == 'id':
            continue
        copia = index
        new = input(f'[{index.capitalize()}] ----> ')
        if type(shop[priority][0][index]) == int:
            new = int(new)
        plantilla[copia] = new
    shop[priority].append(plantilla)
    print('Dato añadido!')

def eliminate(lista, priority, id):
    print(f'Eliminaras:')
    for indx in id:
        print(f'{indx.capitalize()}: {id[indx]}')
    print()
    confirm = int(input('Estas seguro de eliminarlo?\n[1] Si [2] No\n---> '))
    if confirm == 1: 
        lista[priority].remove(id)
        print('Dato eliminado!')
    elif confirm == 2:
        print('Cancelado')
        return
    else:
        print('Error: Opcion incorrecta')

def detalle_boleta(shop, boleta, id_boleta):
    print('--------- Boleta ---------')
    search_json = ('', 'clientes','vendedores','','formas_pago')
    view = ('', 'Cliente', 'Vendedor', '', 'Forma de pago')
    
    for pos, index in enumerate(boleta):
        if index == 'total' or index == 'id_boleta' or search_json[pos] == '':
            continue
        founder = listados(shop,search_json[pos], boleta[index])
        print(f'{view[pos]}:',founder['nombre']) if type(founder) == dict else print(founder.capitalize())

    print('-------- Productos --------')
    for indx in shop['detalle_boletas']:
        if indx.get('id_boleta') == id_boleta:
            print(listados(shop,'productos',indx.get('id_producto'))['nombre'].capitalize())
    else:
        print('-'* 27)


def main():
    opciones = ('Productos', 'Clientes', 'Vendedores', 'Boletas', 'Imprimir JSON')
    opciones_crud = ('Agregar', 'Listado', 'Modificar', 'Eliminar')
    compras = read_archive_and_print_archive(False)
    while True:
        opc = opi(opciones)
        if opc == 5:
            read_archive_and_print_archive(compras, True)
            continue
        for pos, i in enumerate(opciones, start=1):
            if opc == pos:
                opc = i.lower()
                if opc == 'boletas': detalle_boletas = 'detalle_boletas'
        if type(opc) == int:
            print('Error: Opcion no existe')
            continue
        opc2 = opi(opciones_crud)

        if opc2 == 1:
            Id_create = int(input('Ingrese ID: '))
            if Id_create <= 0:
                print('Error: El ID tiene que ser un numero positivo mayor a 0')
                continue

            if listados(compras.copy(), opc, Id_create) is None:
                create(compras, opc, Id_create)
            else:
                print('Error: Ya existe ese ID')
                continue
        elif opc2 == 2:
            id = int(input('Ingrese ID: '))
            request = listados(compras.copy(), opc, id)
            if request is not None:
                if opc == 'boletas':
                    detalle_boleta(compras, request, id)
                else:
                    for indx in request:
                        print(f'{indx.capitalize()}: {request[indx]}')
            else:
                print('Error: ID no encontrado')
        elif opc2 == 3:
            if opc == 'boletas':
                print('Error: Las boletas no se pueden modificar')
                continue
            request = listados(compras.copy(), opc)
            update(compras, opc, request)
        elif opc2 == 4:
            id_eliminate = listados(compras,opc)
            if id_eliminate is not None:
                eliminate(compras, opc, id_eliminate)
            else:
                print('Error: El ID ingresado no existe')



main()

