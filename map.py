mapa = [0,0,0,1,0,0]
position = 3


while True:
    for i in mapa:
        view = "_"
        if i == 2:
            view = "🚪"
        elif i == 1:
            view = "😒"
        print(view, end=" ")
    
    move = input("\n<----[A] [D]---->\n-> ")
    
    if move == "a":
        mapa[position] = 0
        position -= 1
        mapa[position] = 1

    if position > (len(mapa) - 1):
        position = 0
    elif position < (len(mapa) - 1):
        position = 5
