from game2048.agents import NN_Agent
from game2048.game import Game

game = Game()
test = NN_Agent(game)
test.ModelWrapper.train_offline()
