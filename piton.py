import json

def read():
    with open("compras.json", "r") as archibo:
        return json.load(archibo)
    
def search(lista:list, priority:str):
    id_search = int(input("Ingrese ID: "))
    founder = None
    for indx in lista[priority]:
        if indx["id"] == id_search: founder = indx
    return founder


def editar(lista:list, priority:str):
    id_request = search(lista, priority)
    if id_request is not None:
        print("Productos a editar:")
        info = {}
        for pos, indx in enumerate(id_request):
            if indx == "id": continue
            info[pos] = indx
            print(f"{[pos]} {indx.capitalize()}: {id_request[indx].capitalize() if type(id_request[indx]) is str else id_request[indx]}")
        edit_request = int(input("----> "))
        edit_request = info[edit_request]
        print(edit_request)
    else:
        print("ID no encontrado")

lista_compras = read()

editar(lista_compras, "productos")