import sys
import pygame

from stars import Stars

class StarrySky:
    """Overall class to represent stars and app attributes"""
    def __init__(self):
        """Initialize the app and create resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.screen_rect = self.screen.get_rect()
        self.star = Stars(self)

    def run_app(self):
        """Runs the app"""
        while True:
            self._check_events()
            self._update_screen()
    
    def _check_events(self):
        """Checks for events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _update_screen(self):
        """Updates the screen"""
        self.screen.fill((0, 0, 30))

        # Draw stars
        for x in range(0, self.screen.get_width(), 50):
            for y in range(0, self.screen.get_height(), 50):
                self.star.draw_star(x, y)

        pygame.display.flip()

if __name__ == '__main__':
    starry_sky = StarrySky()
    starry_sky.run_app()