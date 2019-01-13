import sys

class Display:
    def display(self, game):
        if game.end == 2:
            self.win(game)
        elif game.end == 1:
            self.lose(game)
        else:
            self.show(game)

    def _display(self, game):
        print(game)

    def show(self, game):
        self._display(game)

    def win(self, game):
        self._display(game)
        print("You win! Score: %s" % game.score)

    def lose(self, game):
        self._display(game)
        print("You lose! Score: %s" % game.score)


