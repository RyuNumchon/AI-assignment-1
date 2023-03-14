# CSS324 Homework Assignment 1

## Problem 1

(5 points)

To conduct A* search on the eight-puzzle problem, the heuristic function h2 is
defined by finding the sum of the Manhattan distances between each number’s
current location to its goal location. Implement the function `h2` in
`problem-1/eight_puzzle.py` so that an A* graph search can be properly conducted using
the h2 heuristic function (`problem-1/asg_eight_puzzle.py`). 

## Problem 2

(5 points)

A puzzle called **Moving Magic Square** is played on a 3x3 table containing
each of the numbers 1 to 9. The number 9 is the **movable number**. We can move
9 in four directions by swapping it with the number in that direction. All actions cost 1. 
The initial state is shown in the table below. The goal of this puzzle is to move
9 to reach a state such that the sum of the three numbers on every row, column,
and diagonal is 15. 

```
+---+---+---+
| 6 | 9 | 8 |
+---+---+---+
| 7 | 1 | 3 |
+---+---+---+
| 2 | 5 | 4 |
+---+---+---+
```

There are multiple states that satisfy the goal test. The search can stop when
the first goal state is reached. 

Complete `problem-2/moving_magic.py` so that a uniform-cost graph search can be properly conducted (`problem-2/ucgs_moving_magic.py`)

(Source: http://www.cs.cornell.edu/courses/cs4700)

## Problem 3 (Extra Credits, Optional)

(3 points)

Prove that the heuristic function h1 for the eight-puzzle problem studied in the class is consistent.
For this problem, write a prove with detailed explanation and add a PDF file into the repo.
