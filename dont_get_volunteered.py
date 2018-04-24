"""
Don't Get Volunteered!
======================

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies at the same time, after all! In order to make sure that everyone working for her is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called answer(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) src = 19
    (int) dest = 36
Output:
    (int) 1

Inputs:
    (int) src = 0
    (int) dest = 1
Output:
    (int) 3
"""

"""
A position is a two-tuple.
The first coordinate is the row of the position, from the top left.
The second coordiante is the column of the position, from the top left.
It's the same as how we count off rows and columns of elements of a matrix.
The coordinates are one-indexed. It just seemed right.

A google_position is the way Google counts off positions in this challenge.
"""

def google_position_to_position(google_position):
    return(tuple(map(sum, zip(divmod(google_position, 8), (1,1)))))

def position_to_google_position(position):
    return(8 * (position[0]-1) + (position[1]-1))

def is_valid_position(position):
    squares = [(r,c) for r in range(1,9) for c in range(1,9)]
    return(position in squares)

# Given a list of positions, find all the valid moves from that position.
def valid_moves(positions):
    if isinstance(positions, tuple): positions = [positions]
    positions = [p for p in positions if is_valid_position(p)]
    moves = [(x,y) for x in [-1,1,-2,2] for y in [-1,1,-2,2] if abs(x) != abs(y)]
    moves_with_repetitions = [(p[0]+m[0], p[1]+m[1]) for p in positions for m in moves if is_valid_position((p[0]+m[0], p[1]+m[1]))]
    unique_moves = list(set(moves_with_repetitions))
    return(unique_moves)

def answer_acc(positions, dest, acc):
    return(acc if dest in positions else answer_acc(valid_moves(positions), dest, acc+1))
    
def answer(src, dest):
    return(0 if src == dest else answer_acc(google_position_to_position(src), google_position_to_position(dest), 0))



