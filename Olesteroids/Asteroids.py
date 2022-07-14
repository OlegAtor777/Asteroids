import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

BACKGROUND = pygame.image.load('background.png')
SHIP = pygame.image.load('ship.png')
ASTEROID_100 = pygame.image.load('asteroid.png')

pygame.display.set_caption('Asteroids')
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

gameover = False

class Player(object):
    def __init__(self):
        self.img = SHIP
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = SCREEN_WIDTH//2
        self.y - SCREEN_HEIGHT//2
        
    def draw(self, win):
        win.blit(self.img, [self.x, self.y, self.w, self.h])


# Функция для обновления экрана
def redrawGameWindow():
    win.blit(BACKGROUND, (0,0))
    player.draw(win)
    pygame.display.update()

player = Player()

run = True
while run:
    clock.tick(60)
    
    if not gameover:
        pass
    
    # Обработка выхода из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    redrawGameWindow()
            
pygame.quit()