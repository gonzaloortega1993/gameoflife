"""
Conway's Game of Life
---------------------

https://es.wikipedia.org/wiki/Juego_de_la_vida

El "tablero de juego" es una malla formada por cuadrados ("células") que se
extiende por el infinito en todas las direcciones. Cada célula tiene 8 células
vecinas, que son las que están próximas a ella, incluidas las diagonales. Las
células tienen dos estados: están "vivas" o "muertas" (o "encendidas" y
"apagadas"). El estado de la malla evoluciona a lo largo de unidades de tiempo
discretas (se podría decir que por turnos). El estado de todas las células se
tiene en cuenta para calcular el estado de las mismas al turno siguiente.
Todas las células se actualizan simultáneamente.

Las transiciones dependen del número de células vecinas vivas:

* Una célula muerta con exactamente 3 células vecinas vivas "nace" (al turno
  siguiente estará viva).
* Una célula viva con 2 ó 3 células vecinas vivas sigue viva, en otro caso
  muere o permanece muerta (por "soledad" o "superpoblación").
"""

def main():
    """
    Función principal del programa. Crea el estado inicial de Game of LIfe
    y muestra la simulación paso a paso mientras que el usuaio presione
    Enter.
    """
    life = life_crear([
        '..........',
        '.#.....#.#',
        '..#....#..',
        '...#.####.',
        '...#...#..',
        '...###....',
        '...#...#..',
        '..#......#',
    ])
    while True:
        for linea in life_mostrar(life):
            print(linea)
        print()
        input("Presione Enter para continuar, CTRL+C para terminar")
        print()
        life = life_siguiente(life)

#-----------------------------------------------------------------------------

def life_crear(mapa):
    """
    Crea el estado inicial de Game of life a partir de una disposición
    representada con los caracteres '.' y '#'.

    `mapa` debe ser una lista de cadenas, donde cada cadena representa una
    fila del tablero, y cada caracter puede ser '.' (vacío) o '#' (célula).
    Todas las filas deben tener la misma cantidad de caracteres.

    Devuelve el estado del juego, que es una lista de listas donde cada
    sublista representa una fila, y cada elemento de la fila es False (vacío)
    o True (célula).
    """
    life=[]
    for cadena in mapa:
        fila=[]
        for valor in cadena:
            if valor ==".":
                fila.append(False)
            elif valor == "#":
                fila.append(True)
        life.append(fila)
    return life

def pruebas_life_crear():
    """Prueba el correcto funcionamiento de life_crear()."""
    # Para cada prueba se utiliza la instrucción `assert <condición>`, que
    # evalúa que la <condición> sea verdadera, y lanza un error en caso
    # contrario.
    assert life_crear([]) == []
    assert life_crear(['.']) == [[False]]
    assert life_crear(['#']) == [[True]]
    assert life_crear(['#.', '.#']) == [[True, False], [False, True]]

#-----------------------------------------------------------------------------

def life_mostrar(life):
    """
    Crea una representación del estado del juego para mostrar en pantalla.

    Recibe el estado del juego (Trues & Falses) creado con life_crear() y
    devuelve una lista de cadenas (cada caracter debe ser '.' (vacío) o '#' (célula)
    con la representación del tablero para mostrar en la pantalla.
    Cada una de las cadenas representa una fila.
    """
    mostrar = []
    for lista in life:
        fila = ""
        for valor in lista:
            if valor == False:
                fila += "."
            elif valor == True:
                fila += "#"
        mostrar.append(fila)
    return mostrar

def pruebas_life_mostrar():
    """Prueba el correcto funcionamiento de life_mostrar()."""
    assert life_mostrar([]) == []
    assert life_mostrar([[False]]) == ['.']
    assert life_mostrar([[True]]) == ['#']
    assert life_mostrar([[True, False], [False, True]]) == ['#.', '.#']

#-----------------------------------------------------------------------------

def cant_adyacentes(life, f, c):
    '''Recibe una lista de cadenas (life_mostrar) representando el estado del tablero y una posición (f y c).
    Calcula la cantidad de celulas vivas al rededor de la posición de la celda. Como el tablero es infinito
    cuando la longitud de life es menor a 9 celdas el tablero se espeja. 
    Para calcular la cantidad de celulas vivas al rededor de determinada celda accedemos: 
    * Al estado de life[f-1][c-1], life[f-1][c], life[f-1][c_+_1], 
    * Al estado de life[f][c-1], life[f][c_+_1], 
    * Al estado de life[f+1][c-1], life[f+1][c], life[f+1][c_+_1], 

    Por ejemplo si el tablero es generado por life_crear(['.']) todas las celdas seran == None, ya que se replican.
    '''
    
    
    cantidad = 0

    fila_arriba = life[f-1]
    fila_abajo = life[(f+1) % len(life)]
    c_mas1=(c+1) % len(life[0])

    adyacentes = [fila_arriba[c-1], fila_arriba[c], fila_arriba[c_mas1], 
                    life[f][c-1], life[f][c_mas1],
                fila_abajo[c-1], fila_abajo[c], fila_abajo[c_mas1]]

    for celda in adyacentes:
        if celda == True:
            cantidad += 1
    return cantidad

def pruebas_cant_adyacentes():
    """Prueba el correcto funcionamiento de cant_adyacentes()."""
    assert cant_adyacentes(life_crear(['.']), 0, 0) == 0
    assert cant_adyacentes(life_crear(['#']), 0, 0) == 8
    assert cant_adyacentes(life_crear(['..', '..']), 0, 0) == 0
    assert cant_adyacentes(life_crear(['..', '..']), 0, 1) == 0
    assert cant_adyacentes(life_crear(['##', '..']), 0, 0) == 2
    assert cant_adyacentes(life_crear(['##', '..']), 0, 1) == 2
    assert cant_adyacentes(life_crear(['#.', '.#']), 0, 0) == 4
    assert cant_adyacentes(life_crear(['##', '##']), 0, 0) == 8
    assert cant_adyacentes(life_crear(['.#.', '#.#', '.#.']), 1, 1) == 4
    assert cant_adyacentes(life_crear(['.#.', '..#', '.#.']), 1, 1) == 3
    assert cant_adyacentes(life_crear(['...', '.#.', '...']), 1, 1) == 0

#-----------------------------------------------------------------------------

def celda_siguiente(life, f, c):
    """
    Calcula el estado siguiente de la celda ubicada en la fila `f` y la
    columna `c`.

    Devuelve True si en la celda (f, c) habrá una célula en la siguiente
    iteración, o False si la celda quedará vacía.

    * Una célula muerta con exactamente 3 células vecinas vivas "nace" (al turno
    siguiente estará viva).
    * Una célula viva con 2 ó 3 células vecinas vivas sigue viva, en otro caso
    muere o permanece muerta (por "soledad" o "superpoblación").
    """
    celda = life[f][c]
    n = cant_adyacentes(life, f, c)
    if celda == False:
        if n == 3:
            return True
        return False
    if n > 1 and n < 4:
        return True
    return False

def pruebas_celda_siguiente():
    """Prueba el correcto funcionamiento de celda_siguiente()."""
    assert celda_siguiente(life_crear(['.']), 0, 0) == False
    assert celda_siguiente(life_crear(['..', '..']), 0, 0) == False
    assert celda_siguiente(life_crear(['..', '..']), 0, 1) == False
    assert celda_siguiente(life_crear(['##', '..']), 0, 0) == True
    assert celda_siguiente(life_crear(['##', '..']), 0, 1) == True
    assert celda_siguiente(life_crear(['#.', '.#']), 0, 0) == False
    assert celda_siguiente(life_crear(['##', '##']), 0, 0) == False
    assert celda_siguiente(life_crear(['.#.', '#.#', '.#.']), 1, 1) == False
    assert celda_siguiente(life_crear(['.#.', '..#', '.#.']), 1, 1) == True
    assert celda_siguiente(life_crear(['...', '.#.', '...']), 1, 1) == False

#-----------------------------------------------------------------------------

def life_siguiente(life):
    """
    Calcula el siguiente estado del juego.

    Recibe el estado actual del juego (lista de listas de False/True) y
    devuelve un nuevo estado que representa la siguiente iteración según las
    reglas del juego.

    Importante: El "tablero" se considera "infinito": las celdas del borde
    izquierdo están conectadas a la izquierda con las celdas del borde
    derecho, y viceversa. Las celdas del borde superior están conectadas hacia
    arriba con las celdas del borde inferior, y viceversa.
    """
    siguiente = []
    for f in range(len(life)):
        fila = []
        for c in range(len(life[0])):
            fila.append(celda_siguiente(life, f, c))
        siguiente.append(fila)
    return siguiente

#-----------------------------------------------------------------------------

def pruebas():
    """Ejecuta todas las pruebas"""
    pruebas_life_crear()
    pruebas_life_mostrar()
    pruebas_cant_adyacentes()
    pruebas_celda_siguiente()
#pruebas()
main()

