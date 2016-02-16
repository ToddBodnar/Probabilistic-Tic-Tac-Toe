import src.game.settings as settings

class Move:
    def __init__(self, player):
        self.player = player
        self.distribution = dict()

    def setMove(self, x, y, amount):
        self.distribution[(x,y)] = amount

    def __str__(self):
        result = "Player "+str(self.player)+" makes moves:"
        for (x,y) in self.distribution:
            result = result + "\n"+str(x)+" "+str(y)+" "+str(self.distribution[(x,y)])
        return result

    def normalize(self):
        total_applied = 0
        for col in range(0,settings.NUM_COLS):
            for row in range(0,settings.NUM_ROWS):
                if (col,row) in self.distribution:
                    total_applied += self.distribution[(col,row)]
                else:
                    self.distribution[(col,row)] = 0
        if total_applied == 0:
            return
        for col in range(0,settings.NUM_COLS):
            for row in range(0,settings.NUM_ROWS):
                self.distribution[(col, row)] /= total_applied


