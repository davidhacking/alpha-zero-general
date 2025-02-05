import time

class PaceIns:
    _instance = None
    _paces = ['1927', '7062', '7967', '8070', '8979', '7275', 
              '6665', '6364', '6564', '6254', '7770', '5466', 
              '7975', '6654', '7545', '5462', '4543', '5041', 
              '4341', '6254', '4140']
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PaceIns, cls).__new__(cls)
            cls._instance.index = 0
        return cls._instance

    def get_pace(self):
        if self.index < len(self._paces):
            pace = self._paces[self.index]
            self.index += 1
            return pace
        else:
            return None

class TestChineseChessPlayer():
    def __init__(self, game, player=1):
        self.game = game
        self.player = player
        self.paceIns = PaceIns()

    def play(self, board):
        time.sleep(1)
        s = self.paceIns.get_pace()
        x1, y1, x2, y2 = int(s[0]), int(s[1]), int(s[2]), int(s[3])
        print(f"play {x1},{y1} -> {x2},{y2}")
        a = self.game.move_to_action(board, x1, y1, x2, y2)
        return a


class HumanChineseChessPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        valids = self.game.getValidMoves(board, 1)
        for i, v in enumerate(valids):
            if v == 0:
                continue
            print("[", i, end="] ")
        while True:
            input_move = input()
            input_a = input_move.split(" ")
            if len(input_a) == 4:
                try:
                    x1, y1, x2, y2 = [int(i) for i in input_a]
                    a = self.game.move_to_action(board, x1, y1, x2, y2)
                    if valids[a]:
                        break
                except ValueError:
                    # Input needs to be an integer
                    'Invalid integer'
            print('Invalid move')
        return a
