"""
Given a position of a knight on the standard chessboard, find the number of cells which the knight can attack from that cell.

Example

for "a1" output should be 2
for "c2" output should be 6
[input] string cell

String consisting of 2 letters - chess-notation of a cell in 8x8 chessboard (lowercase Latin letter a-h followed by a number 1-8)
[output] integer

"""

def chessKnight(cell):
    row = ord(cell[1]) - ord('0')
    column = ord(cell[0]) - ord('a') + 1
    steps = [
            [-2, -1], [-1, -2], [1, -2], [2, -1],
            [2, 1], [1, 2], [-1, 2], [-2, 1]
            ]
    answer = 0

    for i in range(len(steps)):
        tmpRow = row + steps[i][0]
        tmpColumn =  column + steps[i][1] 
        if (tmpRow >= 1 and tmpRow <= 8 and
            tmpColumn >= 1 and tmpColumn <= 8):
            answer += 1

    return answer