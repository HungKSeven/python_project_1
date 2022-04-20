from tv import *
from colors import *
from process_alpha import *
from text_game import Text
from process_animation import Animation
from process_distance import *
from process_rects import *


class Cube:
    def __init__(self, pos):
        self.value_faces = [0, 1, 2, 3, 4, 5]
        # 0-mat chinh dien
        # 1-mat huong len
        # 2-mat huong phai
        # 3-mat huong xuong
        # 4-mat huong trai
        # 5-mat up
        self.size_rect = 70
        self.rect_face = pg.Rect(0, 0, self.size_rect, self.size_rect)
        self.pos = pos
        self.colors_vs_vf = [white, red, blue, purple, green, yellow]

    def roll_truc_0(self, direct):
        if direct == 1:
            a = self.value_faces[1]
            self.value_faces[1] = self.value_faces[4]
            self.value_faces[4] = self.value_faces[3]
            self.value_faces[3] = self.value_faces[2]
            self.value_faces[2] = a
        else:
            a = self.value_faces[1]
            self.value_faces[1] = self.value_faces[2]
            self.value_faces[2] = self.value_faces[3]
            self.value_faces[3] = self.value_faces[4]
            self.value_faces[4] = a

    def roll_truc_1(self, direct):
        if direct == 1:
            a = self.value_faces[0]
            self.value_faces[0] = self.value_faces[4]
            self.value_faces[4] = self.value_faces[5]
            self.value_faces[5] = self.value_faces[2]
            self.value_faces[2] = a
        else:
            a = self.value_faces[0]
            self.value_faces[0] = self.value_faces[2]
            self.value_faces[2] = self.value_faces[5]
            self.value_faces[5] = self.value_faces[4]
            self.value_faces[4] = a

    def roll_truc_2(self, direct):
        if direct == 1:
            a = self.value_faces[0]
            self.value_faces[0] = self.value_faces[3]
            self.value_faces[3] = self.value_faces[5]
            self.value_faces[5] = self.value_faces[1]
            self.value_faces[1] = a
        else:
            a = self.value_faces[0]
            self.value_faces[0] = self.value_faces[1]
            self.value_faces[1] = self.value_faces[5]
            self.value_faces[5] = self.value_faces[3]
            self.value_faces[3] = a

    def show(self, suf):
        self.rect_face.center = self.pos
        pg.draw.rect(suf, self.colors_vs_vf[self.value_faces[0]], self.rect_face)


class Sources:
    def __init__(self, pos):
        self.pos = pos

        self.hs_source_lost = [93, 0, 0, 0, 0, 0]

        self.w_1 = 12
        self.w_2 = 20
        self.h = 100

        self.rect_sources = []
        for n in range(0, 6):
            self.rect_sources.append(pg.Rect(0, 0, self.w_1, self.h))

        for n in range(0, 6):
            self.rect_sources[n].center = [self.pos[0] + (n+1) * self.w_2, self.pos[1]+self.h/2]

        self.color_rect_source = [white, red, blue, purple, green, yellow]

        self.rect_sources_lost = []
        self.checks_up = [0, 0, 0, 0, 0, 0]
        self.plgs_up_icon = []
        for n in range(0, 6):
            self.rect_sources_lost.append(pg.Rect(0, self.pos[1], self.w_1, self.hs_source_lost[n]))

        for n in range(0, 6):
            self.rect_sources_lost[n].x = self.pos[0] + (n+1) * self.w_2-self.w_1/2
            new_pos_up_source = [self.pos[0] + (n+1) * self.w_2, self.pos[1]+self.h+10]
            new_pos_1 = [new_pos_up_source[0] - 5, new_pos_up_source[1]]
            new_pos_2 = [new_pos_up_source[0], new_pos_up_source[1] - 5]
            new_pos_3 = [new_pos_up_source[0] + 5, new_pos_up_source[1]]
            new_plg = [new_pos_1, new_pos_2, new_pos_3]
            self.plgs_up_icon.append(new_plg)

        self.times_source = [0, 0, 0, 0, 0, 0]

    def lost_source(self, runtime):
        for n in range(1, 6):
            if runtime - self.times_source[n] > rd.randint(5, 8) * 1000:
                self.times_source[n] = runtime
                self.hs_source_lost[n] = rd.randint(1, 30)
            else:
                if self.hs_source_lost[n] > 0:
                    self.hs_source_lost[n] -= 0.08
                else:
                    self.hs_source_lost[n] = 0

            self.rect_sources_lost[n].h = self.hs_source_lost[n]

        if rd.randint(1, 1000000) == 1:
            if self.hs_source_lost[0] > 0:
                self.hs_source_lost[0] -= 0.49
            else:
                self.hs_source_lost[0] = 0
        self.rect_sources_lost[0].h = self.hs_source_lost[0]

    def show(self, suf):

        for n in range(0, 6):
            pg.draw.rect(suf, self.color_rect_source[n], self.rect_sources[n])
            pg.draw.rect(suf, black, self.rect_sources_lost[n])

            if self.checks_up[n] == 1:
                pg.draw.polygon(suf, self.color_rect_source[n], self.plgs_up_icon[n])

        pg.draw.rect(suf,white,[self.pos[0],self.pos[1],140,self.h],1)
        pg.draw.line(suf, white, [self.pos[0], self.pos[1]+self.h],[self.pos[0]+139,self.pos[1]+self.h],3)

class Next_button:
    def __init__(self, pos):
        self.pos = pos
        self.dir_folder = os.path.abspath(os.getcwd())+'/imgs/gameplay2/next_button/'
        self.dir_animation_cases = listdir(self.dir_folder)
        self.case_animation = 0
        self.size_button = 108, 108
        self.animation_cases = []
        self.load_animation()
        self.animation_case = self.animation_cases[self.case_animation]
        self.radius = 40
        self.check_1 = False

    def load_animation(self):
        for dir_case in self.dir_animation_cases:
            animation_case = Animation(self.dir_folder + dir_case + '/', self.size_button, 0, 1)
            self.animation_cases.append(animation_case)

    def change_case(self, mouse_pos):
        if process_distance_1(self.pos, mouse_pos) <= self.radius:
            self.check_1 = True
            self.case_animation = 1
        else:
            self.check_1 = False
            self.case_animation = 0

    def show(self, suf, runtime):
        self.animation_case = self.animation_cases[self.case_animation]
        self.animation_case.show(suf, runtime, self.pos)


class Button_1:
    def __init__(self, pos):
        self.pos = pos
        self.dir_folder = os.path.abspath(os.getcwd())+'/imgs/gameplay2/button_1/'
        self.dir_animation_cases = listdir(self.dir_folder)
        self.case_animation = 0
        self.size_button = 23, 23
        self.animation_cases = []
        self.load_animation()
        self.animation_case = self.animation_cases[self.case_animation]
        self.radius = 13
        self.check_1 = False
        new_pos_1 = [self.pos[0], self.pos[1] + 6 + 12]
        new_pos_2 = [self.pos[0] - 6, self.pos[1] + 12]
        new_pos_3 = [self.pos[0] + 6, self.pos[1] + 12]
        self.poss_plg_down = [new_pos_1, new_pos_2, new_pos_3]
        self.check_2 = False
        self.h_1 = 0

    def load_animation(self):
        for dir_case in self.dir_animation_cases:
            animation_case = Animation(self.dir_folder + dir_case + '/', self.size_button, 0, 1)
            self.animation_cases.append(animation_case)

    def change_case(self, mouse_pos):
        if process_distance_1(self.pos, mouse_pos) <= self.radius:
            self.check_1 = True
            self.case_animation = 1
        else:
            self.check_1 = False
            self.case_animation = 0

    def show(self, suf, runtime):
        self.animation_case = self.animation_cases[self.case_animation]
        self.animation_case.show(suf, runtime, self.pos)
        if self.check_2:

            if self.h_1 < 7:
                self.h_1 += 0.2
                for pos in self.poss_plg_down:
                    pos[1] += 0.2
            else:
                for pos in self.poss_plg_down:
                    pos[1] -= self.h_1
                self.h_1 = 0
            pg.draw.polygon(suf, white, self.poss_plg_down)


class H_mr:
    def __init__(self, pos):
        self.h_mr = 70000
        self.contents_text_h_mr = ('O', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII')
        self.pos = pos
        self.Text_h_mr = None

    def climb(self):
        a = 1

    def show(self, suf, runtime):
        self.Text_h_mr = Text(191, 23, str(self.h_mr), white, 1)
        self.Text_h_mr.show(suf, self.pos)


class Guide:
    def __init__(self):
        self.icon = Text(191, 27, '?', white, 1)
        self.pos_1 = 180, 100
        self.content_guide_1 = Text(191, 23, 'Arrows', white, 0)
        self.content_guide_2 = Text(191, 23, 'R-ctrl', white, 0)
        self.content_guide_3 = Text(191, 23, 'Mouse', white, 0)
        self.check_show = False
        self.rect_icon = pg.Rect((0, 0, 17, 27))
        self.rect_icon.center = self.pos_1
        self.pos_2 = 180, 130
        self.pos_3 = 180, 157
        self.pos_4 = 180, 184

    def check_guide(self, mouse_pos):
        if not process_3(mouse_pos, self.rect_icon.copy()):
            self.check_show = True
        else:
            self.check_show = False

    def show(self, suf):
        self.icon.show(suf, self.pos_1)
        if self.check_show:
            self.content_guide_1.show(suf, self.pos_2)
            self.content_guide_2.show(suf, self.pos_3)
            self.content_guide_3.show(suf, self.pos_4)


class Cubes49:
    def __init__(self, level):
        self.level = level
        self.cubes = []
        self.pc_not_white = 0

        self.size_rect = 70
        self.size_rect_vt = 60
        self.width_line = 17
        self.poss_rect = []
        x_r_0_0 = 640 - self.size_rect * 3 - self.width_line * 3
        y_r_0_0 = 360 - self.size_rect * 3 - self.width_line * 3

        for r in range(0, 7):
            for c in range(0, 7):
                new_pos_rect = [0, 0]
                new_pos_rect[0] = x_r_0_0 + c * (self.size_rect + self.width_line)
                new_pos_rect[1] = y_r_0_0 + r * (self.size_rect + self.width_line)
                new_pos_rect_cop = [new_pos_rect[0], new_pos_rect[1]]
                self.poss_rect.append(new_pos_rect)
                self.cubes.append(Cube(new_pos_rect_cop))

        self.poss_polygon = []
        self.pos_1 = [1100, 600]
        self.radius_1 = 70
        self.poss_alpha = []
        alpha = 90
        while alpha >= -270:
            new_pos = [0, 0]
            new_pos[0] = self.pos_1[0] + math.cos(deg_to_rad(alpha)) * self.radius_1
            new_pos[1] = self.pos_1[1] - math.sin(deg_to_rad(alpha)) * self.radius_1
            alpha -= 1
            self.poss_alpha.append(new_pos)

        self.vt = [3, 3]

        self.on_control = False

        self.rect_vt = pg.Rect(0, 0, self.size_rect_vt, self.size_rect_vt)

        self.source = Sources((1035, 65))

        self.next_button = Next_button(self.pos_1)

        self.ns_vf0 = [0, 0, 0, 0, 0, 0]

        self.stt_skip = 0

        self.h_mr = H_mr((1100, 360))

        self.button_1 = Button_1((1160, 360))

        self.create(self.level)

        self.guide = Guide()

    def process_event_play(self, events, runtime, mouse_pos):

        self.next_button.change_case(mouse_pos)
        self.button_1.change_case(mouse_pos)
        self.guide.check_guide(mouse_pos)

        for event in events:
            if self.stt_skip == 0:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RCTRL:
                        self.on_control = not self.on_control

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        if not self.on_control:
                            self.move_vt(1)
                        else:
                            self.roll(self.vt[0], self.vt[1], 1)

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        if not self.on_control:
                            self.move_vt(2)
                        else:
                            self.roll(self.vt[0], self.vt[1], 2)

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        if not self.on_control:
                            self.move_vt(3)
                        else:
                            self.roll(self.vt[0], self.vt[1], 3)

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        if not self.on_control:
                            self.move_vt(4)
                        else:
                            self.roll(self.vt[0], self.vt[1], 4)

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.next_button.check_1:
                        self.stt_skip = 1

                    if self.button_1.check_1:
                        self.button_1.check_2 = not self.button_1.check_2

        if self.stt_skip == 0:
            self.find_ns_vf0()
            self.find_pc_white()

        self.source.lost_source(runtime)

        self.run_skip()

    def run_skip(self):
        if self.stt_skip == 1:
            self.find_ns_vf0()
            for n in range(0, 6):
                if self.ns_vf0[n] > 0:
                    self.source.checks_up[n] = 1
                else:
                    self.source.checks_up[n] = 0

            if self.source.hs_source_lost[0] > 0:
                self.source.hs_source_lost[0] -= 0.01 * self.ns_vf0[0]
            else:
                self.source.hs_source_lost[0] = 0

            self.source.rect_sources_lost[0].h = self.source.hs_source_lost[0]
            self.stt_skip = 2

        if self.stt_skip == 2:
            for cube in self.cubes:
                cube.pos[0] += 10

            n = 0
            while n < len(self.cubes):
                if self.cubes[n].pos[0] > 950:
                    del self.cubes[n]
                    n -= 1
                n += 1

            if len(self.cubes) == 0:
                self.make_new()

    def move_vt(self, direct):
        if direct == 1:
            self.vt[0] -= 1
        if direct == 2:
            self.vt[1] += 1
        if direct == 3:
            self.vt[0] += 1
        if direct == 4:
            self.vt[1] -= 1

        if self.vt[0] < 0: self.vt[0] = 6
        if self.vt[0] > 6: self.vt[0] = 0
        if self.vt[1] < 0: self.vt[1] = 6
        if self.vt[1] > 6: self.vt[1] = 0

    def create(self, time_roll):
        for n in range(0, time_roll):
            opt = rd.randint(0, 1)
            if opt == 0:
                r = rd.randint(0, 6)
                direct = rd.choice([-1, 1])
                for c in range(0, 7):
                    self.cubes[r * 7 + c].roll_truc_1(direct)
            if opt == 1:
                c = rd.randint(0, 6)
                direct = rd.choice([-1, 1])
                for r in range(0, 7):
                    self.cubes[r * 7 + c].roll_truc_2(direct)

    def roll(self, vt0, vt1, direct):
        if direct == 1:
            for r in range(0, 7):
                self.cubes[r * 7 + vt1].roll_truc_2(1)

        if direct == 3:
            for r in range(0, 7):
                self.cubes[r * 7 + vt1].roll_truc_2(-1)

        if direct == 2:
            for c in range(0, 7):
                self.cubes[vt0 * 7 + c].roll_truc_1(1)

        if direct == 4:
            for c in range(0, 7):
                self.cubes[vt0 * 7 + c].roll_truc_1(-1)

    def set_checks_up(self):
        for n in range(0, 6):
            if self.ns_vf0[n] > 0:
                self.source.checks_up[n] = 1
            else:
                self.source.checks_up[n] = 0

    def find_ns_vf0(self):
        self.ns_vf0 = [0, 0, 0, 0, 0, 0]
        for cube in self.cubes:
            if cube.value_faces[0] == 0:
                self.ns_vf0[0] += 1
            if cube.value_faces[0] == 1:
                self.ns_vf0[1] += 1
            if cube.value_faces[0] == 2:
                self.ns_vf0[2] += 1
            if cube.value_faces[0] == 3:
                self.ns_vf0[3] += 1
            if cube.value_faces[0] == 4:
                self.ns_vf0[4] += 1
            if cube.value_faces[0] == 5:
                self.ns_vf0[5] += 1

    def find_pc_white(self):
        self.pc_not_white = int(round((1 - self.ns_vf0[0] / 49) * 100))
        self.poss_polygon = []
        self.poss_polygon.append(self.pos_1)
        if self.pc_not_white > 0:
            for n in range(0, int(round(self.pc_not_white * 3.6))):
                self.poss_polygon.append(self.poss_alpha[n])

    def make_new(self):
        self.cubes = []
        for pos_rect in self.poss_rect:
            new_cube = Cube([pos_rect[0], pos_rect[1]])
            self.cubes.append(new_cube)

        self.vt = [3, 3]

        self.source.checks_up = [0, 0, 0, 0, 0, 0]

        self.level = rd.choice([7, 17, 7, 77, 77, 77, 177])

        self.create(self.level)

        self.on_control = False

        self.stt_skip = 0

    def show(self, suf, runtime):
        pg.draw.circle(suf, white, self.pos_1, 34, 6)
        if len(self.poss_polygon) >= 3:
            pg.draw.polygon(suf, black, self.poss_polygon)

        for cube in self.cubes:
            cube.show(suf)

        pos_rect_vt = self.poss_rect[self.vt[0] * 7 + self.vt[1]]

        if self.on_control:
            self.rect_vt.w = 86
            self.rect_vt.h = 86
            width_rect_vt = 4
            color_rect_vt = white
        else:
            self.rect_vt.w = 50
            self.rect_vt.h = 50
            width_rect_vt = 7
            color_rect_vt = black

        self.rect_vt.center = pos_rect_vt
        if self.stt_skip == 0 or self.stt_skip == 1:
            pg.draw.rect(suf, color_rect_vt, self.rect_vt, width_rect_vt)

        self.source.show(suf)

        self.next_button.show(suf, runtime)

        self.h_mr.show(suf, runtime)

        self.button_1.show(suf, runtime)

        self.guide.show(suf)
