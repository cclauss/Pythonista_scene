# See: http://omz-forums.appspot.com/pythonista/post/5275991815487488

import scene

#color_black = scene.Color(0, 0, 0, .5)
#color_white = scene.Color(1, 1, 1, .5)
color_red   = scene.Color(1, 0, 0, .5)
color_green = scene.Color(0, 1, 0, .5)
color_blue  = scene.Color(0, 0, 1, .5)

class Circle(scene.Layer):
    def __init__(self, in_rect):
        super(self.__class__, self).__init__(in_rect)
        self.background = color_blue
        self.stroke     = color_green
        self.stroke_weight = 1

    def draw(self, a=1):
        super(self.__class__, self).draw()
        g = scene.gravity()
        self.frame.x += g.x * 10
        self.frame.y += g.y * 10
        scene.ellipse(self.frame.x, self.frame.y, self.frame.w, self.frame.h)

class Square(scene.Layer):
    def __init__(self, in_rect):
        super(self.__class__, self).__init__(in_rect)
        self.background = color_red
        self.stroke     = color_green
        self.stroke_weight = 1

    def draw(self, a=1):
        super(self.__class__, self).draw()
        g = scene.gravity()
        self.frame.x += g.x * 10
        self.frame.y += g.y * 10

class MyScene(scene.Scene):
    def __init__(self):
        scene.run(self)

    def setup(self):
        x, y = self.bounds.center()
        self.add_layer(Circle(scene.Rect(x-150, y-150, 100, 100)))
        self.add_layer(Square(scene.Rect(x+50, y+50, 100, 100)))

    def draw(self):
        scene.background(0, 0, 0)
        self.root_layer.update(self.dt)
        self.root_layer.draw()

MyScene()
