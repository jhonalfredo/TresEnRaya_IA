import  random
from FuncionJuego import Pos, Jugador, Juego, Jugadores

class Generador:

    def __init__(self, tablero,turno,lista):
        for i in range(3):
            for j in range(3):
                self.tableroValor[i][j]= tablero[i][j]
        self.turno = turno
        self.listaGrande = lista

    def __str__(self):
        return ""

    listaGrande = []
    turno = 1;    # si es 1 sera el turno de  player1 , 0 es el turno de player2
    resultado = -1 ;  # cuando se a -1 la partida aun no termina , 1 caundo ganan , 0 cuando es empate

    tableroValor = [['', '', ''],
                    ['', '', ''],
                    ['', '', '']]
    historialPasos =[]

    def generarJugandas(self ,historial):
        listaValores = []
        for i in range(len(historial)):
            listaValores.append(historial[i])
        if (self.verificarEsdadoJuego("x") == 1):
            listaEscritura = ["player1", listaValores, 1, "player1"]
            self.listaGrande.append(listaEscritura)
            return;
        if (self.verificarEsdadoJuego("o") == 1):
            listaEscritura = ["player1", listaValores, 1, "player2"]
            self.listaGrande.append(listaEscritura)
            return;
        if (self.verificarEsdadoJuego("o") == 0):
            listaEscritura = ["player1", listaValores, 0, "empate"]
            self.listaGrande.append(listaEscritura)
            return;

        if self.turno:
            pos = self.buscarJuagadaGanadora("x")
            if  pos != None:
                historialCopia = []
                for j in range(len(historial)):
                    historialCopia.append(historial[j])
                historialCopia.append(self.tranformarANumero(pos.x, pos.y))
                self.tableroValor[pos.x][pos.y] = "x"
                (Generador(self.tableroValor, not self.turno, self.listaGrande)).generarJugandas(historialCopia);
                self.tableroValor[pos.x][pos.y] = ""
                return
        else:
            pos = self.buscarJuagadaGanadora("o")
            if pos != None:
                historialCopia = []
                for j in range(len(historial)):
                    historialCopia.append(historial[j])
                historialCopia.append(self.tranformarANumero(pos.x, pos.y))
                self.tableroValor[pos.x][pos.y] = "o"
                (Generador(self.tableroValor, not self.turno, self.listaGrande)).generarJugandas(historialCopia);
                self.tableroValor[pos.x][pos.y] = ""
                return

        for i in range(1,10):
            aux = self.tranformarAPos(i)
            if self.tableroValor[aux.x][aux.y] == "":
                historialCopia = []
                for j in  range(len(historial)):
                    historialCopia.append(historial[j])
                historialCopia.append(self.tranformarANumero(aux.x,aux.y))
                if self.turno:
                    self.tableroValor[aux.x][aux.y] = "x"
                    (Generador(self.tableroValor,not self.turno,self.listaGrande)).generarJugandas(historialCopia);
                else:
                    self.tableroValor[aux.x][aux.y] = "o"
                    (Generador(self.tableroValor, not self.turno, self.listaGrande)).generarJugandas(historialCopia);
                self.tableroValor[aux.x][aux.y] = ""

    def verificarEsdadoJuego(self,simbolo):
        for i in range(3):
            if (self.tableroValor[i][0] == self.tableroValor[i][1] == self.tableroValor[i][2]) and self.tableroValor[i][0] == simbolo:
                return 1
            elif (self.tableroValor[0][i]) == (self.tableroValor[1][i]) == (self.tableroValor[2][i]) and self.tableroValor[0][i] == simbolo:
                return 1
        if (self.tableroValor[0][0]) == (self.tableroValor[1][1]) == (self.tableroValor[2][2]) and self.tableroValor[0][0] == simbolo:
            return 1
        elif (self.tableroValor[0][2]) == (self.tableroValor[1][1]) == (self.tableroValor[2][0]) and  self.tableroValor[0][2] == simbolo:
            return 1
        for i in range(3):
            for j in range(3):
                if self.tableroValor[i][j] == "":
                    return -1
        return 0
    def tranformarAPos(self,valor):
        aux = [['1', '2', '3'],
                        ['4', '5', '6'],
                        ['7', '8', '9']]
        for i in range(3):
            for j in range(3):
                if valor == int(aux[i][j]):
                    return Pos(i,j)
        return  None

    def tranformarANumero(self,x,y):
        aux = [['1', '2', '3'],
                        ['4', '5', '6'],
                        ['7', '8', '9']]
        return  aux[x][y]

    def buscarJuagadaGanadora(self, simbolo):  # se bucara si el "playes" esta apunto de conectar 3 puntos asi que  devolveremos una posicion para que no lo logre
        cantRepetisiones = 0
        posLibre = None;
        for i in range(3):
            cantRepetisiones = 0
            posLibre = None;
            for j in range(3):
                if self.tableroValor[i][j] == simbolo:
                    cantRepetisiones = cantRepetisiones + 1
                elif len(self.tableroValor[i][j]) == 0:
                    posLibre = Pos(i, j)
            if cantRepetisiones > 1 and posLibre != None:
                return posLibre
            cantRepetisiones = 0
            posLibre = None;

            for j in range(3):
                if self.tableroValor[j][i] == simbolo:
                    cantRepetisiones = cantRepetisiones + 1
                elif len(self.tableroValor[j][i]) == 0:
                    posLibre = Pos(j, i)
            if cantRepetisiones > 1 and posLibre != None:
                return posLibre

        cantRepetisiones = 0
        posLibre = None;

        for i in range(3):
            if self.tableroValor[i][i] == simbolo:
                cantRepetisiones = cantRepetisiones + 1
            elif len(self.tableroValor[i][i]) == 0:
                posLibre = Pos(i, i)
        if cantRepetisiones > 1 and posLibre != None:
            return posLibre
        cantRepetisiones = 0
        posLibre = None;
        for i in range(3):
            if self.tableroValor[i][2 - i] == simbolo:
                cantRepetisiones = cantRepetisiones + 1
            elif len(self.tableroValor[i][2 - i]) == 0:
                posLibre = Pos(i, 2 - i)
        if cantRepetisiones > 1 and posLibre != None:
            return posLibre
        return None

