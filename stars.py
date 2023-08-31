import pygame

class Stars:
    """Class to represent a single star"""
    def __init__(self, game):
        """Set spawn point of the first star"""
        self.screen = game.screen
        
        # Load the image.
        self.image = pygame.image.load('star.bmp')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
    
    def draw_star(self, x, y):
        self.rect.topleft = (x, y)
        self.screen.blit(self.image, self.rect)