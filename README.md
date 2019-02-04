# Game of life / Algoritmos I - UBA

## Simulador para el autómata celular Conway's Game of Life.

El "tablero de juego" es una malla formada por cuadrados ("células") que se extiende por el infinito en todas las direcciones.
Cada célula tiene 8 células vecinas, que son las que están próximas a ella, incluidas las diagonales. Las células tienen dos 
estados: están "vivas" o "muertas" (o "encendidas" y "apagadas"). El estado de la malla evoluciona a lo largo de unidades de 
tiempo discretas (se podría decir que por turnos). El estado de todas las células se tiene en cuenta para calcular el estado 
de las mismas al turno siguiente. Todas las células se actualizan simultáneamente.

Las transiciones dependen del número de células vecinas vivas:

Una célula muerta con exactamente 3 células vecinas vivas "nace" (al turno siguiente estará viva).
Una célula viva con 2 ó 3 células vecinas vivas sigue viva, en otro caso muere o permanece muerta (por "soledad" o 
"superpoblación").
Consigna
Se provee una implementación incompleta del Game of Life. El objetivo es completar la implementación en todos los lugares 
donde dice return '???'. Una vez comlpetado, al ejecutar python3 life.py debería verse el funcionamiento del Game of Life.

Notar que el código incluye pruebas utilizando la instrucción de Python assert <condición>, que pueden ser de utilidad para 
entender cuál es el resultado esperado de cada función en diferentes casos. El simulador funcionará sólamente cuando todas 
las pruebas pasen correctamente. No es necesario agregar ni modificar pruebas.
