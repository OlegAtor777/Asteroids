import pygame
from pygame.math import Vector2
from utils import wrap_position
from pygame.transform import rotozoom
import random

UP = Vector2(0, -1)

class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self, surface):
        self.position = wrap_position(self.position + self.velocity, surface)

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius
    
class Spaceship(GameObject):
    MANEUVERABILITY = 1
    ACCELERATION = 0.003
    DECCELERATION = -0.0005
    lives = 5
    def __init__(self, position):
        self.direction = Vector2(UP)
        super().__init__(position, pygame.transform.scale(pygame.image.load('ship.png'),(80,95)), Vector2(0))
       # print(self.position)
        
    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)
    
    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION
        self.sprite = pygame.transform.scale(pygame.image.load('ship_throt.png'),(80,95));
                
        
    def draw(self, surface):
        self.endgame()
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)
        if abs(self.velocity[0]) > 0 or abs(self.velocity[1]) > 0:
            if self.velocity[0] > 0:
                self.velocity[0] += self.DECCELERATION
            else:
                self.velocity[0] -= self.DECCELERATION
            if self.velocity[1] > 0:
                self.velocity[1] += self.DECCELERATION
            else:
                self.velocity[1] -= self.DECCELERATION
    
            
    def endgame(self):
        if self.lives == 0:
            return False
        else:
            return True
        
    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius
        
        
class Asteroid(GameObject):
    MANEUVERABILITY = random.uniform(0, 1.5)
     
    def __init__(self, position, vel0, vel1, clockwise):
        super().__init__(position, pygame.transform.scale(pygame.image.load('asteroid.png'), (100,100)), (0, 0))
        self.direction = Vector2(UP)
        self.vel0 = vel0
        self.vel1 = vel1
        self.clockwise = clockwise
    
    def rotate(self):
        sign = 1 if self.clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)
        
    
    def go(self):
        self.velocity[0]= self.vel0
        self.velocity[1]= self.vel1
        
        
    def draw(self, surface):
        self.go()
        self.rotate()
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)
    