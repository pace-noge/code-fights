"""
    Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.
    
    Example
    
    for "A1" and "C3" output should be true,
    for "H1" and "H3" output should be false,
    [input] string cell1
    
    coordinates of the white bishop
    [input] string cell2
    
    coordinates of the black pawn
    [output] boolean
"""

def bishopAndPawn(cell1, cell2):
    return ord(cell1[0]) + ord(str(cell2[1])) == ord(str(cell1[1])) + ord(cell2[0]) or ord(cell1[0]) + ord(str(cell1[1])) ==  ord(cell2[0]) + ord(str(cell2[1]))