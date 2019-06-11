# Game of life / Algoritmos I - UBA

## Simulator of the cellular automaton Conway's Game of Life.


The "board of game" is a matrix formed by squares ("cells") that extends
by the infinit in every direction. Every cell has 8 neighbor cells, 
that are the cells surround it, diagonals included. The cells has two states: 
they are "alive" or "dead". The matrix state evolves evoluciona throught unitys of time
(it could be said by turns). The state of every cell is used for calculate
their state in the next turn. All the cells are refreshed at the same time.

The transitions depends of the number of neighbor alive cells:

*   One dead cell with exactky 3 neighbor alive cells "borns"
    (In the next turn will be alive).
  
*   One alive cell with 2 or 3 neighbor alive cells continue alive,
    in other case dies or stay dead.

