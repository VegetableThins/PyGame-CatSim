# KidsCanCode - Game Development with Pygame video series
# Jumpy! (a platform game) - Part 9
# Video link: https://youtu.be/mBC5VqxnFLA
# Using Spritesheets
# Art from Kenney.nl

import pygame as pg
import random
from Settings import *
from sprites import *
from os import path


class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.time = pg.time
        self.clock = pg.time.Clock()
        self.running = True
        # self.font_name = pg.font.Font('RobotoMono-Regular.ttf', 16)
        self.font_name = None
        self.load_data()

    def load_data(self):
        # load high score
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, 'IMG')
        self.spritesheet = SpriteSheet(path.join(img_dir, SPRITESHEET))

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        # self.cat = Cat(self)
        # self.all_sprites.add(self.cat)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pg.MOUSEBUTTONDOWN:  # Mouse gone down?
                posn_of_click = event.dict["pos"]  # Get the coordinates.
                spriteclicked = False
                for sprite in self.all_sprites:
                    if sprite.contains_point(posn_of_click):
                        spriteclicked = True
                        sprite.handle_click()
                        # self.all_sprites.remove(sprite)
                        # del sprite
                        break
                if spriteclicked == False:
                    newcat = Cat(self, posn_of_click)
                    self.all_sprites.add(newcat)

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platform - only if falling

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text("Number of Cats = {}".format(len(self.all_sprites)), 22, WHITE, WIDTH / 2, 15)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        # self.draw_text("Arrows to move, Space to jump", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        # self.draw_text("Press a key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        # self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()

    # def show_go_screen(self):
        # game over/continue
        # if not self.running:
            # return
        # self.screen.fill(BGCOLOR)
        # self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        # self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
        # self.draw_text("Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        # if self.score > self.highscore:
        #     self.highscore = self.score
        #     self.draw_text("NEW HIGH SCORE!", 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
        #     with open(path.join(self.dir, HS_FILE), 'w') as f:
        #         f.write(str(self.score))
        # else:
        #     self.draw_text("High Score: ", 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
        # pg.display.flip()
        # self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
