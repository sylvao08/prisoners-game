import random
class Player:
    def __init__(self):
        self.scores = []
        
    def _decide(self, past_results):
        pass

    def play(self, past_results):
        return self._decide(past_results)
    
    def keep_score(self, game_score):
        self.scores.append(game_score)

class Cooperator(Player):
    def __init__(self):
        super().__init__()

    def _decide(self, past_results):
        return 0

class Defector(Player):
    def __init__(self):
        super().__init__()

    def _decide(self, past_results):
        return 1
    
class Random(Player):
    def __init__(self):
        super().__init__()

    def _decide(self, past_results):
        return random.choice([0, 1])
    
class TitForTat(Player):
    def __init__(self):
        super().__init__()

    def _decide(self, past_results):
        if len(past_results) == 0:
            return 0
        return past_results[-1][1]
    
if __name__ == "__main__":
    pass