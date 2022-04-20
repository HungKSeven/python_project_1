from process_animation import Animation
from tv import *
from process_effects_2 import Effect_kind_2_3
from colors import *


class Thing_1:
    def __init__(self):
        self.name = 'nap'
        self.pos = [0, 0]
        self.case = 6
        self.size = 100, 120
        self.dir_folder_thing_1 = os.path.abspath(os.getcwd())+'/imgs/things/thing_1/'
        self.dir_animation_cases = listdir(self.dir_folder_thing_1)
        print(self.dir_animation_cases);
        self.animation_cases = []
        self.load_animation()
        self.stt_use = 1
        self.time = 0
        self.y_role = 0
        self.y2_role = 0
        self.pos_on_screen = [0, 0]
        self.pos_ef1 = [0, 0]
        self.using = False
        self.opt_add_ef1 = 0
        self.ef1 = Effect_kind_2_3(pos_center_effect=self.pos, alpha_direct=90, d_effect=60, v_particle_max=2,
                                   size_max=6, size_min=1, v_size=0.1, radius_max_effect=0, rbp=1, g=0, color=white,
                                   color_light=(20, 20, 20),npm=-7,npps=1)

    def load_animation(self):
        for dir_case in self.dir_animation_cases:
            animation_case = Animation(self.dir_folder_thing_1 + dir_case + '/', self.size, 0, 3)
            self.animation_cases.append(animation_case)

    def show(self, suf, runtime):
        self.ef1.show(suf)
        self.animation_cases[self.case].show(suf, runtime, self.pos_on_screen)

    def run_events(self, role, runtime):
        if self.stt_use == 1:
            self.event_1_use(role, runtime)
        if self.stt_use == 2:
            self.event_2_use(role, runtime)
        if self.stt_use == 3:
            self.event_3_use(role, runtime)
            self.opt_add_ef1 = 1
        else:
            self.opt_add_ef1 = 0
        if self.stt_use == 4:
            self.event_4_use(role, runtime)

    def event_1_use(self, role, runtime):
        if self.pos[0] - 20 <= role.pos_body[0] <= self.pos[0] + 20:
            if self.pos[1] - 10 <= role.pos_body[1] - 20 <= self.pos[1] + 10:
                self.using = True
                if role.case_power != 5:
                    role.can_control = False
                    self.time = runtime
                    self.y_role = role.pos_body[1]
                    self.stt_use = 2
                    role.runtime_event_1 = runtime + 4000
        else:
            self.using = False

    def event_2_use(self, role, runtime):
        role.reset_stt()
        role.flying = True
        if runtime - self.time < 600:
            role.pos_body[0] = self.pos[0]
            role.pos_body[1] = self.y_role - int(round(1.5 * (runtime - self.time) / 100))
        else:
            self.stt_use = 3
            self.time = runtime
            self.y2_role = role.pos_body[1]

    def event_3_use(self, role, runtime):
        self.case = role.case_power
        if runtime - self.time >= 3000:
            self.stt_use = 4
            role.case_power = 5
            self.time = runtime

    def event_4_use(self, role, runtime):
        if runtime - self.time < 600:
            role.pos_body[1] = self.y2_role + int(round(1.5 * (runtime - self.time) / 100))
        else:
            self.stt_use = 1
            self.case = 6
            role.pos_body[1] = self.y_role
            role.can_control = True
            role.stt_onair = True
            role.flying = False
            role.vy = 0

    def reset_time(self, runtime):
        if runtime < self.time:
            self.time = runtime

    def find_on_screen(self, screen):
        self.pos_on_screen[0] = self.pos[0] - screen.x
        self.pos_on_screen[1] = self.pos[1] - screen.y
        self.pos_ef1[0] = self.pos[0]
        self.pos_ef1[1] = self.pos[1] + 50
        self.ef1.update_poss_alpha_direct(self.pos_ef1, 90)
        self.ef1.process_effect(screen, self.opt_add_ef1)


class Thing_3:
    def __init__(self):
        self.name = 'tivi'
        self.pos = [0, 0]
        self.case = rd.randint(0, 2)
        self.size = 75, 120
        self.dir_folder_thing_3 = os.path.abspath(os.getcwd())+'/imgs/things/thing_3/'
        self.dir_animation_cases = listdir(self.dir_folder_thing_3)
        self.animation_cases = []
        self.load_animation()
        self.time = 0
        self.pos_on_screen = [0, 0]

    def load_animation(self):
        for dir_case in self.dir_animation_cases:
            animation_case = Animation(self.dir_folder_thing_3 + dir_case + '/', self.size, 0, 3)
            self.animation_cases.append(animation_case)

    def show(self, suf, runtime):
        self.animation_cases[self.case].show(suf, runtime, self.pos_on_screen)

    def reset_time(self, runtime):
        if runtime < self.time:
            self.time = runtime

    def run_events(self, runtime):
        self.event_1(runtime)

    def event_1(self, runtime):
        if runtime - self.time > 5000:
            self.case = rd.randint(0, 2)
            self.time = runtime

    def find_on_screen(self, screen):
        self.pos_on_screen[0] = self.pos[0] - screen.x
        self.pos_on_screen[1] = self.pos[1] - screen.y


class Thing_2:
    def __init__(self, case, pos):
        self.name = 'gift'
        self.pos = pos
        self.case = case
        self.size = 50, 50
        self.dir_folder_thing_2 = os.path.abspath(os.getcwd())+'/imgs/things/thing_2/'
        self.dir_animation_cases = listdir(self.dir_folder_thing_2)
        self.animation_cases = []
        self.load_animation()
        self.time = 0
        self.pos_on_screen = [0, 0]
        self.stt_move = 1
        self.v_fall = 1
        self.stt = 1

    def event_1(self, main_role):
        if self.stt == 1:
            if self.pos[1] - 5 <= main_role.pos_body[1] + 12 <= self.pos[1] + 5:
                if self.pos[0] - 20 <= main_role.pos_body[0] <= self.pos[0] + 20:
                    self.stt = 2

    def load_animation(self):
        for dir_case in self.dir_animation_cases:
            animation_case = Animation(self.dir_folder_thing_2 + dir_case + '/', self.size, 0, 3)
            self.animation_cases.append(animation_case)

    def show(self, suf, runtime):
        if self.stt == 1:
            self.animation_cases[self.case].show(suf, runtime, self.pos_on_screen)

    def reset_time(self, runtime):
        if runtime < self.time:
            self.time = runtime

    def find_on_screen(self, screen):
        self.pos_on_screen[0] = self.pos[0] - screen.x
        self.pos_on_screen[1] = self.pos[1] - screen.y
