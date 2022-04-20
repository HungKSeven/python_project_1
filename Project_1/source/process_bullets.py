from process_alpha import *
from tv import *
from process_distance import *
from process_animation import Animation
from process_rects import *
from tv import *
from colors import *


class MR_bullet_0():
    def __init__(self):
        self.pos_start = [0, 0]
        self.pos_end = [0, 0]
        self.alpha = 0
        self.time = 0
        self.v = 20
        self.vx = 0
        self.vy = 0
        self.pos_on_screen = [0, 0]
        self.size = 40, 40
        self.rect_bullet = []
        self.radius_bullet = 4
        self.vsed = False
        self.damage = 3

        # animation
        self.dir_folder_animation = os.path.abspath(os.getcwd())+'/imgs/roles/main_role/bullet_0/'
        self.animation = None
        self.load_animation()

    def load_animation(self):
        self.animation = Animation(self.dir_folder_animation, self.size, 0, 3)

    def fire(self, pos_start, pos_end, alpha, runtime):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.alpha = alpha
        self.time = runtime
        self.vx = self.v * math.cos(deg_to_rad(self.alpha))
        self.vy = -self.v * math.sin(deg_to_rad(self.alpha))

    def process_move(self, screen):
        self.flying()
        self.find_on_screen(screen)

    def flying(self):
        pos = [0, 0]
        pos[0] = self.pos_start[0] + self.vx
        pos[1] = self.pos_start[1] + self.vy
        self.pos_start = pos

    def find_on_screen(self, screen):
        self.pos_on_screen[0] = self.pos_start[0] - screen.x
        self.pos_on_screen[1] = self.pos_start[1] - screen.y

    def get_rect(self):
        self.rect_bullet = [int(self.pos_start[0] - self.size[0] / 2), int(self.pos_start[1] - self.size[1] / 2),
                            self.size[0],
                            self.size[1]]
        return self.rect_bullet

    def show(self, suf, runtime):
        self.animation.rotate_imgs(self.alpha)
        self.animation.show(suf, runtime, self.pos_on_screen)


class MR_bullet_1:
    def __init__(self, hp):
        self.pos_start = [0, 0]
        self.pos_end = [0, 0]
        self.alpha = 0
        self.time = 0
        self.v = 20
        self.vx = 0
        self.vy = 0
        self.pos_on_screen = [0, 0]
        self.reached = False
        self.size_1 = 30, 30
        self.size_2 = 50, 50
        self.rect_bullet_1 = []
        self.rect_bullet_2 = []
        self.hp_max = hp
        self.hp = hp
        self.alpha_box = 0
        self.v_alpha_box = 3
        self.vsed=False

        # animation
        self.dir_folder_animation = os.path.abspath(os.getcwd())+'/imgs/roles/main_role/bullet_1/'
        self.dir_animatione_case = listdir(self.dir_folder_animation)
        self.animation_cases = []
        self.load_animation()
        self.case_animation = 0
        self.animation_case = self.animation_cases[self.case_animation]

    def damage_hp(self, damage):
        self.hp -= damage

    def load_animation(self):
        for n in range(0, len(self.dir_animatione_case)):
            if n == 0:
                size = self.size_1
            else:
                size = self.size_2
            animatione_case = Animation(self.dir_folder_animation + self.dir_animatione_case[n] + '/', size, 0, 4)
            self.animation_cases.append(animatione_case)

    def fire(self, pos_start, pos_end, alpha, runtime):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.alpha = alpha
        self.alpha_box = alpha
        self.time = runtime
        self.vx = self.v * math.cos(deg_to_rad(self.alpha))
        self.vy = -self.v * math.sin(deg_to_rad(self.alpha))

    def rotate_box(self):
        self.alpha_box -= self.v_alpha_box

    def process_move(self, screen):
        self.flying()
        self.rotate_box()
        self.find_on_screen(screen)

    def flying(self):
        if not self.reached:
            pos = [0, 0]
            pos[0] = self.pos_start[0] + self.vx
            pos[1] = self.pos_start[1] + self.vy
            self.check_reached(pos)

    def check_reached(self, pos):
        if check_in_distance(pos, self.pos_end, 15):
            self.pos_start = self.pos_end
            self.reached = True
            self.case_animation = 1
        else:
            self.pos_start = pos
            self.case_animation = 0

    def find_on_screen(self, screen):
        self.pos_on_screen[0] = self.pos_start[0] - screen.x
        self.pos_on_screen[1] = self.pos_start[1] - screen.y

    def get_rect(self):
        self.rect_bullet_2 = [int(self.pos_start[0] - self.size_2[0] / 2), int(self.pos_start[1] - self.size_2[1] / 2),
                              self.size_2[0],
                              self.size_2[1]]
        return self.rect_bullet_2

    def show(self, suf, runtime):
        self.animation_case = self.animation_cases[self.case_animation]
        if not self.reached:
            self.animation_case.rotate_imgs(self.alpha_box)
        self.animation_case.show(suf, runtime, self.pos_on_screen)

        if self.reached:
            new_rect = pg.Rect((0, 0, self.size_2[0] * 0.6, self.size_2[1] * 0.6))
            new_rect.center = self.pos_on_screen
            hp_pc = 1 - self.hp / self.hp_max
            pg.draw.rect(suf, white, new_rect, 3)
            if hp_pc > 0.25:
                pg.draw.circle(suf, black, self.pos_on_screen, 24, draw_top_right=True)
            if hp_pc >= 0.5:
                pg.draw.circle(suf, black, self.pos_on_screen, 24, draw_bottom_right=True)
            if hp_pc >= 0.75:
                pg.draw.circle(suf, black, self.pos_on_screen, 24, draw_bottom_left=True)
            if hp_pc == 1:
                pg.draw.circle(suf, black, self.pos_on_screen, 24, draw_top_left=True)


class MR_bullet_2():
    def __init__(self):
        self.pos_start = [0, 0]
        self.pos_end = [0, 0]
        self.alpha = 0
        self.time = 0
        self.v = 10
        self.vx = 0
        self.vy = 0
        self.pos_on_screen = [0, 0]
        self.size = 20, 20
        self.rect_bullet = []

        # animation
        self.dir_folder_animation = os.path.abspath(os.getcwd())+'/imgs/roles/main_role/bullet_2/'
        self.animation = None
        self.load_animation()

    def load_animation(self):
        self.animation = Animation(self.dir_folder_animation, self.size, 0, 3)

    def fire(self, pos_start, pos_end, alpha, runtime):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.alpha = alpha
        self.time = runtime
        self.vx = self.v * math.cos(deg_to_rad(self.alpha))
        self.vy = -self.v * math.sin(deg_to_rad(self.alpha))

    def process_move(self, screen):
        self.flying()
        self.find_on_screen(screen)

    def flying(self):
        pos = [0, 0]
        pos[0] = self.pos_start[0] + self.vx
        pos[1] = self.pos_start[1] + self.vy
        self.pos_start = pos

    def find_on_screen(self, screen):
        self.pos_on_screen[0] = self.pos_start[0] - screen.x
        self.pos_on_screen[1] = self.pos_start[1] - screen.y

    def get_rect(self):
        self.rect_bullet = [int(self.pos_start[0] - self.size[0] / 2), int(self.pos_start[1] - self.size[1] / 2),
                            self.size[0],
                            self.size[1]]
        return self.rect_bullet

    def show(self, suf, runtime):
        self.animation.rotate_imgs(self.alpha)
        self.animation.show(suf, runtime, self.pos_on_screen)


class MR_bullet_3:
    def __init__(self):
        self.pos_start = [0, 0]
        self.pos_end = [0, 0]
        self.alpha = 0
        self.time = 0
        self.v = 10
        self.vx = 0
        self.vy = 0
        self.pos_on_screen = [0, 0]
        self.reached = False
        self.size_1 = 20, 20
        self.size_2 = 32, 130
        self.rect_bullet_1 = []
        self.rect_bullet_2 = []

        # animation
        self.dir_folder_animation = os.path.abspath(os.getcwd())+'/imgs/roles/main_role/bullet_3/'
        self.dir_animatione_case = listdir(self.dir_folder_animation)
        self.animation_cases = []
        self.load_animation()
        self.case_animation = 0
        self.animation_case = self.animation_cases[self.case_animation]

    def load_animation(self):
        for n in range(0, len(self.dir_animatione_case)):
            if n == 0:
                size = self.size_1
            else:
                size = self.size_2
            animatione_case = Animation(self.dir_folder_animation + self.dir_animatione_case[n] + '/', size, 0, 4)
            self.animation_cases.append(animatione_case)

    def fire(self, pos_start, pos_end, alpha, runtime):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.alpha = alpha
        self.time = runtime
        self.vx = self.v * math.cos(deg_to_rad(self.alpha))
        self.vy = -self.v * math.sin(deg_to_rad(self.alpha))

    def process_move(self, screen):
        self.flying()
        self.find_on_screen(screen)

    def flying(self):
        if not self.reached:
            pos = [0, 0]
            pos[0] = self.pos_start[0] + self.vx
            pos[1] = self.pos_start[1] + self.vy
            self.check_reached(pos)

    def check_reached(self, pos):
        if check_in_distance(pos, self.pos_end, 13):
            self.pos_start = self.pos_end
            self.reached = True
            self.case_animation = 1
        else:
            self.pos_start = pos
            self.case_animation = 0

    def find_on_screen(self, screen):
        self.pos_on_screen[0] = self.pos_start[0] - screen.x
        self.pos_on_screen[1] = self.pos_start[1] - screen.y

    def get_rect(self):
        self.rect_bullet_2 = [int(self.pos_start[0] - self.size_2[0] / 2), int(self.pos_start[1] - self.size_2[1] / 2),
                              self.size_2[0],
                              self.size_2[1]]
        return self.rect_bullet_2

    def show(self, suf, runtime):
        self.animation_case = self.animation_cases[self.case_animation]
        self.animation_case.show(suf, runtime, self.pos_on_screen)
