
import pygame

BLACK = (0, 0, 0)

class Background(pygame.sprite.Sprite):    
    def __init__(self, color, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.width = width
        self.height = height
 
        pygame.draw.rect(self.image, color,(0,0,width,height))
        self.rect = self.image.get_rect()


    def draw(self):
        pygame.draw.rect(self.image, BLACK ,(0,0,self.width,self.height))



