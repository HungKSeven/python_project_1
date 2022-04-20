from process_animation import Animation
from tv import *
from colors import *
from process_alpha import *
from process_rects import *
from skills_case_1 import *
from process_distance import *
from process_effects_2 import Effect_kind_2_2


class O_role_1:
    def __init__(self, level, pos):
        self.hps_max = [70, 170, 270]
        self.h_area = 600
        self.radius = 700
        self.pos_body = pos
        self.alpha = -90
        self.radius_eyeball = 5
        self.pos_body_on_scren = [0, 0]
        self.pos_eyeball_on_body = [0, 0]
        self.pos_eyeball = [0, 0]
        self.pos_eyeball_on_screen = [0, 0]
        self.pos_gun_1 = [0, 0]
        self.pos_gun_2 = [0, 0]
        self.pos_gun_3 = [0, 0]
        self.pos_gun_4 = [0, 0]
        self.pos_gun_5 = [0, 0]
        self.pos_gun_1_on_screen = [0, 0]
        self.pos_gun_2_on_screen = [0, 0]
        self.pos_gun_3_on_screen = [0, 0]
        self.pos_gun_4_on_screen = [0, 0]
        self.pos_gun_5_on_screen = [0, 0]

        self.size_body = 34, 34
        self.size_eyeball = 20, 20
        self.size_gun = 230, 230
        self.size_ek1_1 = 25, 25
        self.level = level
        self.dir_folder = os.path.abspath(os.getcwd())+'/imgs/roles/o_roles/o_role_1/'
        self.dir_folder_body = self.dir_folder + 'body/'
        self.dir_folder_eyeball = self.dir_folder + 'eyeball/'
        self.dir_folder_gun = self.dir_folder + 'gun/'
        self.dir_animation_eyeball_levels = listdir(self.dir_folder_eyeball)
        self.dir_animation_eyeball_level = self.dir_folder_eyeball + self.dir_animation_eyeball_levels[self.level] + '/'

        self.dir_animation_gun_cases = listdir(self.dir_folder_gun)
        self.dir_animation_gun_case = self.dir_animation_gun_cases[0]

        self.animation_body = Animation(self.dir_folder_body, self.size_body, 0, 1)
        self.animation_gun = Animation(self.dir_folder_gun + self.dir_animation_gun_case + '/', self.size_gun, 0, 1)

        # load animation
        self.animation_eyeball = Animation(self.dir_animation_eyeball_level, self.size_eyeball, 0, 1)

        self.pass_skill_1 = OR_1_skill_pass_1(self.pos_body)

        self.skills_0 = []
        self.m_skill_1 = OR_1_skill_1()
        self.m_skills_2 = []
        self.m_skill_3 = OR_1_skill_3()
        self.v1_m_skills = []
        self.set_up_skills()
        self.v1_m_skills=[0,0,2]
        self.m_skill_3.ulti_mode=1

        self.on_skill_0 = True
        self.stt_skill_1 = 0
        self.stt_skill_2 = 0
        self.stt_skill_3 = 0

        self.time_use_mana_skill = 0

        self.v_alpha_direct_target = 1

        self.wait_after_skill_1 = 0
        self.wait_after_skill_2 = 0

        self.stt_direct = 0

        self.skill_choosen = 0

        self.hp_max = self.hps_max[self.level]
        self.hp = self.hp_max

        self.rect_body = [0, 0, self.size_body[0], self.size_body[1]]

        self.sleep_on = False

    def damage(self, damage):
        self.hp -= damage

    def set_up_skills(self):
        for n in range(0, 2):
            self.skills_0.append(OR_1_skill_0())
        for n in range(0, 2):
            self.m_skills_2.append(OR_1_skill_2())

        if self.level == 0:
            a = [0, 0, 0]
            b = rd.randint(0, 2)
            a[b] = 1
            opt1 = rd.randint(1, 4)
            if opt1 == 1:
                a[b] = 2
            if opt1 == 2:
                for n in range(0, 2):
                    self.skills_0[n].ulti_mode = 1
        else:
            if self.level == 1:
                a = [1, 1, 1]
                b = rd.randint(0, 2)
                a[b] = 0
                b = rd.randint(0, 2)
                check = False
                if a[b] == 1:
                    a[b] = 2
                    check = True
                if not check:
                    for n in range(0, 2):
                        self.skills_0[n].ulti_mode = 1
            else:
                a = [1, 1, 1]
                b = rd.randint(0, 2)
                a[b] = 2

        if a[2] == 2:
            self.m_skill_3.ulti_mode = 1

        self.v1_m_skills = a

    def find_on_screen(self, screen):
        self.pos_body_on_scren[0] = self.pos_body[0] - screen.x
        self.pos_body_on_scren[1] = self.pos_body[1] - screen.y
        self.pos_eyeball_on_screen[0] = self.pos_eyeball[0] - screen.x
        self.pos_eyeball_on_screen[1] = self.pos_eyeball[1] - screen.y
        self.pos_gun_1_on_screen[0] = self.pos_gun_1[0] - screen.x
        self.pos_gun_1_on_screen[1] = self.pos_gun_1[1] - screen.y
        self.pos_gun_2_on_screen[0] = self.pos_gun_2[0] - screen.x
        self.pos_gun_2_on_screen[1] = self.pos_gun_2[1] - screen.y
        self.pos_gun_3_on_screen[0] = self.pos_gun_3[0] - screen.x
        self.pos_gun_3_on_screen[1] = self.pos_gun_3[1] - screen.y
        self.pos_gun_4_on_screen[0] = self.pos_gun_4[0] - screen.x
        self.pos_gun_4_on_screen[1] = self.pos_gun_4[1] - screen.y
        self.pos_gun_5_on_screen[0] = self.pos_gun_5[0] - screen.x
        self.pos_gun_5_on_screen[1] = self.pos_gun_5[1] - screen.y

    def direct_target(self, pos_target):
        if self.stt_skill_1 == 0 and self.stt_skill_2 == 0:
            alpha_deg = process_alpha_1(self.pos_body, pos_target)
            if abs(alpha_deg - self.alpha) < self.v_alpha_direct_target:
                self.alpha = alpha_deg
                self.stt_direct = 1
            else:
                value_alpha = process_alpha_2(self.alpha, alpha_deg)
                self.alpha += value_alpha * self.v_alpha_direct_target
                self.alpha = process_alpha_plus(self.alpha)
                self.stt_direct = 0

            alpha_rad = deg_to_rad(self.alpha)

            self.animation_gun.rotate_imgs(self.alpha)
            if process_distance_1(self.pos_body, pos_target) > self.radius:
                self.pos_eyeball_on_body = [0, 0]
            else:
                self.pos_eyeball_on_body[0] = round(self.radius_eyeball * math.cos(alpha_rad))
                self.pos_eyeball_on_body[1] = round(self.radius_eyeball * math.sin(alpha_rad))

            self.pos_eyeball[0] = int(self.pos_body[0] + self.pos_eyeball_on_body[0])
            self.pos_eyeball[1] = int(self.pos_body[1] - self.pos_eyeball_on_body[1])

            d_gun_1_2 = 107
            alpha_gun_1_2 = 12
            self.pos_gun_1[0] = self.pos_body[0] + d_gun_1_2 * math.cos(deg_to_rad(self.alpha + alpha_gun_1_2))
            self.pos_gun_1[1] = self.pos_body[1] - d_gun_1_2 * math.sin(deg_to_rad(self.alpha + alpha_gun_1_2))
            self.pos_gun_2[0] = self.pos_body[0] + d_gun_1_2 * math.cos(deg_to_rad(self.alpha - alpha_gun_1_2))
            self.pos_gun_2[1] = self.pos_body[1] - d_gun_1_2 * math.sin(deg_to_rad(self.alpha - alpha_gun_1_2))

            d_gun_3 = 91
            self.pos_gun_3[0] = self.pos_body[0] + d_gun_3 * math.cos(deg_to_rad(self.alpha))
            self.pos_gun_3[1] = self.pos_body[1] - d_gun_3 * math.sin(deg_to_rad(self.alpha))

            d_gun_4_5 = -37
            alpha_gun_4_5 = 50
            self.pos_gun_4[0] = self.pos_body[0] + d_gun_4_5 * math.cos(deg_to_rad(self.alpha + alpha_gun_4_5))
            self.pos_gun_4[1] = self.pos_body[1] - d_gun_4_5 * math.sin(deg_to_rad(self.alpha + alpha_gun_4_5))
            self.pos_gun_5[0] = self.pos_body[0] + d_gun_4_5 * math.cos(deg_to_rad(self.alpha - alpha_gun_4_5))
            self.pos_gun_5[1] = self.pos_body[1] - d_gun_4_5 * math.sin(deg_to_rad(self.alpha - alpha_gun_4_5))

    def choose_m_skill_1(self, runtime):
        if self.v1_m_skills[0] == 1 or self.v1_m_skills[0] == 2:
            if self.skill_choosen == 0:
                if self.stt_direct == 1:
                    if self.v1_m_skills[0] == 1:
                        speed_use = rd.randint(3, 6)
                    else:
                        speed_use = rd.randint(2, 5)
                    if runtime - self.time_use_mana_skill <= speed_use * 1000:
                        self.skill_choosen = 0
                    else:
                        self.skill_choosen = 1
                        self.time_use_mana_skill = runtime

    def choose_m_skill_2(self, runtime):
        if self.v1_m_skills[1] == 1 or self.v1_m_skills[1] == 2:
            if self.skill_choosen == 0:
                if self.stt_direct == 1:
                    if self.v1_m_skills[1] == 1:
                        speed_use = rd.randint(3, 6)
                    else:
                        speed_use = rd.randint(2, 5)
                    if runtime - self.time_use_mana_skill <= speed_use * 1000:
                        self.skill_choosen = 0
                    else:
                        self.skill_choosen = 2
                        self.time_use_mana_skill = runtime

    def use_m_skills(self, pos_target, runtime, rects_room):
        if self.skill_choosen == 1:
            if self.stt_skill_1 == 0:
                self.stt_skill_1 = 1
            self.use_m_skill_1(pos_target, runtime)

        if self.skill_choosen == 2:
            if self.stt_skill_2 == 0:
                self.stt_skill_2 = 1
            self.use_m_skill_2(pos_target, runtime)

        if self.v1_m_skills[2] == 1 or self.v1_m_skills[2] == 2:
            self.use_m_skill_3(pos_target, runtime, rects_room)

    def use_m_skill_1(self, pos_target, runtime):
        if self.stt_skill_1 == 1:
            self.on_skill_0 = False
            self.m_skill_1.use_skill(pos_target, self.pos_gun_3, runtime, self.pos_body, self.alpha)
            self.stt_skill_1 = 2
            self.wait_after_skill_1 = 0

        if self.stt_skill_1 == 2:
            if self.m_skill_1.stt == 1:
                self.wait_after_skill_1 += 1
                if self.wait_after_skill_1 > 30:
                    self.on_skill_0 = True
                    self.stt_skill_1 = 0
                    self.skills_0[0].time = runtime
                    self.skills_0[1].time = runtime
                    self.skill_choosen = 0
                    self.time_use_mana_skill = runtime

    def use_m_skill_2(self, pos_target, runtime):
        if self.stt_skill_2 == 1:
            self.on_skill_0 = False
            alpha_4 = process_alpha_plus(self.alpha - 90)
            alpha_5 = process_alpha_plus(self.alpha + 90)
            self.m_skills_2[0].use_skill(pos_target, self.pos_gun_4, runtime, self.pos_body, alpha_4)
            self.m_skills_2[0].use_skill(pos_target, self.pos_gun_5, runtime, self.pos_body, alpha_5)
            self.stt_skill_2 = 2
            self.wait_after_skill_2 = 0

        if self.stt_skill_2 == 2:
            self.wait_after_skill_2 += 1
            if self.wait_after_skill_2 > 30:
                self.on_skill_0 = True
                self.stt_skill_2 = 0
                self.skills_0[0].time = runtime
                self.skills_0[1].time = runtime
                self.skill_choosen = 0
                self.time_use_mana_skill = runtime

    def use_m_skill_3(self, pos_target, runtime, rects_room):
        if self.stt_skill_3 == 0:
            if self.m_skill_3.use_skill(pos_target, runtime, rects_room) == 1:
                self.stt_skill_3 = 1

        if self.stt_skill_3 == 1:
            if self.m_skill_3.stt == 1:
                self.stt_skill_3 = 0

    def use_skill_0(self, pos_target, runtime):
        if self.on_skill_0:
            if self.stt_direct == 1:
                self.skills_0[0].use_skill(pos_target, self.pos_gun_1, runtime, self.pos_body,
                                           self.alpha)
                self.skills_0[1].use_skill(pos_target, self.pos_gun_2, runtime, self.pos_body,
                                           self.alpha)

    def use_all_skills(self, pos_target, runtime, screen, rects_room):
        if self.v1_m_skills[0] >= self.v1_m_skills[1]:
            self.choose_m_skill_2(runtime)
            self.choose_m_skill_1(runtime)
        else:
            self.choose_m_skill_1(runtime)
            self.choose_m_skill_2(runtime)
        self.use_m_skills(pos_target, runtime, rects_room)
        self.use_skill_0(pos_target, runtime)

    def process_skills(self, screen, rects_room, main_role):
        self.pass_skill_1.process_skill(main_role, self.pos_eyeball_on_screen, self.pos_body_on_scren, screen)
        self.skills_0[0].process_skill(screen, self.pos_body, rects_room, main_role)
        self.skills_0[1].process_skill(screen, self.pos_body, rects_room, main_role)
        self.m_skill_1.process_skill(screen, self.pos_body, rects_room, main_role)
        self.m_skills_2[0].process_skill(screen, self.pos_body, rects_room, main_role)
        self.m_skills_2[1].process_skill(screen, self.pos_body, rects_room, main_role)
        self.m_skill_3.process_skill(screen, self.pos_body, rects_room, main_role, self.pos_eyeball_on_screen)
        self.check_vs_mr_skill_0(main_role)

    def get_rect(self):
        self.rect_body[0] = self.pos_body[0] - self.size_body[0] / 2
        self.rect_body[1] = self.pos_body[1] - self.size_body[1] / 2
        return self.rect_body

    def check_vs_mr_skill_0(self, main_role):
        self.get_rect()
        for bullet in main_role.skills[0].bullets:
            if check_rect_vs_circle(self.rect_body, bullet.pos_start, bullet.radius_bullet):
                bullet.vsed = True
                self.damage(bullet.damage)

    def show(self, suf, runtime):
        pg.draw.circle(suf, black, self.pos_body_on_scren, 33, 6)
        hp_pc = self.hp / self.hp_max
        if hp_pc > 0:
            pg.draw.circle(suf, red, self.pos_body_on_scren, 31, 2, draw_top_left=True)
        if hp_pc > 0.25:
            pg.draw.circle(suf, red, self.pos_body_on_scren, 31, 2, draw_bottom_left=True)
        if hp_pc > 0.5:
            pg.draw.circle(suf, red, self.pos_body_on_scren, 31, 2, draw_bottom_right=True)
        if hp_pc > 0.75:
            pg.draw.circle(suf, red, self.pos_body_on_scren, 31, 2, draw_top_right=True)

        for skill_0 in self.skills_0:
            skill_0.show_skill(suf, runtime)

        self.m_skill_1.show_skill(suf, runtime)

        for m_skill_2 in self.m_skills_2:
            m_skill_2.show_skill(suf, runtime)

        self.animation_gun.show(suf, runtime, self.pos_body_on_scren)
        self.animation_body.show(suf, runtime, self.pos_body_on_scren)
        self.animation_eyeball.show(suf, runtime, self.pos_eyeball_on_screen)

        self.m_skill_3.show_skill(suf, runtime)

        self.pass_skill_1.show(suf)

        # pg.draw.circle(suf, red, self.pos_gun_1_on_screen, 2)
        # pg.draw.circle(suf, blue, self.pos_gun_2_on_screen, 2)
        '''pg.draw.circle(suf, blue, self.pos_gun_3_on_screen, 2)
        pg.draw.circle(suf, blue, self.pos_gun_3_on_screen, 15, 1)'''
        # pg.draw.circle(suf, red, self.pos_gun_4_on_screen, 2)
        # pg.draw.circle(suf, blue, self.pos_gun_5_on_screen, 2)
