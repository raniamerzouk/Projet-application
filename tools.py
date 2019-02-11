#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:12:52 2019

@author: 3522495
"""
from math import *
from soccersimulator import*


class SuperState(object):
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_team = id_team 
        self.id_player = id_player

#    def __getattr__(self, attr):
#        return getattr(self.state, attr)     

    @property
    def ball(self):
        return self.state.ball.position
    
    @property
    def player(self):
        return self.state.player_state(self.id_team, self.id_player).position
   
    @property 
    def goal(self):
        return Vector2D(GAME_WIDTH * ((self.id_team-1)), GAME_HEIGHT /2)
    
    @property 
    def goal_opponent(self):
        return Vector2D(GAME_WIDTH * (2- self.id_team), GAME_HEIGHT /2)
    
    def deplacement(self, obj):
        return (obj -self.player).normalize()*1500
    
    #foncer vers le but 
    @property
    def foncer_vers_but(self):
        return SoccerAction(shoot = (self.goal - self.ball).normalize())
   
    #shoot vers le but 
    @property
    def tirer_au_but(self):
        return SoccerAction(shoot =(self.goal - self.ball).normalize()*maxPlayerShoot) 
    
    @property
    def can_shoot(self):
        return (self.state.ball.position - state.player_state(id_team, id_player).position).norm <= BALL_RADIUS + PLAYER_RADIUS
    
    @property
    def shoot(self, target, strength):
        return (target-state.player_state(id_team, id_player).position).normalize() * strength
    
	#liste des opposants
    @property
    def opponents(self):
        return [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team != self.id_team] [1]
    #si il est un opposants ou pas
    @property
    def Test_opponents(self):
        for i in opponents:
            return true
        return false
	#trouver l'adversaire le plus proche 
    def proche_adversaire(self):
        return min([(self.player.distance(player), player) for player in opponents])
	#liste des players
    @property
    def list_player(self):
        return [self.state.player_state(it, ip) for (it, ip) in self.state.players]

	#joeur avec la balle 
    @property
    def player_with_ball(self):
        return min([(self.player.distance(self.ball),player) for player in self.list_player])[1]
    
    #test balle avec le joueur
    @property
    def test_ball(self):
        return (self.player_with_ball == self.player)
    

	 
