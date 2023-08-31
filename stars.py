import sys
import pygame

class Stars:
    """Overall class to represent stars and app attributes"""
    def __init__(self):
        """Initialize the app and create resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
    
    def run_app(self):
        """Runs the app"""
        while True:
            self.screen.fill((0, 0, 30))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    starry = Stars()
    starry.run_app()