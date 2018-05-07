from soccersimulator import SoccerAction,Vector2D,settings ,SoccerTeam,Billard ,show_simu,Strategy
from soccersimulator.settings import * 

class FonceurLent(Strategy):
    def __init__(self):
        super(FonceurLent,self).__init__("fonceur")
    def compute_strategy(self,state,idteam,idplayer):
        ball = state.ball
        me = state.player_state(1,0)
        oth = state.balls[0]
        shoot = (oth.position-ball.position)*0.1
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


myt = SoccerTeam("prof")
myt.add("N",FonceurLent())
b = Billard(myt,type_game=0)
show_simu(b)

