from process_distance import *
from process_rects import *


class Screen():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 1366
        self.h = 768
        self.v_move = 20
        self.area_up = [0, 70]
        self.area_down = [698, 768]
        self.area_left = [0, 70]
        self.area_right = [1296, 1366]
        self.can_screen = False
        self.focus=False

    def focus_mainrole(self, mainrole):
        self.y = mainrole.pos_body[1] - 384

    def move_screen_1(self):
        if self.x < 1366:
            self.x += 10
        else:
            self.can_screen = True

    def move_screen_2(self):
        if self.x > 0:
            self.x -= 10
        else:
            self.can_screen = False

    def move_screen_3(self, main_role, mouse_y):
        if self.can_screen:
            if self.area_up[0] <= mouse_y <= self.area_up[1]:
                y_test = self.y - self.v_move
                if y_test >= main_role.pos_body[1] - 768:
                    self.y = y_test

            if self.area_down[0] <= mouse_y <= self.area_down[1]:
                y_test = self.y + self.v_move
                if y_test <= main_role.pos_body[1] and y_test < 0:
                    self.y = y_test

    def show_off(self, main_role, room, suf, runtime):
        room.show_room(suf, runtime, main_role)
