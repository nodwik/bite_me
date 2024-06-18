WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    board = []

    for i in range(size):
        line = ''
        for j in range(size):
            if (i + j) % 2 == 0:
                line += WHITE
            else:
                line += BLACK
        board.append(line)


    #board = []
    #lines = []
    #l1 = ''
    #l2 = ''
    #board_line = ''

    #for i in range(0, size):
    #    if i % 2 == 0:
    #        l1 += WHITE
    #    elif i % 2 != 0:
    #        l1 += BLACK
    #lines.append(l1 + '\n')

    #for i in range(0, size):
    #    if i % 2 == 0:
    #        l2 += BLACK
    #    elif i % 2 != 0:
    #        l2 += WHITE
    #lines.append(l2 + '\n')

    #for i in range(0, size):
    #    if i % 2 == 0:
    #        board_line += lines[0]
    #    elif i % 2 != 0:
    #        board_line += lines[1]
    #board.append(board_line)

    for line in board:
        print(line)





create_chessboard(16)
