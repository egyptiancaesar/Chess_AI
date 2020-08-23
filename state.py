import chess

class State(object):
    def __init__(self):
        self.board = chess.Board()

    def edges(self):
        return list(self.board.legal_moves)

    def value(self):
        # add neural network here
        return 1 # all board positions are equal, for now

if __name__ == "__main__":
    s = State()
    print(s.edges())
