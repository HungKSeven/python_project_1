from process_animation import Animation
from tv import *


class Game_mouse:
    def __init__(self):
        self.pos = 0, 0
        self.dir_folder = os.path.abspath(os.getcwd())+'/imgs/mouse/'
        self.dir_animation_cases = listdir(self.dir_folder)
        self.size_1 = 20, 20
        self.size_2 = 55, 55
        self.case = 0
        self.animation_cases = []
        self.load_animation()
        self.animation_case = self.animation_cases[self.case]
        self.stt_show = 1

    def load_animation(self):
        n = 0
        for dir_case in self.dir_animation_cases:
            if n == 0:
                size = self.size_1
            else:
                size = self.size_2
            animation_case = Animation(self.dir_folder + dir_case + '/', size, 0, 10)
            self.animation_cases.append(animation_case)
            n += 1

    def update(self, pos):
        self.pos = pos

    def show_mouse(self, suf, runtime):
        if self.stt_show == 1:
            self.animation_case = self.animation_cases[self.case]
            self.animation_case.show(suf, runtime, self.pos)
