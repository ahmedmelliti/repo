from soccersimulator import SoccerTeam, Simulation, show_simu, Strategy
from module.strategies  import *


## Creation d'une equipe
pyteam = SoccerTeam(name="PyTeam")
thon = SoccerTeam(name="ThonTeam")
pyteam.add("PyPlayer",FonceurStrategy()) #Strategie qui ne fait rien
thon.add("ThonPlayer",Defenseur())   #Strategie aleatoire
pyteam.add("PyPlayer",RandomStrategy())
thon.add("ThonPlayer",Milieu())

#Creation d'une partie
simu = Simulation(pyteam,thon)
#Jouer et afficher la partie
show_simu(simu)
