import pygame
pygame.init()

screen = pygame.display.set_mode((800,800))

class Circle:
    def __init__(self, color, dimensions):
        self.s = screen
        self.c = color
        self.d = dimensions
    def draw(self):
        pygame.draw.rect(self.s, self.c, self.d)

game = True

c1 = Circle((70, 130, 180),(500, 500, 213, 4))
c2 = Circle((70, 130, 180),(100, 50, 10.5, 213))
c3 = Circle((70, 130, 180),(50, 599, 1, 1))

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    c1.draw()
    c2.draw()
    c3.draw()
    pygame.display.update()


    
