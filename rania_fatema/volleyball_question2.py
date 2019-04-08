#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:54:33 2019

@author: 3701014
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from .tools import *
import math
from .actions import *
from soccersimulator import VolleySimulation, volley_show_simu
import math
import random 

class Attaque(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
       

        if s.milieu:
            if s.can_shoot:
                if s.avantmilieu:
                    return SoccerAction(shoot = (s.shootavantmilieu - s.player).normalize()*2)
                else:
                    x = s.xdudef
                    y = (s.loin_opponent.y +GAME_HEIGHT)/2
                    return SoccerAction(shoot = (Vector2D(x,y) - s.player).normalize()*6 )
            else:
                return SoccerAction(acceleration = s.balleamelioree -s.player)