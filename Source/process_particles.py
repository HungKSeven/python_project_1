from tv import *
from process_animation import Animation
from process_alpha import *
from process_distance import *
from colors import *


class Particle_1:
    def __init__(self, v, size_start, alpha, in_out, case, pos_start, v_size, g, color_light):
        # basic 1
        self.pos = pos_start
        self.size = size_start
        self.alpha_direct = deg_to_rad(alpha)
        self.in_out = in_out
        self.dir_folder = os.path.abspath(os.getcwd())+'/imgs/particle/'
        self.dir_animation_cases = listdir(self.dir_folder)
        self.case_particle = case
        self.animation_cases = []
        self.load_animation()
        self.animation_case = self.animation_cases[self.case_particle]
        self.pos_on_screen = [0, 0]
        self.v = v * self.in_out
        self.vx = self.v * math.cos(self.alpha_direct)
        self.vy = -self.v * math.sin(self.alpha_direct)
        self.v_size = v_size * self.in_out
        self.g = g
        self.suf_light_particle = None
        self.color_light = color_light

    def create_light(self):
        self.suf_light_particle = pg.Surface((self.size[0] * 2, self.size[1] * 2))
        pg.draw.circle(self.suf_light_particle, self.color_light, (self.size[0] * 1, self.size[1] * 1),
                       self.size[0] * 1)

    def set_pos_start(self, pos_start):
        self.pos = pos_start

    def load_animation(self):
        for dir_case in self.dir_animation_cases:
            dir_animation_case = self.dir_folder + dir_case + '/'
            animation_case = Animation(dir_animation_case, self.size, 0, 1)
            self.animation_cases.append(animation_case)

    def fly(self):
        pos = [0, 0]
        pos[0] = self.pos[0] + self.vx
        pos[1] = self.pos[1] + self.vy
        self.vy += self.g
        self.pos = pos

    def resize_particle(self):
        new_size = [1, 1]
        if self.in_out > 0:
            if self.size[0] > 2:
                new_size[0] = self.size[0] - self.v_size
                new_size[1] = self.size[1] - self.v_size
        else:
            new_size[0] = self.size[0] - self.v_size
            new_size[1] = self.size[1] - self.v_size
        self.size = new_size
        self.animation_case.resize_imgs([int(self.size[0]), int(self.size[1])])

    def find_on_screen(self, screen):
        self.pos_on_screen[0] = self.pos[0] - screen.x
        self.pos_on_screen[1] = self.pos[1] - screen.y

    def process_total(self, screen):
        self.fly()
        self.resize_particle()
        self.find_on_screen(screen)
        self.create_light()

    def show(self, suf, runtime):
        rect_light = self.suf_light_particle.get_rect()
        rect_light.center = self.pos_on_screen
        suf.blit(self.suf_light_particle, rect_light, special_flags=pg.BLEND_RGB_ADD)
        self.animation_case.show(suf, runtime, self.pos_on_screen)


class Particle_2:
    def __init__(self, v, size_start, alpha, pos_start, v_size, g, color, color_light, in_out):
        # basic 2
        self.pos = pos_start
        self.size = size_start
        self.alpha_direct = deg_to_rad(alpha)
        self.pos_on_screen = [0, 0]
        self.in_out = in_out
        self.v = v * self.in_out
        self.vx = self.v * math.cos(self.alpha_direct)
        self.vy = -self.v * math.sin(self.alpha_direct)
        self.v_size = v_size * self.in_out
        self.g = g
        self.color = color
        self.color_light = color_light
        self.suf_light_particle = None

    def update_direct(self, alpha):
        self.alpha_direct = deg_to_rad(alpha)
        self.vx = self.v * math.cos(self.alpha_direct)
        self.vy = -self.v * math.sin(self.alpha_direct)

    def create_light(self):
        self.suf_light_particle = pg.Surface((self.size * 4, self.size * 4))
        pg.draw.circle(self.suf_light_particle, self.color_light, (self.size * 2, self.size * 2), self.size * 2)

    def set_pos_start(self, pos_start):
        self.pos = pos_start

    def fly(self):
        pos = [0, 0]
        pos[0] = self.pos[0] + self.vx
        pos[1] = self.pos[1] + self.vy
        self.vy += self.g
        self.pos = pos

    def resize_particle(self):
        self.size -= self.v_size

    def find_on_screen(self, screen):
        self.pos_on_screen[0] = self.pos[0] - screen.x
        self.pos_on_screen[1] = self.pos[1] - screen.y

    def process_total(self, screen):
        self.fly()
        self.resize_particle()
        self.find_on_screen(screen)
        self.create_light()

    def show(self, suf):
        rect_light = self.suf_light_particle.get_rect()
        rect_light.center = self.pos_on_screen
        suf.blit(self.suf_light_particle, rect_light, special_flags=pg.BLEND_RGB_ADD)
        pg.draw.circle(suf, self.color, self.pos_on_screen, self.size)


class Particle_3:
    def __init__(self, v, size_start, alpha, pos_start, v_size, g, color):
        # name: smoke
        self.pos = pos_start
        self.size = size_start
        self.alpha_direct = deg_to_rad(alpha)
        self.pos_on_screen = [0, 0]
        self.v = v
        self.vx = self.v * math.cos(self.alpha_direct)
        self.vy = -self.v * math.sin(self.alpha_direct)
        self.v_size = v_size
        self.g = g
        self.color = color
        self.suf_particle = None
        self.alpha_suf_particle = rd.randint(70, 230)

    def create_suf(self):
        self.suf_particle = pg.Surface((self.size * 2, self.size * 2)).convert_alpha()
        pg.draw.circle(self.suf_particle, self.color, (self.size, self.size), self.size)
        self.suf_particle.set_alpha(self.alpha_suf_particle)

    def set_pos_start(self, pos_start):
        self.pos = pos_start

    def fly(self):
        pos = [0, 0]
        pos[0] = self.pos[0] + self.vx
        pos[1] = self.pos[1] + self.vy
        self.vy += self.g
        self.pos = pos

    def resize_particle(self):
        self.size -= self.v_size

    def find_on_screen(self, screen):
        self.pos_on_screen[0] = self.pos[0] - screen.x
        self.pos_on_screen[1] = self.pos[1] - screen.y

    def process_total(self, screen):
        self.fly()
        self.resize_particle()
        self.find_on_screen(screen)
        self.create_suf()

    def show(self, suf):
        rect_suf_particle = self.suf_particle.get_rect()
        rect_suf_particle.center = self.pos_on_screen
        suf.blit(self.suf_particle, rect_suf_particle, special_flags=pg.BLEND_RGBA_ADD)


class Particle_4:
    def __init__(self, v, size_start, alpha, case, pos_start, v_size):
        # jet_1
        self.pos = pos_start
        self.size_max = size_start
        self.size = size_start
        self.alpha_direct_rad = deg_to_rad(alpha)
        self.dir_folder = os.path.abspath(os.getcwd())+'/imgs/jet_effect/'
        self.dir_animation_cases = listdir(self.dir_folder)
        self.case_particle = case
        self.animation_cases = []
        self.load_animation()
        self.animation_case = self.animation_cases[self.case_particle]
        self.pos_on_screen = [0, 0]
        self.v = v
        self.vx = self.v * math.cos(self.alpha_direct_rad)
        self.vy = -self.v * math.sin(self.alpha_direct_rad)
        self.v_size = v_size

    def set_pos_start(self, pos_start):
        self.pos = pos_start

    def load_animation(self):
        for dir_case in self.dir_animation_cases:
            dir_animation_case = self.dir_folder + dir_case + '/'
            animation_case = Animation(dir_animation_case, self.size, 0, 1)
            self.animation_cases.append(animation_case)

    def fly(self):
        pos = [0, 0]
        pos[0] = self.pos[0] + self.vx
        pos[1] = self.pos[1] + self.vy
        self.pos = pos

    def resize_particle(self):
        new_size = [1, 1]
        if self.size[0] > 2:
            new_size[0] = self.size[0] - self.v_size
            new_size[1] = self.size[1] - self.v_size
        self.size = new_size
        self.animation_case.resize_imgs([int(self.size[0]), int(self.size[1])])

    def find_on_screen(self, screen):
        self.pos_on_screen[0] = self.pos[0] - screen.x
        self.pos_on_screen[1] = self.pos[1] - screen.y

    def process_total(self, screen):
        self.fly()
        self.resize_particle()
        self.find_on_screen(screen)

    def show(self, suf, runtime):
        self.animation_case.show(suf, runtime, self.pos_on_screen)



