# Sprite classes for platform game
import pygame as pg
import random
from Settings import *
vec = pg.math.Vector2


class SpriteSheet:
    # utility class for loading and parsing spritesheets
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        # grab an image out of a larger spritesheet
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image, (width * 3, height * 3))
        return image


class HealthBar(pg.rect.Rect):
    def __init__(self, pos, width):
        pg.rect.Rect.__init__(self)



class Cat(pg.sprite.Sprite):
    def __init__(self, game, pos):
        # positioning and graphics
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.load_images()
        self.image = self.idle_frame
        self.image.set_colorkey(COLORKEY)
        self.image.fill((190, 0, 0), special_flags=pg.BLEND_MULT)

        self.last_update = 0
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.pos = vec(pos[0], pos[1])
        self.direction = True
        self.new_x = 0
        self.new_y = 0

        # Cat properties
        self.health = 100
        self.hunger = 100
        self.happiness = 100

    def load_images(self):
        self.idle_frame = self.game.spritesheet.get_image(CAT_SPRITE[0], CAT_SPRITE[1], SPRITE_SIZE, SPRITE_SIZE)
        self.damaged_frame = self.game.spritesheet.get_image(DAMAGE_SPRITE[0], DAMAGE_SPRITE[1], SPRITE_SIZE, SPRITE_SIZE)
        self.idle_frame.set_colorkey(COLORKEY)
        self.damaged_frame.set_colorkey(COLORKEY)

    def update(self):
        now = pg.time.get_ticks()
        self.health -= 0.1

        if now - self.last_update > random.randint(2000, 5000):
            self.last_update = now
            self.new_x = self.pos.x + random.randint(-30, 30)
            self.new_y = self.pos.y + random.randint(-30, 30)

        # update sprite on movement
        if self.new_x > self.pos.x:
            self.pos.x += 1
        elif self.new_x < self.pos.x:
            self.pos.x -= 1
        elif self.new_x == self.pos.x:
            pass

        if self.new_y > self.pos.y:
            self.pos.y += 1
        elif self.new_y < self.pos.y:
            self.pos.y -= 1
        elif self.new_y == self.pos.y:
            pass

        if self.health <= 0:
            self.kill()
        # if self.pos.x <= 0:
        #     self.direction = True
        #
        # if self.pos.x >= WIDTH:
        #     self.direction = False

        # if self.direction:
        #     self.pos.x += 2
        # else:
        #     self.pos.x -= 2


        self.rect.midbottom = self.pos

    def animate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 350:
            self.last_update = now
            bottom = self.rect.bottom
            self.image = self.damaged_frame
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom

        # self.rect.center = self.pos
        # keys = pg.key.get_pressed()
        # if keys[pg.K_LEFT]:
        #     self.acc.x = -PLAYER_ACC
        # if keys[pg.K_RIGHT]:
        #     self.acc.x = PLAYER_ACC
        #
        # # apply friction
        # self.acc.x += self.vel.x * PLAYER_FRICTION
        # # equations of motion
        # self.vel += self.acc
        # self.pos += self.vel + 0.5 * self.acc
        # # wrap around the sides of the screen
        # if self.pos.x > WIDTH:
        #     self.pos.x = 0
        # if self.pos.x < 0:
        #     self.pos.x = WIDTH
        #
        # self.rect.midbottom = self.pos

    def contains_point(self, pt):
        """ Return True if my sprite rectangle contains point pt """
        (my_x, my_y) = self.pos
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        (x, y) = pt
        return my_x <= x < my_x + my_width and y >= my_y and y < my_y + my_height

    def handle_click(self):
        print("cat clicked.")
        self.animate()

    def destruction(self):
        print("destroying cat instance")
        self.kill()
# class Platform(pg.sprite.Sprite):
#     def __init__(self, x, y, w, h):
#         pg.sprite.Sprite.__init__(self)
#         self.image = pg.Surface((w, h))
#         self.image.fill(GREEN)
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y