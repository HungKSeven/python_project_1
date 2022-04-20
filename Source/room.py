from tv import *
from colors import *
from thing import *
from maps import Map
from process_rects import *
from process_animation import Animation
from process_role import SP_role
from process_o_roles import O_role_1
from process_distance import *


class Rooms():
    def __init__(self):
        self.room_case = 1
        # rect_box_room
        self.rects_room = []
        self.rect_room = [100, 230, 1166, 300]
        self.y_ground = self.rect_room[1] + self.rect_room[3]

        # things_1
        self.num_thing_1 = 7
        self.things_1 = []
        self.load_animation_things_1()
        self.poss_thing_1 = []
        self.create_poss_thing_1()
        self.set_poss_things_1()

        # thing_3
        self.num_thing_3 = 7
        self.things_3 = []
        self.load_animation_things_3()
        self.poss_thing_3 = []
        self.create_poss_thing_3()
        self.set_poss_things_3()

        # main_role_pos
        self.start_pos_mainrole = [self.poss_thing_3[6][0], self.y_ground - 50]

        self.check_event_1_room = False
        self.rect_way = [1166, 530, 400, 0]
        self.stt_event_1_room = 1
        self.check_change_1 = True
        self.time_check = 0
        self.x_gate = 1366

        self.check_change_room = False
        self.room_change_to = 0
        self.rects_room_on_screen = []
        self.rect_tower = [1466, 530 - 13980, 1166, 13980]

        # things_2:
        self.num_thing_2 = 5
        self.things_2 = []
        self.poss_thing_2 = []
        self.create_poss_thing_2()
        self.load_things_2()

        # sp_roles
        self.num_sp_roles = 6
        self.sp_roles = []
        self.poss_sp_roles = []
        self.create_poss_sp_roles()
        self.load_sp_role_1()
        self.set_poss_sp_roles()

        self.o_roles = []
        self.create_o_roles()

    def create_o_roles(self):
        # create case 6
        self.o_roles.append(O_role_1(1, [2300, 100]))

    def create_poss_sp_roles(self):
        start_x = 200
        step_x = 160
        h_vs_ground = 58
        for n in range(0, self.num_sp_roles):
            pos = [start_x + n * step_x, self.y_ground - h_vs_ground]
            self.poss_sp_roles.append(pos)

    def create_poss_thing_2(self):
        start_x = 1760
        step_x = 160
        h_vs_ground = 25
        for n in range(0, self.num_thing_2):
            pos = [start_x + n * step_x, self.y_ground - h_vs_ground]
            self.poss_thing_2.append(pos)

    def create_poss_thing_1(self):
        start_x = 200
        step_x = 160
        h_vs_ground = 58
        for n in range(0, self.num_thing_1):
            pos = [start_x + n * step_x, self.y_ground - h_vs_ground]
            self.poss_thing_1.append(pos)

    def create_poss_thing_3(self):
        start_x = 200
        step_x = 160
        h_vs_ground = 200
        for n in range(0, self.num_thing_3):
            pos = [start_x + n * step_x, self.y_ground - h_vs_ground]
            self.poss_thing_3.append(pos)

    def load_animation_things_3(self):
        for n in range(0, self.num_thing_3):
            self.things_3.append(Thing_3())

    def load_animation_things_1(self):
        for n in range(0, self.num_thing_1):
            self.things_1.append(Thing_1())

    def load_sp_role_1(self):
        for n in range(0, self.num_sp_roles):
            self.sp_roles.append(SP_role())

    def load_things_2(self):
        for n in range(0, self.num_thing_2):
            self.things_2.append(Thing_2(n, self.poss_thing_2[n]))

    def set_poss_things_1(self):
        for n in range(0, self.num_thing_1):
            self.things_1[n].pos = self.poss_thing_1[n]

    def set_poss_things_3(self):
        for n in range(0, self.num_thing_3):
            self.things_3[n].pos = self.poss_thing_3[n]

    def set_poss_sp_roles(self):
        for n in range(0, self.num_sp_roles):
            self.sp_roles[n].pos_body = self.poss_sp_roles[n]

    def run_event_room_1(self, main_role, runtime, screen):
        for n in range(0, self.num_sp_roles):
            self.things_1[n].run_events(self.sp_roles[n], runtime)
        self.things_1[6].run_events(main_role, runtime)
        for n in range(0, self.num_thing_3):
            self.things_3[n].run_events(runtime)
        main_role.run_events(runtime)
        for n in range(0, self.num_sp_roles):
            self.sp_roles[n].process_move(self.rects_room, screen)
            self.sp_roles[n].run_events(runtime)

    def run_event_room_2(self, main_role, runtime, screen):
        for n in range(0, self.num_thing_2):
            self.things_2[n].event_1(main_role)
        for n in range(0, self.num_sp_roles):
            self.sp_roles[n].process_move(self.rects_room, screen)

    def event_change_room(self, main_role, screen):
        if main_role.pos_body[0] > 1366:
            screen.move_screen_1()
            if self.room_case == 1:
                self.room_case = 2
                main_role.case_power = 5
                main_role.can_use_skill = True
                main_role.case_hand = 1
        if main_role.pos_body[0] < 1366:
            screen.move_screen_2()
            if self.room_case == 2:
                self.room_case = 1
                main_role.can_use_skill = False
                main_role.case_power = 5
                main_role.case_hand = 0

    def run_event_1_room_1(self, runtime):
        if self.stt_event_1_room == 1:
            self.event_1_1_room_1(runtime)
        if self.stt_event_1_room == 2:
            self.event_1_2_room_1()
        if self.stt_event_1_room == 3:
            self.event_1_3_room_1()

    def event_1_1_room_1(self, runtime):
        if self.check_change_1 != self.things_1[6].using:
            self.time_check = runtime
            self.check_change_1 = self.things_1[6].using
        if runtime - self.time_check > 7000:
            self.check_event_1_room = True
            if not self.things_1[6].using:
                self.stt_event_1_room = 2
            else:
                self.stt_event_1_room = 3

    def event_1_2_room_1(self):
        if self.rect_way[3] < 190:
            self.rect_way[3] = self.rect_way[3] + 2
            self.rect_way[1] = self.rect_way[1] - 2
        else:
            self.stt_event_1_room = 1

    def event_1_3_room_1(self):
        if self.rect_way[3] > 3:
            self.rect_way[3] = self.rect_way[3] - 3
            self.rect_way[1] = self.rect_way[1] + 3
        else:
            self.rect_way = [1166, 530, 400, 0]
            self.stt_event_1_room = 1
            self.check_event_1_room = False

    def upd_rects_room(self):
        self.rects_room = []
        self.rects_room.append(self.rect_room)
        self.rects_room.append(self.rect_tower)
        if self.check_event_1_room:
            self.rects_room.append(self.rect_way)

    def find_rects_on_screen(self, screen):
        self.rects_room_on_screen = []
        for n in range(0, len(self.rects_room)):
            rect_on_screen = [self.rects_room[n][0] - screen.x, self.rects_room[n][1] - screen.y, self.rects_room[n][2],
                              self.rects_room[n][3]]
            self.rects_room_on_screen.append(rect_on_screen)

    def find_things_on_screen(self, screen):
        for thing_1 in self.things_1:
            thing_1.find_on_screen(screen)
        for thing_3 in self.things_3:
            thing_3.find_on_screen(screen)
        for thing_2 in self.things_2:
            thing_2.find_on_screen(screen)
        for o_role in self.o_roles:
            o_role.find_on_screen(screen)

    def run_o_roles(self, main_role, runtime, screen):
        if self.room_case == 2:
            for o_role in self.o_roles:
                if abs(main_role.pos_body[1]-o_role.pos_body[1]) <= o_role.h_area:
                    o_role.direct_target(main_role.pos_body)
                    o_role.use_all_skills(main_role.pos_body, runtime, screen,self.rects_room)
                o_role.process_skills(screen, self.rects_room, main_role)

    def reset_time(self, runtime):
        for n in range(0, self.num_thing_1):
            self.things_1[n].reset_time(runtime)
        for n in range(0, self.num_thing_3):
            self.things_1[n].reset_time(runtime)

    def set_start_pos_role(self, role):
        role.pos_body = self.start_pos_mainrole

    def run_events_room(self, runtime, main_role, screen, mouse):
        if self.room_case == 1:
            self.run_event_room_1(main_role, runtime, screen)
        self.run_event_1_room_1(runtime)
        if self.room_case == 2:
            self.run_event_room_2(main_role, runtime, screen)
            screen.move_screen_3(main_role, mouse.pos[1])
            self.run_o_roles(main_role, runtime, screen)
        self.event_change_room(main_role, screen)
        self.upd_rects_room()
        self.find_rects_on_screen(screen)
        self.find_things_on_screen(screen)

    def draw_box(self, suf):
        for n in range(0, len(self.rects_room_on_screen)):
            pg.draw.rect(suf, gray, self.rects_room_on_screen[n])

    def show_things_1(self, suf, runtime):
        for n in range(0, self.num_thing_1):
            self.things_1[n].show(suf, runtime)

    def show_things_3(self, suf, runtime):
        for n in range(0, self.num_thing_3):
            self.things_3[n].show(suf, runtime)

    def show_things_2(self, suf, runtime):
        for n in range(0, self.num_thing_2):
            self.things_2[n].show(suf, runtime)

    def show_sp_roles(self, suf, runtime):
        for n in range(0, self.num_sp_roles):
            self.sp_roles[n].show(suf, runtime)

    def show_o_roles(self, suf, runtime):
        for o_role in self.o_roles:
            o_role.show(suf, runtime)

    def show_room(self, suf, runtime, main_role):
        suf.fill(black)
        self.draw_box(suf)
        self.show_things_3(suf, runtime)
        self.show_things_2(suf, runtime)
        if self.room_case == 2:
            self.show_o_roles(suf, runtime)
            main_role.hp_and_mana.show(suf, runtime)
        main_role.show(suf, runtime)
        self.show_sp_roles(suf, runtime)
        self.show_things_1(suf, runtime)

