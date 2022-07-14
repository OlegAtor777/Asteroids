import pygame
import random
# импорт загрузчика
from utils import get_random_position
from models import Asteroid, Spaceship

class SpaceRocks:
    MIN_ASTEROID_DISTANCE = 250
    
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load('background.png')
        self.clock = pygame.time.Clock()

        self.asteroids = [Asteroid(get_random_position(self.screen), random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), random.choice([True, False])) for _ in range(6)]
        self.spaceship = Spaceship((400, 300))

   
        
       
    def main_loop(self):
        run = True
        pygame.font.init()
        f1 = pygame.font.Font(None, 36)
        f2 = pygame.font.Font(None, 50)
        
        while run:
            self._damage()
            self.text1 = f1.render(f'lives: {self.spaceship.lives}', True,
                  (180, 0, 0))
            if self.spaceship.lives == 0:
                self.text2 = f2.render(f'GAME OVER', True,
                      (180, 0, 0))
                self.screen.blit(self.text2, (400, 300))
                pygame.time.wait(5000)
                
                pygame.quit()
                
            self._handle_input()
            self._process_game_logic()
            self._draw()
            
            #print(lives)
            #print(self.spaceship.position)
            #for aster in self._get_asteroids():
             #   aster.go(random.uniform(-1, 1),random.uniform(-1, 1))

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption('Asteroids')
        

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
        is_key_pressed = pygame.key.get_pressed()
        
        
        if is_key_pressed[pygame.K_RIGHT]:
            self.spaceship.rotate(clockwise=True)
        elif is_key_pressed[pygame.K_LEFT]:
            self.spaceship.rotate(clockwise=False)  
        if is_key_pressed[pygame.K_UP]:
            self.spaceship.accelerate()
            #self.spaceship.sprite = pygame.transform.scale(pygame.image.load('ship_throt.png'),(80,95))
        else:
            self.spaceship.sprite = pygame.transform.scale(pygame.image.load('ship.png'),(80,95))
            
    def _process_game_logic(self):
        for game_object in self._get_game_objects():
            game_object.move(self.screen)
            
        
        #for i in range(len(self.asteroids)):
         #   self.asteroids[i].rotate()
    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text1, (20, 50))
        
        for game_object in self._get_game_objects():
            game_object.draw(self.screen)
        pygame.display.flip()
    
    def _get_game_objects(self):
        return [*self.asteroids, self.spaceship]
    
    def _get_asteroids(self):
        return self.asteroids
    
    def is_near(self,x1,x2,y1,y2):
       nr = ((x2-x1)**2+(y2-y1)**2)**0.5
       return print(nr)
    
    def _damage(self):
        #for i in self._get_asteroids():
        if self.spaceship.collides_with(self.asteroids[0]):
            self.asteroids[0].position[0] = random.randint(0, 799)
            self.asteroids[0].position[1] = random.randint(0, 599)
            self.spaceship.lives -= 1
            
        elif self.spaceship.collides_with(self.asteroids[1]):
            self.asteroids[1].position[0] = random.randint(0, 799)
            self.asteroids[1].position[1] = random.randint(0, 599)
            self.spaceship.lives -= 1
            
        elif self.spaceship.collides_with(self.asteroids[2]):
            self.asteroids[2].position[0] = random.randint(0, 799)
            self.asteroids[2].position[1] = random.randint(0, 599)
            self.spaceship.lives -= 1
            
        elif self.spaceship.collides_with(self.asteroids[3]):
            self.asteroids[3].position[0] = random.randint(0, 799)
            self.asteroids[3].position[1] = random.randint(0, 599)
            self.spaceship.lives -= 1
            
        elif self.spaceship.collides_with(self.asteroids[4]) :
            self.asteroids[4].position[0] = random.randint(0, 799)
            self.asteroids[4].position[1] = random.randint(0, 599)
            self.spaceship.lives -= 1
            
        elif self.spaceship.collides_with(self.asteroids[5]):
            self.asteroids[5].position[0] = random.randint(0, 799)
            self.asteroids[5].position[1] = random.randint(0, 599)
            self.spaceship.lives -= 1
            
            #if self.is_near(i.position[0],self.spaceship.position[0],i.position[1],self.spaceship.position[1]) < 40:
             #   print('near')
            #self.is_near(i.position[0],self.spaceship.position[0],i.position[1],self.spaceship.position[1])
            #print(i.position, self.spaceship.position)
            #if (i.position[0] >= self.spaceship.position[0] - 80//2 and i.position[0] <= self.spaceship.position[0] + 80//2) or (i.position[0] + 50 <= self.spaceship.position[0] + 80//2 and i.position[0] + 50 >= self.spaceship.position[0] - 80//2):
                   #if(i.position[1] >= self.spaceship.position[1] - 95//2 and i.position[1] <= self.spaceship.position[1] + 95//2) or (i.position[1] + 50 >= i.position[1] - 95//2 and i.position[1] + 50 <= self.spaceship.position[1] + 95//2):
            #i.position[0] = random.randint(0, 799)
            #i.position[1] = random.randint(0, 599)
                       #pygame.time.wait(10000)
            #return -1
        else:
            return 0
               # return print('hello)')
