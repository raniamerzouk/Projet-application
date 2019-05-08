#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import *
from soccersimulator import*


class SuperState(object):
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_team = id_team 
        self.id_player = id_player

    def __getattr__(self, attr):
        return getattr(self.state, attr)     

    #position de la balle
    @property
    def ball(self):
        return self.state.ball.position
    
    #position balle anticipée
    @property
    def balleamelioree(self):
        return self.state.ball.position  + (5 * self.state.ball.vitesse)    
    
    #position du joueur
    @property
    def player(self):
        return self.state.player_state(self.id_team, self.id_player).position
   
    #own goal
    @property 
    def goal(self):
        return Vector2D(GAME_WIDTH * ((self.id_team-1)), GAME_HEIGHT /2)
    
    #goal adverse
    @property 
    def goal_opponent(self):
        return Vector2D(GAME_WIDTH * (2- self.id_team), GAME_HEIGHT /2)
    
                ########################################################################################
                #                       Méthodes et propriétés liées au joueur                         #
                ########################################################################################
    
    #liste des joueurs
    @property
    def list_player(self):
        return [self.state.player_state(it, ip).position for (it, ip) in self.state.players]
    
    #trouver la distance entre objet et joueur
    def getDistanceTo(self, obj):
        return self.player.distance(obj)
    
    #le joueur a-t-il la balle ?
    def has_ball(self, pos):
        return self.ball.distance(pos) <= PLAYER_RADIUS + BALL_RADIUS
    
    #la balle est-elle devant le joueur?
    @property 
    def balldevantjoueur(self):
        if self.id_team == 1:
            return self.ball.x > self.player.x
        else:
            return self.ball.x < self.player.x

                #########################################################################################
                #                          Méthodes et propriétés liées au coequipier                   #
                #########################################################################################
     
    #liste des coequipiers
    @property
    def listecoequipier(self):
        return [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players if (id_team == self.id_team) and (id_player != self.id_player)]
   
    #coequipier le plus proche
    @property
    def coequipierproche(self):
        return min([(self.player.distance(player), player) for player in self.listecoequipier],key=lambda x: x[0])[1]
    
    #coequiper le plus proche des cages de l'équipe adverse
    @property
    def coequipierprochegoal_op(self):
        return min([(player.distance(self.goal_opponent), player) for player in self.listecoequipier],key=lambda x: x[0])[1]
    
    def coequipierDistanceTo(self, obj):
        return self.coequipierproche.distance(obj)
    
    #coequiper proche de ses propres cages
    @property
    def coequipierprochedugoal(self):
        return min([(self.player.distance(self.goal), player) for player in self.listecoequipier],key=lambda x: x[0])[1]
    
    #coequipier le plus proche de la balle
    @property
    def coequipierprocheball(self):
        return min([(self.player.distance(self.ball), player) for player in self.listecoequipier],key=lambda x: x[0])[1]

    #distance entre le joueur et son coequipier
    @property
    def dist_coequipier_player(self):
        return Vector2D(self.player.x - self.coequipierproche.x, self.player.y - self.coequipierproche.y).norm
    
    #liste des coequipiers se trouvant devant le joueur
    @property 
    def listecoequipiersdevant(self):
        L = []
        if self.id_team ==1:
            for player in self.listecoequipier:
                if self.player.x < player.x:
                    L.append(player)
        else:
            for player in self.listecoequipier:
                if self.player.x > player.x:
                    L.append(player)
        return L
    
    #coequipier devant le joueur le plus proche
    @property
    def coequipierprochedevant(self):
        return min([(self.player.distance(player), player) for player in self.listecoequipiersdevant],key=lambda x: x[0], default=(None, None))[1]
<<<<<<< HEAD
    @property
    def coequipierprochedevant2(self):
        if self.listecoequipiersdevant == []:
            return self.closest_opponent
        else:
            return min([(self.player.distance(player), player) for player in self.listecoequipiersdevant],key=lambda x: x[0], default=(None, None))[1]
    #COEQUIPIER DEVANT OU PAS   
=======

    #test pour savoir si le coequipier est devant le joueur ou pas     
>>>>>>> d6a95b880940566ba39ce29ec2f4c553a1034f3d
    @property 
    def testjoueurdevant(self):
        if self.id_team == 1:
            return self.coequipierproche.x > self.player.x
        else:
            return self.coequipierproche.x < self.player.x
        
               #########################################################################################
               #                         Méthodes et propriétés liées aux opponents                    #   
               #########################################################################################
                            
    #liste des adversaires
    @property
    def opponents(self):
        return [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team != self.id_team]
    
    #si c'est un adversaire ou pas
    @property
    def test_opponents(self):
        for i in opponents:
            return True
        return False
    
    #trouver l'adversaire le plus proche
    @property
    def closest_opponent(self):
        return min([(self.player.distance(player), player) for player in self.opponents],key=lambda x: x[0])[1]
    
    @property
    def dist_opponent_player(self):
        return Vector2D(self.player.x - self.closest_opponent.x, self.player.y - self.closest_opponent.y).norm
    
    #id_team de l'équipe adverse
    @property
    def id_opponent(self):
        return (self.id_team % 2)+1
    
<<<<<<< HEAD
#    @property 
#    def testopponentderriere(self):
#        if self.id_team == 1:
#            for opponent in self.opponents:
#                if opponent.x <= self.player.x:
#                    return False
#            return True
#                    
#        else:
#            for opponent in self.opponents:
#                if opponent.x >= self.player.x:
#                    return False
#            return True
    
    
=======
    #test si l'adversaire est derrière le joueur ou pas
    @property 
    def testopponentderriere(self):
        if self.id_team == 1:
            for opponent in self.opponents:
                if opponent.x <= self.player.x:
                    return False
            return True
                    
        else:
            for opponent in self.opponents:
                if opponent.x >= self.player.x:
                    return False
            return True
        
    #test si l'adversaire est devant la balle ou pas
>>>>>>> d6a95b880940566ba39ce29ec2f4c553a1034f3d
    @property 
    def testopponentdevantball(self):
        if self.id_team == 1:
            for opponent in self.opponents:
                if opponent.x <= self.ball.x:
                    return True
            return False
                    
        else:
            for opponent in self.opponents:
                if opponent.x >= self.ball.x:
                    return True
            return False
        
    #test si l'adversaire le plus proche est devanr ou derrière le joueur
    @property
    def estderriere(self):
        if self.id_team == 1 :
            return self.closest_opponent.x >= self.player.x
        if self.id_team == 2 :
            return self.closest_opponent.x <= self.player.x
    
                #########################################################################################
                #                Méthodes et propriétés liées aux positions du terrain                  # 
                #########################################################################################
    
    #milieu du terrain
    @property
    def milieu(self):
        if self.id_team == 1:
            return self.ball.x <= GAME_WIDTH/2
        else:
            return self.ball.x > GAME_WIDTH/2
        
    #position du defenseur
    @property
    def pos_def(self):
        if self.id_team == 1:
            pos = GAME_WIDTH/5
        else:
            pos = (4*GAME_WIDTH)/5
        return pos
    
    #où se trouve la balle par rapport au défenseur?
    @property
    def test_posball(self):
        if self.id_team == 1:
            return self.ball.x < self.pos_def+10
        else:
            return self.ball.x > self.pos_def-10
    
    #1/4 du terrain
    @property
    def quart_terrain(self):
        if self.id_team == 1:
            return GAME_WIDTH/4
        else:
            return (3*GAME_WIDTH)/4
<<<<<<< HEAD
    
    @property
    def posattaquantdanssonmilieu (self):
        if self.id_team == 1:
            return Vector2D(2*GAME_WIDTH/5, 2*GAME_HEIGHT/3)
        else:
            return Vector2D(3*GAME_WIDTH/5, 2*GAME_HEIGHT/3)
    @property
    def terrain2_5 (self):
        if self.id_team == 1:
            return 1*GAME_WIDTH/3
        else:
            return 2*GAME_WIDTH/3
    @property
    def testposballterrain2_5 (self):
        if self.id_team == 1:
            return self.ball.x >= self.terrain2_5
        else:
            return self.ball.x <= self.terrain2_5
        
=======
        
    #position de l'attaquant 2
>>>>>>> d6a95b880940566ba39ce29ec2f4c553a1034f3d
    @property 
    def pos_att2(self):
        if self.id_team ==1:
            return Vector2D(4*GAME_WIDTH/5, GAME_HEIGHT/3)
        else:
            return Vector2D(GAME_WIDTH/5, GAME_HEIGHT/3)
        
    #position de l'attaquant 1   
    @property
    def pos_att(self):
        if self.id_team == 1:
            return Vector2D( 2*GAME_WIDTH/3,  2*GAME_HEIGHT/3)
        else:
            return Vector2D(GAME_WIDTH/3, 2*GAME_HEIGHT/3)
        
    @property
    def pos_att3(self):
        if self.id_team == 1:
            return Vector2D((5*GAME_WIDTH)/8., (2*GAME_HEIGHT)/3.)
        else:
            return Vector2D((3*GAME_WIDTH)/8., (2*GAME_HEIGHT)/3.)
        
    @property
    def pos_att4(self):
        if self.id_team == 1:
            return Vector2D((7*GAME_WIDTH)/8., GAME_HEIGHT/3.)
        else:
            return Vector2D(GAME_WIDTH/8., GAME_HEIGHT/3.)
    
    @property
    def testposballgardien(self):
        if self.test_posball:
            if (self.ball.y > 0 and self.ball.y < 10) or (self.ball.y >0 and self.ball.y  < GAME_HEIGHT):
                return  True
        else:
            return False
    
        
                    #####################################################################################
                    #              Méthodes et propriétés liées aux positions des cages                 #
                    #####################################################################################
    
    @property
    def goal_radius(self):
        return GAME_GOAL_HEIGHT/2.
    
    #centre des cages
    @property
    def goal_center(self):
        return self.goal_radius + GAME_HEIGHT/2.
    
    #foncer vers le but 
    @property
    def foncer_vers_but(self):
        return SoccerAction(shoot = (self.goal - self.ball).normalize())
   
    #shoot vers le but 
    @property
    def tirer_au_but(self):
        return SoccerAction(shoot =(self.goal - self.ball).normalize()*maxPlayerShoot) 
    
    ########################################################
    ########################################################
    
    #pour se deplacer vers un objet
    def deplacement(self, obj):
        return (obj - self.player).normalize()*6

    #le joueur peut-il tirer?
    @property
    def can_shoot(self):
        return self.getDistanceTo(self.ball) <= BALL_RADIUS + PLAYER_RADIUS
    
    #tirer
    @property
    def shoot(self, target, strength):
        return (target-state.player_state(id_team, id_player).position).normalize() * strength
    
    #tir coin bas gauche
    @property
    def tirCoinBasG(self):
        return Vector2D(0, 0) - self.player
    
    #tir coin bas droit
    @property
    def tirCoinBasG(self):
        return Vector2D(150, 0) - self.player
    
    #tir coin haut
    @property
    def tirCoinHaut(self):
        if self.id_team == 1:
            return Vector2D(GAME_HEIGHT, GAME_WIDTH) - self.player
        else:
            return Vector2D(0, 90) - self.player    
    
    #dribbler            
    @property
    def dribble(self) :
        if self.estderriere: #si l'adversaire est derrière on dribble 
            if self.closest_opponent.y > self.player.y or self.closest_opponent.y == self.player.y : #Si le joueur vient par la droite
                dir = (self.goal_opponent - self.player).normalize() * 1.5
                dir.angle -= 3.14/6
                return SoccerAction(shoot = dir)
                #return SoccerAction(shoot = Vector2D(s.goaladverse.x - s.player.x, s.opposantsplusproche[1].y-15 - s.player.y).normalize()*1.1) #+ self.avanceravecballe #On avance par la gauche
                    
            else : 
                dir = (self.goal_opponent - self.player).normalize() * 1.5
                dir.angle += 3.14/6
                return SoccerAction(shoot = dir)
                #return SoccerAction(shoot = Vector2D(s.goaladverse.x - s.player.x, s.opposantsplusproche[1].y+15 - s.player.y).normalize()*1.1) #+ self.avanceravecballe #On avance par la gauche
                
        else : 
            shoot = self.goal_opponent - self.player
            return SoccerAction(shoot = shoot.normalize()*1.2)
    
    
    @property
    def attaquant_avance(self):
        if self.id_team == 1: 
            if self.testjoueurdevant:
                acceleration = Vector2D(self.coequipierproche.x*1.2, self.player.y) - self.player 
                return SoccerAction(acceleration = acceleration)
            
        else: 
            if self.testjoueurdevant:
                acceleration = Vector2D(self.coequipierproche.x/1.2, self.player.y) - self.player
                return SoccerAction(acceleration = acceleration)
  

    @property 
    def deplacementopponentderriere(self):
        if self.id_team == 1:
            for opponent in self.opponents:
                    deplacement = opponent - self.player
                    return SoccerAction(acceleration = deplacement)
                    
        else:
            for opponent in self.opponents:
                    deplacement = opponent - self.player
                    return SoccerAction(acceleration = deplacement)
        