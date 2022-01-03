from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from FuncionJuego import Pos, Jugador, Juego, Jugadores
import random
import  EstadisticaJugadas as estadistica
from GeneradorJugadas import Generador

ventana = Tk()
ventana.title("Tres en raya")
ventana.resizable(0, 0)
ventana.config(bg="#3c3f41")
frameCuadros = Frame(width=300, height=300)
frameCuadros.place(x=25, y = 30)
frameBotones = Frame(width=140, height=40)
frameBotones.place(x=100,y=360)
frameBotones.config(bg="#3c3f41")

listaBotones = [[None, None, None], [None, None, None], [None, None, None]]
estadoTablero = []
tableroValor = [['1', '2', '3'],
                ['4', '5', '6'],
                ['7', '8', '9']]
listaGrande = []
g = Generador([['', '', ''],
                    ['', '', ''],
                    ['', '', '']],1,listaGrande)
g.generarJugandas([])
print("termiando historial")
print("Todal de jugadas generadas: " + str(len(listaGrande)))

valor = None
jugadores = None
juego = None

# -------------- METODOS  -----------------
def metodoBoton(i, j):
    if juego.tipoFin >= 0:
        messagebox.showinfo(message="El juego ya termino , tiene que reiniciarlo ",title="Mensaje")
        return

    b = listaBotones[i][j]
    if  valor==None or jugadores == None or juego == None:
        return

    if len(b['text']) == 0:
        if jugadores.j1.miTurno:
            b.config(text="x")
            juego.marcarJugada(Pos(i,j))
            estadoTablero.append(tableroValor[i][j])
            if juego.tipoFin == -1:
                 #posicion = Pos(random.randint(0, 2), random.randint(0, 2))
                posicion = estadistica.getJugada(1, estadoTablero, listaGrande)
                res = juego.marcarJugada(posicion)

               # while not res:
                    #posicion = Pos(random.randint(0, 2), random.randint(0, 2))
                #    posicion = estadistica.getJugada(1, estadoTablero, listaGrande)
                 #   res = juego.marcarJugada(posicion)
                b = listaBotones[posicion.x][posicion.y]
                b.config(text="o")
                estadoTablero.append(tableroValor[posicion.x][posicion.y])

    else:
        print("esta casilla ya esta marcada")


    if (juego.tipoFin == 0):
        messagebox.showinfo(message="La partida termino en empate !!!!!!!!! ",title="Mensaje")
        print("Empataron")
        #reiniciar()
        return
    elif (juego.tipoFin == 1):
        for i in range(3):
            if (listaBotones[i][0])['text'] == (listaBotones[i][1])['text'] == (listaBotones[i][2])['text']:
                pintar(Pos(i,0),Pos(i,1),Pos(i,2))
                break
            elif (listaBotones[0][i])['text'] == (listaBotones[1][i])['text'] == (listaBotones[2][i])['text']:
                pintar(Pos(0, i), Pos(1, i), Pos(2, i))
                break
        if (listaBotones[0][0])['text'] == (listaBotones[1][1])['text'] == (listaBotones[2][2])['text']:
            pintar(Pos(0, 0), Pos(1, 1), Pos(2, 2))
        elif (listaBotones[0][2])['text'] == (listaBotones[1][1])['text'] == (listaBotones[2][0])['text']:
            pintar(Pos(0, 2), Pos(1, 1), Pos(2, 0))
        messagebox.showinfo(message="El ganador de esta partida es " + str(juego.jugadores.getJugadorTurno().nombre), title="Mensaje")
        print("El ganador es: " + str(juego.jugadores.getJugadorTurno().nombre))
        #reiniciar()
        return


def pintar(pos1,pos2,pos3):
    (listaBotones[pos1.x][pos1.y]).config(fg="lightgreen");
    (listaBotones[pos2.x][pos2.y]).config(fg="lightgreen");
    (listaBotones[pos3.x][pos3.y]).config(fg="lightgreen");


def reiniciar():
    global valor
    global jugadores
    global juego
    global estadoTablero
    estadoTablero = [];
    valor = random.randint(0, 1) == 0
    # jugadores = Jugadores(Jugador("Jhon", "x", valor), Jugador("IA", "o", not valor))
    jugadores = Jugadores(Jugador("Jhon", "x", 0), Jugador("IA", "o",  1))
    juego = Juego(jugadores)

    for i in range(3):
        for j in range(3):
            listaBotones[i][j].config(text="");
            listaBotones[i][j].config(fg="#c4c4c4");
    if jugadores.j2.miTurno:
        #posicion = Pos(random.randint(0, 2), random.randint(0, 2))
        posicion = estadistica.getJugada(1, estadoTablero, listaGrande)
        res = juego.marcarJugada(posicion)
        while not res:
            #posicion = Pos(random.randint(0, 2), random.randint(0, 2))
            posicion = estadistica.getJugada(1,estadoTablero,listaGrande)
            res = juego.marcarJugada(posicion)
        b = listaBotones[posicion.x][posicion.y]
        b.config(text="o")
        estadoTablero.append(tableroValor[posicion.x][posicion.y])


def retornarMatriz():
    res = [["", "", ""], ["", "", ""], ["", "", ""]]
    for i in range(3):
        for j in range(3):
            res[i][j] = (listaBotones[i][j])['text'];
    print(res);
    return res

# -------------------------------------------------

# -------- seccion de  creacion de los cuadros----------
pixelVirtual = PhotoImage(width=1, height=1)
fontStyle = tkFont.Font(family="Lucida Grande", size=50)
for i in range(3):
    for j in range(3):
        b1 = Button(frameCuadros, text=" ", font=fontStyle, image=pixelVirtual, width=100, height=100,bg="#23282d",compound="c",
                    borderwidth=3)
        b1.config(command=lambda fila=i, colum=j: metodoBoton(fila, colum),relief="solid")
        b1.place(x=j*100, y=i*100)
        listaBotones[i][j] = b1
# ------------------------------------------------------
# -------- creacion de botones  REINICIAR -------------
fontStyle2 = tkFont.Font(family="Lucida Grande", size=20)
botonReiniciar = Button(frameBotones, text="reiniciar", font=fontStyle2, image=pixelVirtual, width=120, height=25,
                        border=5,compound="c",fg="#99c787",bg="#303841");
botonReiniciar.config(command=lambda: reiniciar())
botonReiniciar.place(x=0, y=0)
# ------------------------------------------------------

# ---------------- PONER VENTNA AL CENTRO -----------------------
window_height = 430
window_width = 350
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
ventana.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
# ------------------------------------------------------

reiniciar()
ventana.mainloop()