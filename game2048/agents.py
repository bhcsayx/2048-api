import numpy as np
from .guides import Guides
from .ModelWrapper import ModelWrapper


class Agent:
    '''Agent Base.'''

    def __init__(self, game, display=None):
        self.game = game
        self.display = display

    def play(self, max_iter=np.inf, record=False, verbose=False,record_file='data.txt'):
        n_iter = 0
        if record:
            f = open(record_file,'a')
        while (n_iter < max_iter) and (not self.game.end):
            if record:
                data = self.game.get_ohe()
                tmp = []
                for i in range(16):
                    tmp.append(data[int(i/4)][int(i%4-1)])
            direction = self.step()
            if record:
                tmp.append(direction)
                f.write(str(tmp)+'\n')
            self.game.move(direction)
            n_iter += 1
            if verbose:
                print("Iter: {}".format(n_iter))
                print("======Direction: {}======".format(
                    ["left", "down", "right", "up"][direction]))
                if self.display is not None:
                    self.display.display(self.game)

    def step(self):
        direction = int(input("0: left, 1: down, 2: right, 3: up = ")) % 4
        return direction


class RandomAgent(Agent):

    def step(self):
        direction = np.random.randint(0, 4)
        return direction


class ExpectiMaxAgent(Agent):

    def __init__(self, game, display=None):
        if game.size != 4:
            raise ValueError(
                "`%s` can only work with game of `size` 4." % self.__class__.__name__)
        super().__init__(game, display)
        from .expectimax import board_to_move
        self.search_func = board_to_move

    def step(self):
        direction = self.search_func(self.game.board)
        return direction

class NN_Agent(Agent):
   
   def __init__(self,game,display):
        self.game=game
        self.display=display
        self.ModelWrapper = ModelWrapper()
        self.ModelWrapper.game=game
        #self.ModelWrapper.train_offline()
   def step(self):
        ohe_board = self.ModelWrapper.game.get_ohe()
        direction = self.ModelWrapper.predict(ohe_board)
        print(type(direction))
        return direction
