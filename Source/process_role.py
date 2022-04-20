from process_animation import Animation
from tv import *
from colors import *
from process_alpha import *
from process_rects import *
from process_effects_1 import Effect_kind_1
from skills import MR_skill_0, MR_skill_1, MR_skill_2, MR_skill_3
from hp_and_mana import Hp_Mana_main_role
from process_effects_2 import Effect_kind_2_6
from process_distance import *


class Main_role:
    def __init__(self):
        # mana
        self.hp_and_mana = Hp_Mana_main_role()

        # jet effect
        self.jet_effect = Effect_kind_2_6(pos_center_effect=[0, 0], alpha_direct=-90, area_alpha=0,
                                          v_particle_max=5, case=0,
                                          size_max=60, size_min=39, v_size=7, rbp=1)

        self.opt_add_jet_ef = 0
        self.alpha_jet_ef = 0

        # time
        self.runtime_event_1 = 0

        # main role room
        self.room = None
        self.can_control = True
        self.can_control_hand = False
        self.can_use_skill = False

        # pos
        self.pos_body = [0, 0]
        self.pos_body_on_screen = [0, 0]
        self.pos_effect_1_onbody = 0, -30
        self.pos_hand_onbody = 0, -20
        self.pos_hand = [0, 0]
        self.pos_effect_1 = [0, 0]
        self.pos_hand_on_screen = [0, 0]
        self.pos_effect_1_on_screen = [0, 0]

        self.pos_end_hand = [0, 0]
        self.pos_end_hand_on_screen = [0, 0]
        self.alpha_hand = 0
        self.alpha_legball = 0
        self.pos_leg_onbody = [0, 0]
        self.pos_leg = [0, 0]
        self.pos_leg_on_screen = [0, 0]
        self.v_alpha_leg = 18

        # van toc
        self.v_walk = 5
        self.v_jump = -10
        self.g = 0.3
        self.vy = 0
        self.y_down = 0

        # stt move
        self.flying = False
        self.jumping = False
        self.stt_onair = True
        self.stt_jump = 1
        self.stt_walk_right = False
        self.stt_walk_left = False
        self.time_jump = 0

        # dir animation
        self.case_power = 5
        self.case_body = 0
        self.case_hand = 0
        self.dir_folder = os.path.abspath(os.getcwd())+'/imgs/roles/main_role'
        self.dir_animation_body_cases = listdir(self.dir_folder + '/body/')
        self.dir_animation_hand_cases = listdir(self.dir_folder + '/hand/')
        self.dir_animation_leg = self.dir_folder + '/legball/'
        self.size_legball = (24, 24)
        self.size_body_1 = (40, 72)
        self.size_body_2 = (42, 72)
        self.size_hand_1 = (85, 85)
        self.size_hand_2 = (90, 90)
        self.rect_hitbox = [0, 0, 41, 72]

        # animation
        self.animation_body_cases = []
        self.animation_hand_cases = []
        self.animation_leg = None
        self.load_animation()
        self.animation_body_case = self.animation_body_cases[self.case_body]
        self.animation_hand_case = self.animation_hand_cases[self.case_hand]

        self.skills = []
        self.clock_skill = False * 6
        self.skills.append(MR_skill_0())
        self.skills.append(MR_skill_1())
        self.skills.append(MR_skill_2())
        self.skills.append(MR_skill_3())

        self.vsed_skill_1 = False

    def load_animation(self):
        for n in range(0, len(self.dir_animation_body_cases)):
            dir_body_case = self.dir_animation_body_cases[n]
            if n == 0:
                size_body = self.size_body_1
            else:
                size_body = self.size_body_2
            animation_body_case = Animation(self.dir_folder + '/body/' + dir_body_case + '/',
                                            size_body, 0, 1)
            self.animation_body_cases.append(animation_body_case)

        for n in range(0, len(self.dir_animation_hand_cases)):
            dir_hand_case = self.dir_animation_hand_cases[n]
            if n != 1:
                size_hand = self.size_hand_1
            else:
                size_hand = self.size_hand_2
            animation_hand_case = Animation(self.dir_folder + '/hand/' + dir_hand_case + '/',
                                            size_hand, 0, 1)
            self.animation_hand_cases.append(animation_hand_case)

            self.animation_leg = Animation(self.dir_animation_leg, self.size_legball, 0, 1)

    def process_event_move(self, events, runtime):
        if self.can_control:
            for event in events:
                # walk right
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_d:
                        self.stt_walk_right = True
                if event.type == pg.KEYUP:
                    if event.key == pg.K_d:
                        self.stt_walk_right = False
                # walk Left
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        self.stt_walk_left = True
                if event.type == pg.KEYUP:
                    if event.key == pg.K_a:
                        self.stt_walk_left = False
                # jump
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w:
                        self.jumping = True
                        self.time_jump = runtime
                if event.type == pg.KEYUP:
                    if event.key == pg.K_w:
                        self.jumping = False
                        self.stt_jump = 1

    def process_jumping(self, runtime):
        if self.jumping:
            if not self.stt_onair:
                if self.stt_jump == 1:
                    self.stt_jump = 2
                    self.time_jump = runtime
                if self.stt_jump == 2:
                    if runtime - self.time_jump > 23:
                        self.stt_onair = True
                        self.stt_jump = 1
                        self.vy = self.v_jump

    def process_case_body(self):
        if not self.stt_onair:
            if self.stt_walk_right:
                if self.stt_jump == 2:
                    if self.stt_walk_left:
                        self.case_body = 3
                    else:
                        self.case_body = 4
                else:
                    if self.stt_walk_left:
                        self.case_body = 0
                    else:
                        self.case_body = 1

            if self.stt_walk_left:
                if self.stt_jump == 2:
                    if self.stt_walk_right:
                        self.case_body = 3
                    else:
                        self.case_body = 5
                else:
                    if self.stt_walk_right:
                        self.case_body = 0
                    else:
                        self.case_body = 2
            if not self.stt_walk_right and not self.stt_walk_left:
                if self.stt_jump == 2:
                    self.case_body = 3
                else:
                    self.case_body = 0
        else:
            if self.stt_walk_right:
                if self.stt_walk_left:
                    self.case_body = 0
                else:
                    self.case_body = 1

            if self.stt_walk_left:
                if self.stt_walk_right:
                    self.case_body = 0
                else:
                    self.case_body = 2
            if not self.stt_walk_right and not self.stt_walk_left:
                self.case_body = 0

    def update_poss_onbody(self):
        if self.case_body == 0:
            self.pos_hand_onbody = 0, -10
            self.pos_leg_onbody = 0, 24

        if self.case_body == 1:
            self.pos_hand_onbody = 0, -10
            self.pos_leg_onbody = -8, 24

        if self.case_body == 2:
            self.pos_hand_onbody = 0, -10
            self.pos_leg_onbody = 8, 24

        if self.case_body == 3:
            self.pos_hand_onbody = 0, -10
            self.pos_leg_onbody = 0, 24

        if self.case_body == 4:
            self.pos_hand_onbody = 0, -10
            self.pos_leg_onbody = -6, 24

        if self.case_body == 5:
            self.pos_hand_onbody = 0, -10
            self.pos_leg_onbody = 7, 23

        if self.stt_onair:
            if self.case_body == 1:
                self.pos_effect_1_onbody = -10, -3
                self.opt_add_jet_ef = 1
                self.alpha_jet_ef = 180
            if self.case_body == 2:
                self.pos_effect_1_onbody = 10, -3
                self.opt_add_jet_ef = 1
                self.alpha_jet_ef = 0
            if self.case_body == 0:
                self.opt_add_jet_ef = 0
        else:
            self.opt_add_jet_ef = 0

    def rect_test(self, pos_body_check):
        self.rect_hitbox[0] = pos_body_check[0] - int(round(self.rect_hitbox[2] / 2))
        self.rect_hitbox[1] = pos_body_check[1] - int(round(self.rect_hitbox[3] / 2))

    def get_rect(self):
        x_rect = self.pos_body[0] - int(round(self.rect_hitbox[2] / 2))
        y_rect = self.pos_body[1] - int(round(self.rect_hitbox[3] / 2))
        return [x_rect, y_rect, self.rect_hitbox[2], self.rect_hitbox[3]]

    def check_vs_skill_1(self):
        rect_hb = self.get_rect()
        self.vsed_skill_1 = False
        for bullet in self.skills[1].bullets:
            if bullet.reached:
                rect_bullet = bullet.get_rect()
                if not process_1(rect_hb, rect_bullet):
                    self.vsed_skill_1 = True

    def check_move_vs_skill_1(self):
        if not self.vsed_skill_1:
            for bullet in self.skills[1].bullets:
                if bullet.reached:
                    rect_bullet = bullet.get_rect()
                    if not process_1(self.rect_hitbox, rect_bullet):
                        return True
            return False
        else:
            return False

    def check_move(self, rects_box, pos_body_check):
        self.rect_test(pos_body_check)
        if check_in_rects_room(self.rect_hitbox, rects_box) and not self.check_move_vs_skill_1():
            self.pos_body = pos_body_check
            return True
        else:
            return False

    def process_walking(self, rect):
        pos_body_check = [0, 0]
        if self.stt_walk_right:
            pos_body_check[0] = self.pos_body[0] + self.v_walk
            pos_body_check[1] = self.pos_body[1]
            self.alpha_legball -= self.v_alpha_leg
            if not self.check_move(rect, pos_body_check):
                x_pos = pos_body_check[0]
                for dx in range(0, self.v_walk):
                    pos_body_check[0] = x_pos - dx
                    pos_body_check[1] = self.pos_body[1]
                    if self.check_move(rect, pos_body_check):
                        break

        if self.stt_walk_left:
            pos_body_check[0] = self.pos_body[0] - self.v_walk
            pos_body_check[1] = self.pos_body[1]
            self.alpha_legball += self.v_alpha_leg
            if not self.check_move(rect, pos_body_check):
                x_pos = pos_body_check[0]
                for dx in range(0, self.v_walk):
                    pos_body_check[0] = x_pos + dx
                    pos_body_check[1] = self.pos_body[1]
                    if self.check_move(rect, pos_body_check):
                        break

    def process_fall(self, rect, runtime):
        pos_body_check = [0, 0]
        if not self.flying:
            if self.stt_onair:
                pos_body_check[0] = self.pos_body[0]
                pos_body_check[1] = self.pos_body[1] + self.vy
                self.vy += self.g
                if not self.check_move(rect, pos_body_check):
                    y_stop = pos_body_check[1]
                    if self.vy >= 0:
                        for dy in range(0, int(round(self.vy))):
                            pos_body_check[0] = self.pos_body[0]
                            pos_body_check[1] = y_stop - dy
                            if self.check_move(rect, pos_body_check):
                                break
                    else:
                        for dy in range(0, abs(int(round(self.vy)))):
                            pos_body_check[0] = self.pos_body[0]
                            pos_body_check[1] = y_stop + dy
                            if self.check_move(rect, pos_body_check):
                                break
                    self.stt_onair = False

            else:
                pos_body_check[0] = self.pos_body[0]
                pos_body_check[1] = self.pos_body[1] + 1
                if self.check_move(rect, pos_body_check):
                    self.stt_onair = True
                    self.vy = 0

    def update_poss(self):
        self.pos_hand[0] = self.pos_body[0] + self.pos_hand_onbody[0]
        self.pos_hand[1] = self.pos_body[1] + self.pos_hand_onbody[1]
        self.pos_leg[0] = self.pos_body[0] + self.pos_leg_onbody[0]
        self.pos_leg[1] = self.pos_body[1] + self.pos_leg_onbody[1]
        self.pos_effect_1[0] = self.pos_body[0] + self.pos_effect_1_onbody[0]
        self.pos_effect_1[1] = self.pos_body[1] + self.pos_effect_1_onbody[1]

    def find_poss_on_screen(self, screen):
        self.pos_body_on_screen[0] = self.pos_body[0] - screen.x
        self.pos_body_on_screen[1] = self.pos_body[1] - screen.y
        self.pos_hand_on_screen[0] = self.pos_hand[0] - screen.x
        self.pos_hand_on_screen[1] = self.pos_hand[1] - screen.y
        self.pos_leg_on_screen[0] = self.pos_leg[0] - screen.x
        self.pos_leg_on_screen[1] = self.pos_leg[1] - screen.y
        self.pos_effect_1_on_screen[0] = self.pos_effect_1[0] - screen.x
        self.pos_effect_1_on_screen[1] = self.pos_effect_1[1] - screen.y

    def process_move(self, events, runtime, rects_box, screen):
        self.process_event_move(events, runtime)
        self.process_case_body()
        self.check_vs_skill_1()
        self.process_jumping(runtime)
        self.update_poss_onbody()
        self.process_walking(rects_box)
        self.process_fall(rects_box, runtime)
        self.update_poss()
        self.find_poss_on_screen(screen)
        self.jet_effect.update_poss_alpha_direct(self.pos_effect_1, self.alpha_jet_ef)
        self.jet_effect.process_effect(screen, self.opt_add_jet_ef)
        self.roll_leg()

    def run_events(self, runtime):
        self.event_1(runtime)

    def event_1(self, runtime):
        if self.case_power == 5:
            if runtime - self.runtime_event_1 >= rd.randint(5, 8) * 1000:
                self.case_power = rd.randint(0, 4)
                self.runtime_event_1 = runtime

    def reset_stt(self):
        self.flying = False
        self.jumping = False
        self.stt_onair = True
        self.stt_jump = 1
        self.stt_walk_right = False
        self.stt_walk_left = False

    def reset_time(self, runtime):
        if runtime < self.runtime_event_1:
            self.runtime_event_1 = runtime
        if runtime < self.time_jump:
            self.time_jump = runtime

    def roll_leg(self):
        if self.alpha_legball == 360:
            self.alpha_legball = 0
        if self.alpha_legball == -360:
            self.alpha_legball = 0
        self.animation_leg.rotate_imgs(self.alpha_legball)

    def direct_gun(self, value_direct, opt):
        # 1: mouse 2:alpha
        if self.can_control_hand:
            if opt == 1:
                self.alpha_hand = process_alpha_1(self.pos_hand_on_screen, value_direct)
            else:
                if opt == 2:
                    self.alpha_hand = value_direct
        else:
            self.alpha_hand = -90
        alpha_rad = deg_to_rad(self.alpha_hand)
        self.pos_end_hand[0] = int(self.pos_hand[0] + round(math.cos(alpha_rad) * 37))
        self.pos_end_hand[1] = int(self.pos_hand[1] - round(math.sin(alpha_rad) * 37))
        self.animation_hand_case = self.animation_hand_cases[self.case_hand]
        self.animation_hand_case.rotate_imgs(self.alpha_hand)

    def use_skills(self, events, pos_mouse, runtime, screen, check_fire):
        if self.can_use_skill:
            for event in events:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if pg.mouse.get_pressed(3)[0] == 1:
                        self.on_effect_2 = self.skills[1].use_skill_1(pos_mouse, self.pos_end_hand, runtime,
                                                                      self.alpha_hand, screen,
                                                                      self.pos_body_on_screen, self.hp_and_mana)

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        self.skills[2].use_skill_2(pos_mouse, self.pos_end_hand, runtime, self.alpha_hand,
                                                   screen,
                                                   self.pos_body_on_screen, self.hp_and_mana)

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_e:
                        self.skills[3].use_skill_3(pos_mouse, self.pos_end_hand, runtime,
                                                   self.alpha_hand, screen,
                                                   self.pos_body_on_screen, self.hp_and_mana)

            if check_fire:
                self.on_effect_2 = self.skills[0].use_skill_0(pos_mouse, self.pos_end_hand, runtime, self.alpha_hand,
                                                              screen,
                                                              self.pos_body_on_screen)

    def process_skills(self, screen, rects_room, runtime):
        self.skills[0].process_skill(screen, self.pos_body, rects_room)
        self.skills[1].process_skill(screen, self.pos_body, rects_room, runtime)
        self.skills[2].process_skill(screen, self.pos_body, rects_room)
        self.skills[3].process_skill(screen, self.pos_body, rects_room, runtime)

    def show_power(self, suf):
        colors_power = [red, yellow, green, blue, purple, white]
        color_power = colors_power[self.case_power]
        pg.draw.circle(suf, color_power, self.pos_hand_on_screen, 5)

    def show(self, suf, runtime):
        self.animation_body_case = self.animation_body_cases[self.case_body]
        self.animation_hand_case = self.animation_hand_cases[self.case_hand]

        self.jet_effect.show(suf, runtime)

        self.animation_leg.show(suf, runtime, self.pos_leg_on_screen)
        self.animation_body_case.show(suf, runtime, self.pos_body_on_screen)
        self.show_power(suf)
        self.animation_hand_case.show(suf, runtime, self.pos_hand_on_screen)

        self.skills[1].show_skill(suf, runtime)
        self.skills[0].show_skill(suf, runtime)
        self.skills[2].show_skill(suf, runtime)
        self.skills[3].show_skill(suf, runtime)


        # pg.draw.rect(suf, red, self.rect_hitbox, 1)


class SP_role:
    def __init__(self):
        # time
        self.runtime_event_1 = 0

        self.can_control = True
        self.can_control_hand = False
        self.can_use_skill = False

        # pos
        self.pos_body = [0, 0]
        self.pos_body_on_screen = [0, 0]
        self.pos_hand_onbody = 0, -20
        self.pos_hand = [0, 0]
        self.pos_hand_on_screen = [0, 0]
        self.pos_leg_onbody = [0, 0]
        self.pos_leg = [0, 0]
        self.pos_leg_on_screen = [0, 0]

        # van toc
        self.v_jump = -10
        self.g = 0.3
        self.vy = 0
        self.y_down = 0

        # stt move
        self.flying = False
        self.jumping = False
        self.stt_onair = True

        # dir animation
        self.case_power = 5
        self.case_body = 0
        self.case_hand = 0
        self.case_effect_1 = 0
        self.dir_folder = os.path.abspath(os.getcwd())+'/imgs/roles/sp_role'
        self.dir_animation_body_cases = listdir(self.dir_folder + '/body/')
        self.dir_animation_hand_cases = listdir(self.dir_folder + '/hand/')
        self.dir_animation_leg = self.dir_folder + '/legball/'
        self.size_legball = (24, 24)
        self.size_body = (40, 72)
        self.size_hand = (85, 85)
        self.rect_hitbox = [0, 0, 41, 72]

        # animation
        self.animation_body_cases = []
        self.animation_hand_cases = []
        self.animation_leg = None
        self.load_animation()
        self.animation_body_case = self.animation_body_cases[self.case_body]
        self.animation_hand_case = self.animation_hand_cases[self.case_hand]

    def load_animation(self):
        for n in range(0, len(self.dir_animation_body_cases)):
            dir_body_case = self.dir_animation_body_cases[n]
            animation_body_case = Animation(self.dir_folder + '/body/' + dir_body_case + '/',
                                            self.size_body, 0, 1)
            self.animation_body_cases.append(animation_body_case)

        for n in range(0, len(self.dir_animation_hand_cases)):
            dir_hand_case = self.dir_animation_hand_cases[n]
            animation_hand_case = Animation(self.dir_folder + '/hand/' + dir_hand_case + '/',
                                            self.size_hand, 0, 1)
            self.animation_hand_cases.append(animation_hand_case)

            self.animation_leg = Animation(self.dir_animation_leg, self.size_legball, 0, 1)

    def update_poss_onbody(self):
        if self.case_body == 0:
            self.pos_hand_onbody = 0, -10
            self.pos_leg_onbody = 0, 24

    def rect_test(self, pos_body_check):
        self.rect_hitbox[0] = pos_body_check[0] - int(round(self.rect_hitbox[2] / 2))
        self.rect_hitbox[1] = pos_body_check[1] - int(round(self.rect_hitbox[3] / 2))

    def get_rect(self):
        self.rect_hitbox[0] = self.pos_body[0] - int(round(self.rect_hitbox[2] / 2))
        self.rect_hitbox[1] = self.pos_body[1] - int(round(self.rect_hitbox[3] / 2))

    def check_move(self, rects_box, pos_body_check):
        self.rect_test(pos_body_check)
        if check_in_rects_room(self.rect_hitbox, rects_box):
            self.pos_body = pos_body_check
            return True
        else:
            return False

    def process_fall(self, rect):
        pos_body_check = [0, 0]
        if not self.flying:
            if self.stt_onair:
                pos_body_check[0] = self.pos_body[0]
                pos_body_check[1] = self.pos_body[1] + int(round(self.vy))
                self.vy += self.g
                if not self.check_move(rect, pos_body_check):
                    y_stop = pos_body_check[1]
                    if self.vy >= 0:
                        for dy in range(0, int(self.vy)):
                            pos_body_check[0] = self.pos_body[0]
                            pos_body_check[1] = y_stop - dy
                            if self.check_move(rect, pos_body_check):
                                break
                    else:
                        for dy in range(int(self.vy), 0):
                            pos_body_check[0] = self.pos_body[0]
                            pos_body_check[1] = y_stop + dy
                            if self.check_move(rect, pos_body_check):
                                break
                    self.stt_onair = False
            else:
                pos_body_check[0] = self.pos_body[0]
                pos_body_check[1] = self.pos_body[1] + 2
                if self.check_move(rect, pos_body_check):
                    self.stt_onair = True
                    self.vy = 0

    def update_poss(self):
        self.pos_hand[0] = self.pos_body[0] + self.pos_hand_onbody[0]
        self.pos_hand[1] = self.pos_body[1] + self.pos_hand_onbody[1]
        self.pos_leg[0] = self.pos_body[0] + self.pos_leg_onbody[0]
        self.pos_leg[1] = self.pos_body[1] + self.pos_leg_onbody[1]

    def find_poss_on_screen(self, screen):
        self.pos_body_on_screen[0] = self.pos_body[0] - screen.x
        self.pos_body_on_screen[1] = self.pos_body[1] - screen.y
        self.pos_hand_on_screen[0] = self.pos_hand[0] - screen.x
        self.pos_hand_on_screen[1] = self.pos_hand[1] - screen.y
        self.pos_leg_on_screen[0] = self.pos_leg[0] - screen.x
        self.pos_leg_on_screen[1] = self.pos_leg[1] - screen.y

    def process_move(self, rects_box, screen):
        self.update_poss_onbody()
        self.process_fall(rects_box)
        self.update_poss()
        self.find_poss_on_screen(screen)

    def run_events(self, runtime):
        self.event_1(runtime)

    def event_1(self, runtime):
        if self.case_power == 5:
            if runtime - self.runtime_event_1 >= rd.randint(5, 8) * 1000:
                self.case_power = rd.randint(0, 4)
                self.runtime_event_1 = runtime

    def reset_stt(self):
        self.flying = False
        self.jumping = False
        self.stt_onair = True

    def reset_time(self, runtime):
        if runtime < self.runtime_event_1:
            self.runtime_event_1 = runtime

    def show_power(self, suf):
        colors_power = [red, yellow, green, blue, purple, white]
        color_power = colors_power[self.case_power]
        pg.draw.circle(suf, color_power, self.pos_hand_on_screen, 5)

    def show(self, suf, runtime):
        self.animation_body_case = self.animation_body_cases[self.case_body]
        self.animation_hand_case = self.animation_hand_cases[self.case_hand]
        self.animation_leg.show(suf, runtime, self.pos_leg_on_screen)
        self.animation_body_case.show(suf, runtime, self.pos_body_on_screen)
        self.show_power(suf)
        self.animation_hand_case.show(suf, runtime, self.pos_hand_on_screen)
