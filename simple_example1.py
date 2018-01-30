from soccersimulator  import Strategy, SoccerAction, Vector2D, SoccerState
from soccersimulator import SoccerTeam, Simulation, Player
from soccersimulator import show_simu
from soccersimulator.settings import *
import math


## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
	#print(state.player_state(id_team,id_player).position)
	#print(state.player_state(id_team,id_player).position.distance(state.ball.position))
        return SoccerAction(Vector2D.create_random(-0.5,0.5),Vector2D.create_random(-0.5,0.5))

## Strategie Fonceur
class FonceurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Fonceur")
    def compute_strategy(self,state,id_team,id_player):
	a = state.player_state(id_team,id_player).position.distance(state.ball.position)
	
	if a>=PLAYER_RADIUS+BALL_RADIUS:
		return SoccerAction((state.ball.position-state.player_state(id_team,id_player).position),0)
	if id_team==1:
		v=Vector2D(GAME_WIDTH,GAME_HEIGHT/2.)
	else:
		v=Vector2D(0,GAME_HEIGHT/2.)
	w=state.player_state(id_team,id_player).position

	#if(state.ball.position.x<GAME_WIDTH*3/4):
		#return SoccerAction(0,Vector2D(GAME_WIDTH*3/4,GAME_GOAL_HEIGHT/4.))
	#return SoccerAction(0,Vector2D(GAME_WIDTH-state.ball.position.x,(GAME_GOAL_HEIGHT/2.)-state.ball.position.y))
	return SoccerAction(0, 0.08*(v - w))


#(GAME_WIDTH,GAME_WIDTH/2.)-state.player_state(id_team,id_player).position)
## Creation d'une equipe
pyteam = SoccerTeam(name="PyTeam")
thon = SoccerTeam(name="ThonTeam")
pyteam.add("PyPlayer",FonceurStrategy()) #Strategie qui ne fait rien
thon.add("ThonPlayer",FonceurStrategy())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(pyteam,thon)
#Jouer et afficher la partie
show_simu(simu)
