class Game:
    def __init__(self, player1, player2, num_rounds=10):
        self.player1 = player1
        self.player2 = player2
        self.num_round = num_rounds
        self.past_results = []
    
    def operate(self):
        for _ in range(self.num_round):
            print(f"Round {_ + 1}")
            reversed_past_results = [(move_2, move_1) for move_1, move_2 in self.past_results]
            self.past_results.append((self.player1.play(self.past_results), self.player2.play(reversed_past_results)))
            print(self.past_results)
    
    def score(self):
        player1_score = sum([self._judge(move_1, move_2)[0] for move_1, move_2 in self.past_results])
        player2_score = sum([self._judge(move_1, move_2)[1] for move_1, move_2 in self.past_results])
        self.player1.keep_score(player1_score)
        self.player2.keep_score(player2_score)

    
    def _judge(self, move_1, move_2):
        if move_1 == 0 and move_2 == 0:
            return (3, 3)
        elif move_1 == 0 and move_2 == 1:
            return (0, 5)
        elif move_1 == 1 and move_2 == 0:
            return (5, 0)
        elif move_1 == 1 and move_2 == 1:
            return (1, 1)
        else:
            raise ValueError("Invalid move")

if __name__ == "__main__":
    pass