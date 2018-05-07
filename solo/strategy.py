from .utils import  dump_jsonz, load_jsonz, fmt,clean_fn, to_json, to_jsonz, from_json, from_jsonz,dict_to_json
from .utils import  Vector2D, MobileMixin
from .strategies import Strategy,  KeyboardStrategy, DTreeStrategy
from .mdpsoccer import SoccerAction, Ball, PlayerState,SoccerState
from .mdpsoccer import  Player, SoccerTeam, Simulation
from .matches import Score, SoccerTournament
from .gui import SimuGUI, show_simu, show_state, pyg_start, pyg_stop, pyglet
from .challenges import *
from . import  settings
from . import gitutils
from .arbres_utils import apprend_arbre,build_apprentissage,genere_dot
from .billard import BillardState, PlayerStateBillard, Billard,get_collision
import math

class FonceurLent(Strategy):
    def __init__(self):
        super(FonceurLent,self).__init__("fonceur")
    def compute_strategy(self,state,idteam,idplayer):
        ball = state.ball
        me = state.player_state(1,0)
        oth = state.balls[0]
        shoot = (oth.position-ball.position)*100
        if (me.position.distance(ball.position)<(settings.BALL_RADIUS+settings.PLAYER_RADIUS)) and  me.vitesse.norm<0.5:
            return SoccerAction(shoot=shoot)
        acc = ball.position-me.position
        if acc.norm<5:
            acc.norm=100
        return SoccerAction(acceleration=acc)

class Tireur(Strategy):
	def __init__(self):
		super(Tireur,self).__init__("tireur")
	def compute_strategy(self,state,idteam,idplayer):
		ball = state.ball
                me = state.player_state(1,0)
                oth = state.balls[0]
                shoot = (oth.position-ball.position)*100
                shoot1 = Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-me.position
                if (me.position.distance(ball.position)<(settings.BALL_RADIUS+settings.PLAYER_RADIUS)) and  me.vitesse.norm<0.5:
                        if ball.position.distance(oth.position)<0.5 :
                                if ball.position.distance(Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.))<settings.GAME_WIDTH/2 :
                                        return SoccerAction(shoot=shoot)
                                return SoccerAction(shoot=shoot1)
                        return SoccerAction(shoot=shoot)
                #acc = ball.position-me.position
                #if acc.norm<5:
                #    acc.norm=100

                return SoccerAction(ball.position-me.position)

