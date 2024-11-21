def checkmate(board, Confi):
    
    def find_king(board):
        for r, row in enumerate(board):
            if 'K' in row:
                return r, row.index('K')
        return -1, -1
    
    def check_direction(r, c, dr, dc, board):
        row, col = r, c
        while 0 <= row < len(board) and 0 <= col < len(board[0]):
            row += dr
            col += dc
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                piece = board[row][col]
                if piece != '.':
                    if piece == 'P':
                        if (dr == 1 and dc == 1) or (dr == 1 and dc == -1):
                            return True
                    elif piece == 'R' and (dr == 1 or dr == -1 or dc == 1 or dc == -1):
                        return True
                    elif piece == 'B' and (dr == 1 and dc == 1) or (dr == 1 and dc == -1) or (dr == -1 and dc == 1) or (dr == -1 and dc == -1):
                        return True
                    elif piece == 'Q':
                        return True
                    break
        return False

    board = board.strip().splitlines()

    # Find the King
    king_row, king_col = find_king(board)
    if king_row == -1:
        print("Error: King not found")
        return

    # Check
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in directions:
        if check_direction(king_row, king_col, dr, dc, board):
            print("Success")
            return
    print("Fail")
