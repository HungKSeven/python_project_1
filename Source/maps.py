from tv import *
from process_rects import *
from colors import *
from process_event_wdg import *


class Map():
    def __init__(self):
        self.rects = []
        self.n = rd.randint(5, 7)
        self.w = self.n * 1366
        self.h = self.n * 768
        self.hmin = 50
        self.wmin = 50
        w_start = rd.randint(7, 20) * 100
        h_start = rd.randint(3, 6) * 100
        x_start = rd.randint(w_start + 100, self.w - w_start - 100)
        y_start = rd.randint(h_start + 100, self.h - h_start - 100)
        start_rect = [x_start, y_start, w_start, h_start]
        self.rects.append(start_rect)
        self.create_rect_from_rect1(start_rect, [1, 1, 1, 1])

        self.n_scale = 50
        self.w_minimap = int(round(self.w / self.n_scale))
        self.h_minimap = int(round(self.h / self.n_scale))
        self.x_minimap = 1336 - self.w_minimap
        self.y_minimap = 738 - self.h_minimap
        self.rect_box_minimap = [self.x_minimap, self.y_minimap, self.w_minimap, self.h_minimap]
        self.rects_on_minimap = []
        self.create_mini_map()
        self.pos_screen_on_minimap = []

    def create_mini_map(self):
        for rect in self.rects:
            rect_on_minimap = [self.x_minimap + int(round(rect[0] / self.n_scale)),
                               self.y_minimap + int(round(rect[1] / self.n_scale)),
                               int(round(rect[2] / self.n_scale)),
                               int(round(rect[3] / self.n_scale))]
            self.rects_on_minimap.append(rect_on_minimap)

    def create_rect_from_rect1(self, rect, areas):
        check_min_rect = True
        for n in range(0, len(areas)):
            if check_min_rect:
                value = 1
            else:
                value = rd.randint(0, 1)
            if areas[n] == 1 and value == 1:
                w_rect = rd.randint(7, 20) * 100
                h_rect = rd.randint(3, 6) * 100
                x_rect = 0
                y_rect = 0
                area_clock = 0
                if n == 0:
                    area_clock = 2
                    x_rect = rect[0] + rd.randint(self.wmin, int(rect[2] / 2) - self.wmin) - w_rect
                    y_rect = rect[1] + rd.randint(self.hmin, int(rect[3] / 2) - self.hmin) - h_rect

                if n == 1:
                    area_clock = 3
                    x_rect = rect[0] + rd.randint(int(rect[2] / 2) + self.wmin, rect[2] - self.wmin)
                    y_rect = rect[1] + rd.randint(self.hmin, int(rect[3] / 2) - self.hmin) - h_rect
                if n == 2:
                    area_clock = 0
                    x_rect = rect[0] + rd.randint(int(rect[2] / 2) + self.wmin, rect[2] - self.wmin)
                    y_rect = rect[1] + rd.randint(int(rect[3] / 2) + self.hmin, rect[3] - self.hmin)
                if n == 3:
                    area_clock = 1
                    x_rect = rect[0] + rd.randint(self.wmin, int(rect[2] / 2) - self.wmin) - w_rect
                    y_rect = rect[1] + rd.randint(int(rect[3] / 2) + self.hmin, rect[3] - self.hmin)

                new_rect = [x_rect, y_rect, w_rect, h_rect]
                check_end = False
                if x_rect < 0 or y_rect < 0 or x_rect + w_rect > self.w or y_rect + h_rect > self.h:
                    check_end = True

                if process_2(new_rect, self.rects)[1] > 1:
                    check_end = True

                if not check_end:
                    self.rects.append(new_rect)
                    check_min_rect = False
                    new_areas = [1, 1, 1, 1]
                    new_areas[area_clock] = 0
                    self.create_rect_from_rect1(new_rect, new_areas)

    def reset1(self):
        self.rects = []
        w_start = rd.randint(7, 20) * 100
        h_start = rd.randint(3, 6) * 100
        x_start = rd.randint(w_start + 100, self.w - w_start - 100)
        y_start = rd.randint(h_start + 100, self.h - h_start - 100)
        start_rect = [x_start, y_start, w_start, h_start]
        self.rects.append(start_rect)
        self.create_rect_from_rect1(start_rect, [1, 1, 1, 1])

    def show(self, suf):
        for n in range(0, len(self.rects)):
            if n == 0:
                color = red
            else:
                color = white
            pg.draw.rect(suf, color, self.rects[n])

    def find_pos(self, pos, suf):
        for rect in self.rects:
            if not process_3(pos, rect):
                pg.draw.rect(suf, green, rect)

    def show_minimap(self, suf, role):
        pos_role_on_minimap = [self.x_minimap + int(round(role.pos_body[0] / self.n_scale)),
                               self.y_minimap + int(round(role.pos_body[1] / self.n_scale))]
        pg.draw.rect(suf, black, self.rect_box_minimap)
        for rect_on_minimap in self.rects_on_minimap:
            pg.draw.rect(suf, gray, rect_on_minimap)
        pg.draw.circle(suf, red, pos_role_on_minimap, 4)
        rect_screen_on_minimap = [self.x_minimap + int(round(self.pos_screen_on_minimap[0] / self.n_scale)),
                                  self.y_minimap + int(round(self.pos_screen_on_minimap[1] / self.n_scale)),
                                  int(round(1366 / self.n_scale)), int(round(768 / self.n_scale))]
        pg.draw.rect(suf, white, rect_screen_on_minimap, 1)
        pg.draw.rect(suf, white, self.rect_box_minimap, 1)
