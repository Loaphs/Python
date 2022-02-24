import pygame

WID = 400
HEI = 300
BG = (0, 0, 0)


#SPRITE
class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, startx, starty):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.center = [startx, starty]

    def update(self):
            pass

    def draw(self, screen):
            screen.blit(self.image, self.rect)

class Player(Sprite):
    def __init__(self, startx, starty):
        super().__init__("Python\\PyGame Platformer\\p1_front.png", startx, starty)

        self.speed = 4
        self.jumpspd = 10
        self.vsp = 0
        self.gravity = .3

        self.min_jumpspd = 3
        self.prev_key = pygame.key.get_pressed()

    def update(self, boxes):
        hsp = 0
        onground = pygame.sprite.spritecollideany(self, boxes)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            hsp = -self.speed
        elif key[pygame.K_RIGHT]:
            hsp = self.speed

        if key[pygame.K_UP] and onground:
            self.move(0,-self.jumpspd)

        if self.prev_key[pygame.K_UP] and not key[pygame.K_UP]:
            if self.vsp < -self.min_jumpspd:
                self.vsp = -self.min_jumpspd

        #GRAVITY
        if self.vsp < 10 and not onground:
            self.vsp += self.gravity

        if self.vsp > 0 and onground:
            self.vsp = 0

        self.move(hsp, self.vsp)

    def move(self, x, y):
        self.rect.move_ip([x, y])


class Box(Sprite):
    def __init__(self, startx, starty):
        super().__init__("Python\\PyGame Platformer\\stone.png", startx, starty)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WID, HEI))
    clock = pygame.time.Clock()

    player = Player(100, 200)
    
    boxes = pygame.sprite.Group()
    for bx in range(0, 400, 16):
        boxes.add(Box(bx, 300))

    #MAIN LOOP
    while True:
        pygame.event.pump()
        player.update(boxes)

        screen.fill(BG)
        player.draw(screen)
        boxes.draw(screen)
        pygame.display.flip()

        clock.tick(60)

#INIT LOOP
if __name__ == '__main__':
    main()