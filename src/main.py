# %%
from game import *
from players import *
# %%
p1 = Cooperator()
p2 = Defector()
p3 = Random()
game_1 = Game(p1, p3, 20)
game_1.operate()
game_1.score()
# %%
p1.scores
# %%
p2.scores
# %%
p3.scores
# %%
