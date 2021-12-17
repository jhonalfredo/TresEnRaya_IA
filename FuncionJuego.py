class Pos:
    tableroValor = [['1', '2', '3'],
                    ['4', '5', '6'],
                    ['7', '8', '9']]
    posicionesGanadoras = [['1', '2', '3'], ['1', '4', '7'], ['1', '5', '9'], ['2', '5', '8'], ['3', '6', '9'],
                           ['3', '5', '7'], ['4', '5', '6'], ['7', '8', '9']]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.valor = self.tableroValor[x][y]

    def __str__(self):
        valor = "(" + str(self.x) + "," + str(self.y) + ")"
        return valor

    def getPosicionesGanadoras(self):
        self.res = []
        for i in range(len(self.posicionesGanadoras)):
            if self.valor in self.posicionesGanadoras[i]:
                self.res.append(self.posicionesGanadoras[i])
        return self.res


class Jugador:

    def __init__(self, nombre, ficha, miTurno):
        self.nombre = nombre
        self.ficha = ficha
        self.miTurno = miTurno

    def __str__(self):
        return "Nombre: " + self.nombre + ", Ficha: " + self.ficha + ", Turno: " + str(self.miTurno)


class Jugadores:
    def __init__(self, j1, j2):
        self.j1 = j1
        self.j2 = j2

    def __str__(self):
        return "JUGADOR1: " + str(self.j1) + "\nJUGADOR2: " + str(self.j2)

    def cambiarTurnos(self):
        self.j1.miTurno = not self.j1.miTurno
        self.j2.miTurno = not self.j2.miTurno

    def getJugadorTurno(self):
        if self.j1.miTurno:
            return self.j1
        else:
            return self.j2

    def getJugadorNoTurno(self):
        if self.j1.miTurno:
            return self.j2
        else:
            return self.j1


class Juego:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.tablero = [['-', '-', '-'],
                        ['-', '-', '-'],
                        ['-', '-', '-']]
        self.finalizo = False
        self.tipoFin = -1

    def imprimirTablero(self):
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[0])):
                print(self.tablero[i][j], end="")
            print()

    def getPosicion(self, numero):
        tableroValor = [['1', '2', '3'],
                        ['4', '5', '6'],
                        ['7', '8', '9']]
        for i in range(len(tableroValor)):
            for j in range(len(tableroValor[0])):
                if (tableroValor[i][j] == numero):
                    return Pos(i, j)
        return None

    def getNumeroFromPos(self, pos):
        tableroValor = [['1', '2', '3'],
                        ['4', '5', '6'],
                        ['7', '8', '9']]
        return tableroValor[pos.x][pos.y]

    def seTieneGanador(self, posicionesGanadoras, pos, ficha):
        hayGanador = False
        for i in range(len(posicionesGanadoras)):
            cont = 0
            for j in range(len(posicionesGanadoras[0])):
                aux = posicionesGanadoras[i][j]
                if (pos.valor != aux):
                    auxPos = self.getPosicion(aux)
                    if (self.tablero[auxPos.x][auxPos.y] == ficha):
                        cont = cont + 1
            if (cont == 2):
                hayGanador = True
        return hayGanador

    def seTieneEspacio(self):
        espacio = False
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[0])):
                if (self.tablero[i][j] == '-'):
                    espacio = True
        return espacio

    def marcarJugada(self, pos):
        if self.tablero[pos.x][pos.y] == '-':
            self.tablero[pos.x][pos.y] = self.jugadores.getJugadorTurno().ficha
            espacio = self.seTieneEspacio()
            ganador = self.seTieneGanador(pos.getPosicionesGanadoras(), pos, self.jugadores.getJugadorTurno().ficha)
            if ganador:
                self.finalizo = True
                self.tipoFin = 1
            elif not espacio:
                self.finalizo = True
                self.tipoFin = 0
            else:
                self.jugadores.cambiarTurnos()

            return True
        else:
            return False
