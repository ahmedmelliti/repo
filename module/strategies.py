from soccersimulator  import Strategy, SoccerAction, Vector2D, SoccerState
from soccersimulator import SoccerTeam, Simulation, Player
from soccersimulator import show_simu
from soccersimulator.settings import *
from tools import *
import math
## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-0.5,0.5),Vector2D.create_random(-0.5,0.5))


## Strategie Fonceur
class FonceurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Fonceur")
    def compute_strategy(self,state,id_team,id_player):
	t = Tools(state,id_team,id_player)		
	if t.canshoot():
		return SoccerAction(t.goto(t.ball_position)*100,0)
	return SoccerAction(0, 0.08*(t.cage_adv - t.p_position))

## Strategie DefenseZone 
class DZStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"DZ")
    def compute_strategy(self,state,id_team,id_player):
	t = Tools(state,id_team,id_player)
	print(t.adv_le_plus_proche())
	#if t.dbp()<1.65:
	if not t.canshoot():
	#0.8
		if (t.p_position.x-t.adv_le_plus_proche().x<150):
			return SoccerAction(0, 400*(t.cage_adv - t.p_position))
		return SoccerAction(0, 0.001*(t.cage_adv - t.p_position))		
	if t.dbp()<=GAME_WIDTH/4.:
		return SoccerAction(t.goto(t.ball_position)*1,0)	
	if t.p_position.distance(t.cage_adv)<GAME_WIDTH/4.:
		return SoccerAction(t.goto(Vector2D(GAME_WIDTH*3/4.,GAME_HEIGHT/2.)),0)
	
		print(1)
## Strategie FonceurA
class FonceurAStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"FonceurA")
    def compute_strategy(self,state,id_team,id_player):
	t = Tools(state,id_team,id_player)		
	if t.canshoot():
		return SoccerAction(t.goto(t.ball_position)*100,0)
	return SoccerAction(0, 0.01*(t.cage_adv - t.p_position))

