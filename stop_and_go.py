#coding: utf-8

import random, scene, sound

g_speed = 5
g_number_of_enemies = 10

def random_color():
    return scene.Color(random.random(), random.random(), random.random())

class Particle(object):
    def __init__(self, frame=None, velocity=None, color=None):
        self.frame = frame or scene.Rect(0, 0, 25, 25)
        self.velocity = velocity or scene.Point(0, 0)
        self.save_velocity = self.velocity
        self.color = color or random_color()

    def update(self):
        self.frame.x += self.velocity.x
        self.frame.y += self.velocity.y

    def draw(self):
        self.update()
        scene.stroke(0, 0, 0)
        scene.fill(*self.color)
        scene.rect(*self.frame)

    @property
    def is_moving(self):
        return self.velocity.x or self.velocity.y

    def reverse_x(self):
        self.velocity.x *= -1
        self.save_velocity = self.velocity

    def reverse_y(self):
        self.velocity.y *= -1
        self.save_velocity = self.velocity

    def keep_in_bounds(self, bounds):
        if (self.frame.x <= bounds.x
         or self.frame.x + self.frame.w >= bounds.x + bounds.w):
            self.reverse_x()
        if (self.frame.y <= bounds.y
         or self.frame.y + self.frame.h >= bounds.y + bounds.h):
            self.reverse_y()

def random_particle():
    def random_velocity():
        return random.randint(-g_speed, g_speed) or random_velocity()
    return Particle(velocity=scene.Point(random_velocity(), random_velocity()))

class MyScene(scene.Scene):
    def __init__(self):
        #self.player = Particle()
        self.save_velocity_x = g_speed
        self.enemies = [random_particle() for i in xrange(g_number_of_enemies)]
        scene.run(self, scene.LANDSCAPE)
    
    def setup(self):
        self.player = self.make_player()
        for enemy in self.enemies:  # place enemies randomly in self.bounds
            enemy.frame.x = random.randint(0, self.bounds.w - enemy.frame.w)
            enemy.frame.y = random.randint(0, self.bounds.h - enemy.frame.h)

    def make_player(self):
        player_size = 35
        frame = scene.Rect(0, (self.bounds.h - player_size) / 2, player_size, player_size)
        color = scene.Color(1, 1, 1)
        return Particle(frame=frame, color=color)

    def draw(self):
        scene.background(0, 0.5, 1)
        self.player.draw()
        self.player.keep_in_bounds(self.bounds)
        player_frame = self.player.frame
        for enemy in self.enemies:
            enemy.draw()
            enemy.keep_in_bounds(self.bounds)
            if (self.player.is_moving
            and enemy.frame.intersects(player_frame)):
                sound.play_effect('arcade:Explosion_1')

    def touch_began(self, touch):
        if self.player.is_moving:
            self.save_velocity_x = self.player.velocity.x
            self.player.velocity.x = 0
        else:
            self.player.velocity.x = self.save_velocity_x

MyScene()
