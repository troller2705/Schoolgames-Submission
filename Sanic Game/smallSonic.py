
import pygame
from pygame import *
import sys

BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
# Set screen parameters
width = 800
height = 640
dead = False
half_width = int(width / 2)
half_height = int(height / 2)

DISPLAY = (width, height)

bg = pygame.image.load("bg.png")
bg_stretched = pygame.transform.scale(bg, (800, 640))
# Main def
def main():
    global cameraX, cameraY, screen, dead
    timer = pygame.time.Clock()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Sanic!")
    up = down = left = right = running = False
    entities = pygame.sprite.Group()
    player = Player(64, 64)
    platforms = []

    x = y = 0
    level = [
        "P                                          ",
        "P                                          ",
        "P                                          ",
        "P                                          ",
        "P                                          ",
        "P                                          ",
        "P                                          ",
        "P                                          ",
        "P                                          ",
        "P                                          ",
        "P                                          ",
        "P                                          ",
        "P                                          ",
        "PGGGGGGGGGGGGGGGG                                                              E",
        "PPPPPPPPPPPPPPPPP                                                                                                               E",
        "PPPPPPPPPPPPPPPPP                                                              E",
        "PPPPPPPPPPPPPPPP                                                               E",
        "PPPPPPPPPPPPPPP                                                                E",
        "PPPPPPPPPPPPPP                                                                 E",
        "PPPPPPPPPPPPP                                                                  E",
        "PPPPPPPPPPPPP                                                                  E",
        "PPPPPPPPPPPPPG                                                 G    GGGGGGGGGGGP",
        "PPPPPPPPPPPPPPG                                                P    PPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPGG                                          G   P    PPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPG                                         P   P    PPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPGGG      GGGGG         GGGGG             P   P    PPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPG                                     P   P    PPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPG                                    P   P    PPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPGGGGGGGGGGSSSSSSSGGGGGGGSSSSSGGGGGGGPSSSPSSSSPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "E":
                e = ExitBlock(x, y)
                platforms.append(e)
                entities.add(e)
            if col == "G":
                g = Grass(x, y)
                platforms.append(g)
                entities.add(g)
            if col == "L":
                l = Log(x, y)
                platforms.append(l)
                entities.add(l)
            if col == "B":
                b = Enemy(x, y)
                platforms.append(b)
                entities.add(b)
            if col == "S":
                s = Spike(x, y)
                platforms.append(s)
                entities.add(s)
            x += 32
        y += 32
        x = 0

    total_level_width  = len(level[0])*32
    total_level_height = len(level)*32
    camera = Camera(simple_camera, total_level_width, total_level_height)
    entities.add(player)

    while True:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                running = True
                
            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False

        # draw background
        screen.blit(bg_stretched, (0, 0))

        camera.update(player)

        # update player, draw everything else
        player.update(up, down, left, right, running, platforms)
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()

def start():
    pygame.init()
    pygame.mixer.music.load("sanic.wav")
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Sanic!")

    while True:
        for e in pygame.event.get():
            if e.type == KEYDOWN and e.key == K_SPACE:
                main()
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            screen.fill(BLUE)
            bg2 = pygame.image.load("bg1.jpg")
            bg2_stretched = pygame.transform.scale(bg2, (800, 640))
            screen.blit(bg2_stretched, (0, 0))
            myfont = pygame.font.SysFont("comicsans", 48)
            sonic = myfont.render("SONIC", 1, (0,0,0))
            screen.blit(sonic, (350, 175))
            start = myfont.render("Press SPACE to play.", 1, (0,0,0))
            screen.blit(start, (245, 215))
            pygame.display.update()

def end():

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            screen.fill(BLUE)
            bg2 = pygame.image.load("bg1.jpg")
            bg2_stretched = pygame.transform.scale(bg2, (800, 640))
            screen.blit(bg2_stretched, (0, 0))
            myfont = pygame.font.SysFont("comicsans", 48)
            sonic = myfont.render("YOU WON!", 1, (0,0,0))
            screen.blit(sonic, (350, 175))
            start = myfont.render("Press ESCAPE to quit.", 1, (0,0,0))
            screen.blit(start, (245, 215))
            pygame.display.update()

#This is the class that controls where the scrolling stops for the player
class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        #the width and height of the level, we want to stop scrolling at the edges of the level
        self.state = Rect(0, 0, width, height)

    #Method to re-calculate the position on the screen to apply the scrolling
    def apply(self, target):
        return target.rect.move(self.state.topleft)

    #Update camera position once per loop
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

#We just take the position of our target, and add half total screen size.
def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+half_width, -t+half_height, w, h)

#functions to ensure we don't scroll outside of level.
def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+half_width, -t+half_height, w, h
    l = min(0, l)                        # stop scrolling at the left edge
    l = max(-(camera.width-width), l)   # stop scrolling at the right edge
    t = max(-(camera.height-height), t) # stop scrolling at the bottom
    t = min(0, t)                        # stop scrolling at the top
    return Rect(l, t, w, h)

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.image = pygame.image.load("sanic.png")
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect = Rect(x, y, 64, 64)

    def update(self, up, down, left, right, running, platforms):
        if up:
            # only jump if on the ground
            if self.onGround: self.yvel -= 10
        if down:
            pass
        if running:
            self.xvel = 7
        if left:
            self.xvel = -7
        if right:
            self.xvel = 7
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 100: self.yvel = 100
        if not(left or right):
            self.xvel = 0
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    end()
                if isinstance(p, Spike):
                    main()
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

#Classes for each entity/platform
class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("tile.png")
        self.image_stretched = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image_stretched.get_rect(x=x, y=y)

class Grass(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("grass.png")
        self.image_stretched = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image_stretched.get_rect(x=x, y=y)

class Log(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("log.png")
        self.image_stretched = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image_stretched.get_rect(x=x, y=y)

class Spike(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("spike.png")
        self.image_stretched = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image_stretched.get_rect(x=x, y=y)

    def update(self):
        pass

class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF"))

class Enemy(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("vapenation.png")
        self.image_stretched = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image_stretched.get_rect(x=x, y=y)

if __name__ == "__main__":
    start()
