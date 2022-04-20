from tv import *
from process_distance import *
from process_alpha import *
from colors import *


class Lightning:
    def __init__(self, pos_start, pos_end, color, time_start, wl):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.poss = []
        self.color_lighting = color
        self.d = process_distance_1(self.pos_start, self.pos_end)
        self.alpha = process_alpha_1(self.pos_start, self.pos_end)
        self.num_poss_max = self.d // 23
        self.num_poss_min = int(self.num_poss_max / 3)
        self.time = time_start
        self.time_step = 100
        self.h = 17
        self.wight_light = wl
        self.suf_ef = pg.Surface([1366, 768])
        self.suf_ef.set_alpha(70)
        self.poss_on_screen = []

    def find_poss(self):
        num_poss = rd.randint(self.num_poss_min, self.num_poss_max)
        ds_rd = []
        for n in range(0, num_poss):
            dfps = rd.randint(7, int(self.d))
            ds_rd.append(dfps)
        ds_rd.sort()

        self.poss.append(self.pos_start)
        for n in range(0, num_poss):
            new_pos_1 = [0, 0]
            new_pos_2 = [0, 0]
            new_h = rd.randint(int(self.h / 7), self.h)
            new_pos_1[0] = self.pos_start[0] + math.cos(deg_to_rad(self.alpha)) * ds_rd[n]
            new_pos_1[1] = self.pos_start[1] - math.sin(deg_to_rad(self.alpha)) * ds_rd[n]
            new_value = rd.randint(0, 1)
            if new_value == 0:
                new_alpha = self.alpha + 90
            else:
                new_alpha = self.alpha - 90

            new_pos_2[0] = new_pos_1[0] + math.cos(deg_to_rad(new_alpha)) * new_h
            new_pos_2[1] = new_pos_1[1] - math.sin(deg_to_rad(new_alpha)) * new_h
            self.poss.append(new_pos_2)

        self.poss.append(self.pos_end)

    def find_poss_on_screen(self, screen):
        self.poss_on_screen = []
        for poss in self.poss:
            new_poss_on_screen = [0, 0]
            new_poss_on_screen[0] = poss[0] - screen.x
            new_poss_on_screen[1] = poss[1] - screen.y
            self.poss_on_screen.append(new_poss_on_screen)

    def create_poss(self, runtime, screen):
        if runtime - self.time > self.time_step:
            self.poss = []
            self.find_poss()
            self.find_poss_on_screen(screen)
            self.time = runtime
        else:
            self.poss = []

    def show(self, suf):
        if len(self.poss) > 0:
            for n in range(0, len(self.poss_on_screen) - 1):
                pg.draw.line(suf, self.color_lighting, self.poss[n], self.poss[n + 1], self.wight_light)
            self.suf_ef.fill(gray5)
            for n in range(0, len(self.poss_on_screen) - 1):
                pg.draw.line(self.suf_ef, purple1, self.poss[n], self.poss[n + 1], self.wight_light + 50)
            suf.blit(self.suf_ef, [0, 0, 1366, 768])
