from soccersimulator  import Strategy, SoccerAction, Vector2D, SoccerState
from soccersimulator import SoccerTeam, Simulation, Player
from soccersimulator import show_simu
from soccersimulator.settings import *


class Tools(object):
	def __init__(self, state,id_team,id_player):
		self.state = state
		self.id_team = id_team
		self.id_player= id_player

	def goto(self, position):
		return (position-self.state.player_state(self.id_team,self.id_player).position)

	def shoot(self, position):
		return (position-self.state.player_state(self.id_team,self.id_player).position)
		
	def dbp(self):
		return self.state.player_state(self.id_team,self.id_player).position.distance(self.state.ball.position)
	
	def canshoot(self):
		return self.dbp()>=PLAYER_RADIUS+BALL_RADIUS

	def cage(self):
		if self.id_team==1:
			return Vector2D(GAME_WIDTH,GAME_HEIGHT/2.)
		else:
			return Vector2D(0,GAME_HEIGHT/2.)

