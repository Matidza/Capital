class ChessGame: 
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.current_player = 'W'

    def print_board(self):
        print('   a b c d e f g h')
        for i in range(8):
            print(f'{8 - i}  ' + ' '.join(self.board[i]))
        print()

    def is_valid_move(self, from_pos, to_pos):
        from_x, from_y = from_pos
        to_x, to_y = to_pos

        if from_x < 0 or from_x > 7 or from_y < 0 or from_y > 7:
            return False
        if to_x < 0 or to_x > 7 or to_y < 0 or to_y > 7:
            return False

        piece = self.board[from_x][from_y]

        # Check if the piece is a pawn
        if piece == 'p':
            if self.current_player == 'W':
                # White pawn can move one step forward or two steps from the starting position
                if from_y == to_y and to_x == from_x - 1 and self.board[to_x][to_y] == ' ':
                    return True
                if from_y == to_y and from_x == 6 and to_x == from_x - 2 and self.board[to_x][to_y] == ' ' and self.board[from_x - 1][to_y] == ' ':
                    return True
            elif self.current_player == 'B':
                # Black pawn can move one step forward or two steps from the starting position
                if from_y == to_y and to_x == from_x + 1 and self.board[to_x][to_y] == ' ':
                    return True
                if from_y == to_y and from_x == 1 and to_x == from_x + 2 and self.board[to_x][to_y] == ' ' and self.board[from_x + 1][to_y] == ' ':
                    return True

        # Add rules for other pieces (e.g., King, Queen, Bishop, Knight, Rook) here

        return False

    def move_piece(self, from_pos, to_pos):
        from_x, from_y = from_pos
        to_x, to_y = to_pos

        if self.is_valid_move(from_pos, to_pos):
            self.board[to_x][to_y] = self.board[from_x][from_y]
            self.board[from_x][from_y] = ' '
            self.current_player = 'W' if self.current_player == 'B' else 'B'
        else:
            print("Invalid move. Try again.")

    def play(self):
        print("Welcome to Python Text Chess!\n")
        self.board[0] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']  # Set the starting position for white pieces
        self.board[1] = ['p' for _ in range(8)]  # Set the starting position for white pawns
        self.board[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']  # Set the starting position for black pieces
        self.board[6] = ['p' for _ in range(8)]  # Set the starting position for black pawns
        self.print_board()

        while True:
            from_pos = input(f"Player {self.current_player}, enter the piece position (e.g., 'e2'): ")
            from_x, from_y = 8 - int(from_pos[1]), ord(from_pos[0]) - ord('a')
            to_pos = input(f"Player {self.current_player}, enter the destination position: ")
            to_x, to_y = 8 - int(to_pos[1]), ord(to_pos[0]) - ord('a')

            self.move_piece((from_x, from_y), (to_x, to_y))
            self.print_board()


if __name__ == "__main__":
    game = ChessGame()
    game.play()
