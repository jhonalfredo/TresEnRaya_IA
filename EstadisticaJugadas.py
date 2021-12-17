import FuncionJuego as jm
from GeneradorJugadas import Generador
import  random

def getJugada(iniciaIA,estadoTablero,listaGrande):
    historial = listaGrande
    historialIniciIA = [] # jugadas en las que inciar IA (en la lisrta que recibiremos esta con player1)
    historialNoIniciaIA = []
    for i in range(len(historial)):
        if (historial[i])[0] == "player1" and ((historial[i])[3] == "player1" or (historial[i])[3] == "empate")  :
            historialIniciIA.append(historial[i]) # empezamos a guarda las jugada en las que inicia IA y que tambien gane o empate
        else:
            historialNoIniciaIA.append(historial[i])

    listaRefinada = []; # ponemos las jugadas que tenga almenos un paso mas que  el estado de tablero que dimos como parametro
    listaPasosIguales = []; # ponemos las jugadas que sus primeros pasos sean igual que estado de tablermo que pasamos
    if iniciaIA == 1:  # cuando nos dan una estado de tablero en la que inicio IA
        for i in range(len(historialIniciIA)):
            if len((historialIniciIA[i])[1]) > len(estadoTablero):
                listaRefinada.append(historialIniciIA[i])
        for i in range(len(listaRefinada)):
            iguales = 1
            elemento = listaRefinada[i]
            for j in range(len(estadoTablero)):
                if estadoTablero[j] != (elemento[1])[j]:
                    iguales = 0;
                    break;
            if iguales == 1:
                listaPasosIguales.append(elemento)

    listaVictoriasPorCasilla = []
    listaEmpatesPorCasilla = []
    for i in range(9):
        aux1 = []
        aux2 = []
        listaVictoriasPorCasilla.append(aux1)
        listaEmpatesPorCasilla.append(aux2)

    for i in range(len(listaPasosIguales)):
        jugada = listaPasosIguales[i]
        if jugada[3] == "player1":
            (listaVictoriasPorCasilla[int((jugada[1])[len(estadoTablero)])-1]).append(jugada)
        elif jugada[3] == "empate":
            (listaEmpatesPorCasilla[int((jugada[1])[len(estadoTablero)])-1]).append(jugada)

    valor = casillaConMasVictoriasOEmpates(listaVictoriasPorCasilla);
    if valor == 0:
        valor= casillaConMasVictoriasOEmpates(listaEmpatesPorCasilla);
    if valor ==0 :
        valor = 1;  # la usaremos en caso que lista de victorias o empates este vacia
        unico = 0
        while not unico:
            valor = random.randint(1, 9)
            aux = 1
            for i in range(len(estadoTablero)):
                if int(estadoTablero[i]) == valor:
                    aux = 0;
                    break
            unico = aux;
    print("******************************************************************************************************************")
    print("--------------Lista de juagadas con Vitoria")
    for i in range(len(listaVictoriasPorCasilla)):
        print("Casilla: " + str(i+1)+"    Cantidad: "+str(len(listaVictoriasPorCasilla[i])))
    print("--------------Lista de juagadas con Empate")
    for i in range(len(listaEmpatesPorCasilla)):
        print("Casilla: " + str(i+1)+"    Cantidad: "+str(len(listaEmpatesPorCasilla[i])))
    print("--------------Valor elegido: " + str(valor))
    print("******************************************************************************************************************")

    if valor == 1:
        return  jm.Pos(0,0)
    if valor == 2:
        return  jm.Pos(0,1)
    if valor == 3:
        return  jm.Pos(0,2)
    if valor == 4:
        return  jm.Pos(1,0)
    if valor == 5:
        return  jm.Pos(1,1)
    if valor == 6:
        return  jm.Pos(1,2)
    if valor == 7:
        return  jm.Pos(2,0)
    if valor == 8:
        return  jm.Pos(2,1)
    if valor == 9:
        return  jm.Pos(2,2)
    

def  casillaConMasVictoriasOEmpates(lista):
    lisRepetidos = [];
    casillaElegida=-1
    CantCasilla=0
    for i in range(len(lista)):
        if(len(lista[i])) > CantCasilla:
            casillaElegida = i
            CantCasilla=len(lista[i])
    if casillaElegida >= 0:
        for i in range(len(lista)):
            if len(lista[i]) == CantCasilla:
                lisRepetidos.append(i)
    if len(lisRepetidos) > 1:
        casillaElegida = lisRepetidos[random.randint(0,len(lisRepetidos)-1)]
    return casillaElegida+1

'''

listaTotalJugadas = []
var = Generador([['', '', ''],
                    ['', '', ''],
                    ['', '', '']],1,listaTotalJugadas)
var.generarJugandas([])

print(getJugada(1,['5','2','4'],listaTotalJugadas))

#lista = jm.getHistorial(500);
#getJugada(1,['7', '8','9'],lista)
'''