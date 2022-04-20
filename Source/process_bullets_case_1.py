from process_alpha import *
from tv import *
from process_distance import *
from process_animation import Animation
from process_rects import *
from tv import *
from process_effects_2 import Effect_kind_2_2
from colors import *


class OR_1_bullet_0:
    def __init__(self):
        self.pos_start = [0, 0]
        self.pos_end = [0, 0]
        self.alpha = 0
        self.time = 0
        self.v = 12
        self.vx = 0
        self.vy = 0
        self.pos_on_screen = [0, 0]
        self.size = 50, 50
        self.rect_bullet = []
        self.damage = 1
        self.radius_bullet = 2

        # animation
        self.dir_folder_animation = os.path.abspath(os.getcwd())+'/imgs/roles/o_roles/o_role_1/bullet/'
        self.dir_animation_cases = listdir(self.dir_folder_animation)
        self.dir_animation_case = self.dir_animation_cases[0]
        self.animation = Animation(self.dir_folder_animation + self.dir_animation_case + '/', self.size, 0, 7)

    def fire(self, pos_start, pos_end, runtime, alpha):
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

    def check_vs_main_role(self, main_role):
        rect_main_role = main_role.get_rect()
        if check_rect_vs_circle(rect_main_role, self.pos_start, self.radius_bullet):
            main_role.hp_and_mana.hurt(self.damage)
            return True
        else:
            return False

    def check_vs_mr_boxs(self, main_role):
        for box in main_role.skills[1].bullets:
            if box.reached:
                rect_box = box.get_rect()
                if check_rect_vs_circle(rect_box, self.pos_start, self.radius_bullet):
                    box.damage_hp(self.damage)
                    return True
        return False

    def show(self, suf, runtime):
        self.animation.rotate_imgs(self.alpha)
        self.animation.show(suf, runtime, self.pos_on_screen)


class OR_1_bullet_1:
    def __init__(self):
        self.pos_start = [0, 0]
        self.pos_end = [0, 0]
        self.alpha = 0
        self.time = 0
        self.v = 30
        self.vx = 0
        self.vy = 0
        self.pos_on_screen = [0, 0]
        self.size = 50, 50
        self.rect_bullet = []
        self.damage = 7
        self.stt_show = 0
        self.radius_bullet = 8

        # animation
        self.dir_folder_animation = os.path.abspath(os.getcwd())+'/imgs/roles/o_roles/bullet_case_1/'
        self.dir_animation_cases = listdir(self.dir_folder_animation)
        self.dir_animation_case = self.dir_animation_cases[1]
        self.animation = Animation(self.dir_folder_animation + self.dir_animation_case + '/', self.size, 0, 7)

    def fire(self, pos_start, pos_end, runtime, alpha):
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

    def check_vs_main_role(self, main_role):
        rect_main_role = main_role.get_rect()
        if check_rect_vs_circle(rect_main_role, self.pos_start, self.radius_bullet):
            main_role.hp_and_mana.hurt(self.damage)
            return True
        else:
            return False

    def check_vs_mr_boxs(self, main_role):
        for box in main_role.skills[1].bullets:
            if box.reached:
                rect_box = box.get_rect()
                if check_rect_vs_circle(rect_box, self.pos_start, self.radius_bullet):
                    box.damage_hp(self.damage)
                    return True
        return False

    def show(self, suf, runtime):
        if self.stt_show == 1:
            self.animation.rotate_imgs(self.alpha)
            self.animation.show(suf, runtime, self.pos_on_screen)


class OR_1_bullet_2:
    def __init__(self):
        self.pos_start = [0, 0]
        self.pos_end = [0, 0]
        self.alpha = 0
        self.time = 0
        self.v = 3
        self.vx = 0
        self.vy = 0
        self.pos_on_screen = [0, 0]
        self.size = 27, 27
        self.rect_bullet = []
        self.damage = 3
        self.stt_show = 1
        self.v_alpha = 1
        self.radius_bullet = 5

        # animation
        self.dir_folder_animation = os.path.abspath(os.getcwd())+'/imgs/roles/o_roles/bullet_case_1/'
        self.dir_animation_cases = listdir(self.dir_folder_animation)
        self.dir_animation_case = self.dir_animation_cases[2]
        self.animation = Animation(self.dir_folder_animation + self.dir_animation_case + '/', self.size, 0, 7)

        self.eff_jet = Effect_kind_2_2(pos_center_effect=[0, 0], alpha_direct=-90, area_alpha=2, in_out=1,
                                       v_particle_max=5,
                                       size_max=5, size_min=2, v_size=0.3, radius_max_effect=15, rbp=3, g=0, color=red,
                                       color_light=(70, 20, 20), npm=-7, npps=2)

    def fire(self, pos_start, pos_end, runtime, alpha):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.alpha = alpha
        self.time = runtime
        self.vx = self.v * math.cos(deg_to_rad(self.alpha))
        self.vy = -self.v * math.sin(deg_to_rad(self.alpha))

    def process_move(self, screen, main_role):
        self.flying(main_role)
        self.eff_jet.update_poss_alpha_direct(self.pos_start, self.alpha - 180)
        self.eff_jet.process_effect(screen, 1)
        self.find_on_screen(screen)

    def flying(self, main_role):
        alpha_goal = process_alpha_1(self.pos_start, main_role.pos_body)
        if abs(alpha_goal - self.alpha) < self.v_alpha:
            self.alpha = alpha_goal
        else:
            value_alpha = process_alpha_2(self.alpha, alpha_goal)
            self.alpha += value_alpha * self.v_alpha
            self.alpha = process_alpha_plus(self.alpha)

        self.vx = self.v * math.cos(deg_to_rad(self.alpha))
        self.vy = -self.v * math.sin(deg_to_rad(self.alpha))
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

    def check_vs_main_role(self, main_role):
        rect_main_role = main_role.get_rect()
        if check_rect_vs_circle(rect_main_role, self.pos_start, self.radius_bullet):
            main_role.hp_and_mana.hurt(self.damage)
            return True
        else:
            return False

    def check_vs_mr_boxs(self, main_role):
        for box in main_role.skills[1].bullets:
            if box.reached:
                rect_box = box.get_rect()
                if check_rect_vs_circle(rect_box, self.pos_start, self.radius_bullet):
                    box.damage_hp(self.damage)
                    return True
        return False

    def check_vs_mr_normal(self, main_role):
        self.get_rect()
        for bullet in main_role.skills[0].bullets:
            if check_rect_vs_circle(self.rect_bullet, bullet.pos_start, bullet.radius_bullet):
                bullet.vsed = True
                return True

        return False

    def show(self, suf, runtime):
        if self.stt_show == 1:
            self.eff_jet.show(suf)
            self.animation.rotate_imgs(self.alpha)
            self.animation.show(suf, runtime, self.pos_on_screen)


class OR_1_bullet_3:
    def __init__(self):
        self.time = 0
        self.pos_start = [0, 0]
        self.pos_on_screen = [0, 0]
        self.radius = 100
        self.size = 40, 40
        self.time = 0
        self.g = 0.2
        self.vy = 0
        self.damage = 7
        self.rect_bullet = []
        self.stt_show = 0
        self.hp_max = 7
        self.hp = 7

        # animation
        self.dir_folder_animation = os.path.abspath(os.getcwd())+'/imgs/roles/o_roles/o_role_1/bullet/'
        self.dir_animation_cases = listdir(self.dir_folder_animation)
        self.dir_animation_case = self.dir_animation_cases[3]
        self.animation = Animation(self.dir_folder_animation + self.dir_animation_case + '/', self.size, 0, 7)

    def use_skill(self, pos_set):
        self.pos_start = pos_set

    def fall(self):
        pos = [0, 0]
        pos[0] = self.pos_start[0]
        pos[1] = self.pos_start[1] + self.vy
        self.vy += self.g
        self.pos_start = pos

    def find_on_screen(self, screen):
        self.pos_on_screen[0] = self.pos_start[0] - screen.x
        self.pos_on_screen[1] = self.pos_start[1] - screen.y

    def process_move(self, screen, main_role):
        self.fall()
        self.check_vs_mr_normal(main_role)
        self.find_on_screen(screen)

    def get_rect(self):
        self.rect_bullet = [int(self.pos_start[0] - self.size[0] / 2), int(self.pos_start[1] - self.size[1] / 2),
                            self.size[0],
                            self.size[1]]
        return self.rect_bullet

    def check_vs_main_role(self, main_role):
        rect_main_role = main_role.get_rect()
        self.get_rect()
        if not process_1(self.rect_bullet, rect_main_role):
            main_role.hp_and_mana.hurt(self.damage)
            return True
        else:
            return False

    def check_vs_mr_boxs(self, main_role):
        for box in main_role.skills[1].bullets:
            if box.reached:
                rect_box = box.get_rect()
                self.get_rect()
                if not process_1(self.rect_bullet, rect_box):
                    box.damage_hp(self.damage)
                    return True
        return False

    def check_vs_mr_normal(self, main_role):
        self.get_rect()
        for bullet in main_role.skills[0].bullets:
            if check_rect_vs_circle(self.rect_bullet, bullet.pos_start, bullet.radius_bullet):
                bullet.vsed = True
                self.hp -= bullet.damage

    def show(self, suf, runtime):
        if self.stt_show == 1:
            self.animation.show(suf, runtime, self.pos_on_screen)
