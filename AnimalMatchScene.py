# See: http://omz-forums.appspot.com/pythonista/post/5883071282806784

import random, scene, sound

font_name = 'ChalkboardSE-Bold'

# Create a list of image names
animals = '''Ant Bear_Face Bug Chicken Cow_Face Dog_Face Elephant Fish
Frog_Face Honeybee Pig_Face Snail Snake Whale Tiger_Face Rabbit_Face'''.split()

# convert an image name to an animal name with spaces between each letter
def animal_name(image_name):
    name = image_name.partition('_')[0].lower()
    name = { 'bug': 'caterpillar',
             'honeybee': 'bee' }.get(name, name)
    return ' '.join(name)  # add spaces between each letter

class AnimalMatchScene(scene.Scene):
    def __init__(self):
        self.current_animal = None
        self.score = 0
        scene.run(self)

    def setup(self):
        # Setup screen with top 200 pixels reserved for text
        w = self.col_width = self.size.w / 4
        h = self.row_height = (self.size.h - 200) / 4
        for animal in animals:
            layer = scene.Layer(scene.Rect(0, 0, w, h))
            layer.image = animal
            self.add_layer(layer)
        self.shuffle_layer_locations()
        self.current_animal = self.different_layer()

    def different_layer(self):
        layer = random.choice(self.root_layer.sublayers)
        if layer == self.current_animal:
            return self.different_layer()
        return layer

    def shuffle_layer_locations(self):
        random.shuffle(self.root_layer.sublayers)
        for i, layer in enumerate(self.root_layer.sublayers):
            layer.frame.x = (i % 4) * self.col_width
            layer.frame.y = (i / 4) * self.row_height

    def draw(self):
        scene.background(0, 0, 0)
        self.root_layer.update(self.dt)
        self.root_layer.draw()
        # draw the text
        name_text = animal_name(self.current_animal.image)
        score_text = 'Score: %d' % self.score
        w, h = self.size
        y = h - 100
        scene.text(name_text, font_name=font_name, font_size=72.0,
            x = w * 0.5, y = y, alignment = 5)
        scene.text(score_text, font_name=font_name, font_size=24.0,
            x = w / 20, y = y, alignment = 6)

    def touch_ended(self, touch):
        if touch.layer == self.current_animal:
            sound.play_effect('Powerup_1')
            self.score += 1
            self.shuffle_layer_locations()
            self.current_animal = self.different_layer()
        elif touch.layer != self.root_layer:
            sound.play_effect('Error')
            self.score -= 1

AnimalMatchScene()
