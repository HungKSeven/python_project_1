from process_animation import Animation
from tv import *


class Effect_kind_1:
    def __init__(self, case, fps, size):
        self.pos = 0, 0
        self.size = size
        self.alpha = 0
        self.dir_animation = 'c:/users/KSEVEN/desktop/imgs/roles/main_role/effects/'
        self.dir_animation_case = listdir(self.dir_animation)
        self.animation_cases = []
        self.case_animation = case
        self.fps = fps
        self.load_animation()
        self.animation_case = self.animation_cases[self.case_animation]

    def load_animation(self):
        for dir_name in self.dir_animation_case:
            animation_case = Animation(self.dir_animation + dir_name + '/', self.size, self.alpha, self.fps)
            self.animation_cases.append(animation_case)

    def show(self, suf, runtime, pos):
        self.animation_case = self.animation_cases[self.case_animation]
        self.animation_case.rotate_imgs(self.alpha)
        self.animation_case.show(suf, runtime, pos)
