from sys import stdout
from time import sleep 
lyrics = (
    ["Esto es una prueba", 0.13],
    ["Esto sera una prueba?", 0.14],
    ["Esto SI es una prueba", 0.18]
)

delay = (0.5, 0.8, 1)
for pos, (letras, tiempo) in enumerate(lyrics):
    for i in letras:
        print(i, end="")
        stdout.flush()
        sleep(tiempo)
    sleep(delay[pos])
    print("")