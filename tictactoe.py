def TicTacToe(b):
    x,o = 0,0
    for i in b:
        for j in i :
            if j == "x":
                x += 1
            elif j == "o":
                o += 1
    return x==o or x == o+1