from tv import *
from colors import *
from process_alpha import *
from process_effects_2 import Effect_kind_2_3


class Hp_Mana_main_role:
    def __init__(self):
        self.hp_max = 77
        self.mana_max = 77
        self.hp = self.hp_max
        self.mana = self.mana_max
        self.hp_percent = 1
        self.mana_percent = 1
        self.pos = 45, 70
        self.size_mana = 50
        self.rect_mana_use = pg.Rect((0, 0, self.size_mana, self.size_mana))
        self.rect_mana_max = pg.Rect((0, 0, self.size_mana, self.size_mana))
        self.rect_mana_max.center = self.pos
        self.rect_mana_use.center = self.pos
        self.poss_hp = []

        self.size_suf_hp = (self.size_mana * (2 ** (1 / 2)) / 2 + 2) * 2
        self.pos_center_suf_hp = [self.size_suf_hp / 2, self.size_suf_hp / 2]
        self.suf_hp = pg.Surface((self.size_suf_hp, self.size_suf_hp))
        self.rect_suf_hp = self.suf_hp.get_rect()
        self.rect_suf_hp.center = self.pos

    def use_mana(self, mana_use):
        self.mana -= mana_use

    def hurt(self, hp_lost):
        self.hp -= hp_lost

    def plus_mana(self, mana):
        self.mana += mana

    def plus_hp(self, hp):
        self.hp += hp

    def process_hp_mana(self, screen):
        if self.hp < 0:
            self.hp = 0
        if self.mana < 0:
            self.mana = 0

        self.hp_percent = int(round((1 - self.hp / self.hp_max) * 100))
        self.mana_percent = self.mana / self.mana_max
        self.rect_mana_use.h = self.size_mana * (1 - self.mana_percent)

        self.poss_hp = []
        self.poss_hp.append(self.pos_center_suf_hp)
        new_alpha = 90
        new_pos_1 = [0, 0]
        new_pos_1[0] = self.pos_center_suf_hp[0] + math.cos(deg_to_rad(new_alpha)) * 40
        new_pos_1[1] = self.pos_center_suf_hp[1] - math.sin(deg_to_rad(new_alpha)) * 40
        self.poss_hp.append(new_pos_1)

        d_alpha = 0
        alpha_plus = 360 * self.hp_percent / 100
        while d_alpha <= alpha_plus:
            new_pos_2 = [0, 0]
            new_pos_2[0] = self.pos_center_suf_hp[0] + math.cos(deg_to_rad(new_alpha - d_alpha)) * 40
            new_pos_2[1] = self.pos_center_suf_hp[1] - math.sin(deg_to_rad(new_alpha - d_alpha)) * 40
            d_alpha += 3.6
            self.poss_hp.append(new_pos_2)

        new_pos_3 = [0, 0]
        new_pos_3[0] = self.pos[0] + 1366
        new_pos_3[1] = self.pos[1] + 0 + 25

    def show(self, suf, runtime):
        pg.draw.rect(suf, blue, self.rect_mana_max)
        pg.draw.rect(suf, black, self.rect_mana_use)
        pg.draw.circle(suf, black, self.pos, self.size_mana * (2 ** (1 / 2)) / 2 + 2,
                       int(round(self.size_mana * (2 ** (1 / 2)) / 2 - self.size_mana / 2)) + 2)

        pg.draw.circle(self.suf_hp, (200, 200, 200), self.pos_center_suf_hp, self.size_mana * (2 ** (1 / 2)) / 2 + 2,
                       int(round(self.size_mana * (2 ** (1 / 2)) / 2 - self.size_mana / 2)) + 2)

        pg.draw.polygon(self.suf_hp, black, self.poss_hp)

        suf.blit(self.suf_hp, self.rect_suf_hp, special_flags=pg.BLEND_RGB_ADD)
