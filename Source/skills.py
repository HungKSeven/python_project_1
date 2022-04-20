from tv import *
from process_animation import Animation
from process_distance import *
from colors import *
from process_alpha import *
from process_bullets import MR_bullet_0, MR_bullet_1, MR_bullet_2, MR_bullet_3
from process_effects_2 import Effect_kind_2_2
from process_rects import *
from text_game import Text


class MR_skill_0:
    def __init__(self):
        self.name = 'normal'
        self.radius_max = 900
        self.radius_min = 50
        self.bullets = []
        self.time = 0
        self.speed_fire = 200
        self.effs_vs = []

    def use_skill_0(self, pos_mouse, pos_start, runtime, alpha, screen, pos_role):
        # pos mouse(pos end on screen)
        if not check_in_distance(pos_mouse, pos_role,
                                 self.radius_min) and runtime - self.time > self.speed_fire:
            pos_end = [pos_mouse[0] + screen.x, pos_mouse[1] + screen.y]
            bullet = MR_bullet_0()
            bullet.fire(pos_start, pos_end, alpha, runtime)
            self.bullets.append(bullet)
            self.time = runtime
            return True
        else:
            return False

    def del_bullets(self, pos_role, rects_room):
        n = 0
        while n < len(self.bullets):
            check_in_rects_room = False
            for rect in rects_room:
                if not process_3(self.bullets[n].pos_start, rect):
                    check_in_rects_room = True
                    break
            if not check_in_distance(self.bullets[n].pos_start, pos_role,
                                     self.radius_max) or not check_in_rects_room or self.bullets[n].vsed:
                new_eff = Effect_kind_2_2(pos_center_effect=self.bullets[n].pos_start, alpha_direct=90,
                                          area_alpha=360, v_particle_max=5, size_max=4, size_min=1, in_out=1,
                                          v_size=0.1, g=0.1, color=white, color_light=(20, 20, 20), npm=12, npps=3,
                                          rbp=1, radius_max_effect=0)

                self.effs_vs.append(new_eff)
                del self.bullets[n]
                n -= 1
            n += 1

    def del_effs_vs(self):
        n = 0
        while n < len(self.effs_vs):
            if len(self.effs_vs[n].particles) == 0:
                del self.effs_vs[n]
                n -= 1
            n += 1

    def check_vs_skill_0(self, rect_role):
        for n in range(0, len(self.bullets)):
            rect_bullet = self.bullets[n].get_rect()
            if not process_1(rect_role, rect_bullet):
                return True
        return False

    def process_skill(self, screen, pos_role, rects_room):
        for n in range(0, len(self.bullets)):
            self.bullets[n].process_move(screen)
        self.del_bullets(pos_role, rects_room)
        for n in range(0, len(self.effs_vs)):
            self.effs_vs[n].process_effect(screen, 1)
        self.del_effs_vs()

    def show_skill(self, suf, runtime):
        for n in range(0, len(self.bullets)):
            self.bullets[n].show(suf, runtime)
        for n in range(0, len(self.effs_vs)):
            self.effs_vs[n].show(suf)


class MR_skill_1:
    def __init__(self):
        self.name = 'boxs'
        self.mana_skill = 1
        self.radius_max = 700
        self.radius_min = 50
        self.bullets = []
        self.time_life = 70000
        self.level = 1
        self.level_max = 3
        self.nbms = [4, 5, 7]
        self.hps_box = [17, 27, 37]
        self.exp_max = [20, 30]
        self.exp = 0
        self.effs_dsp = []
        self.font_case = 191

    def level_up(self):
        if self.level < self.level_max:
            if self.exp >= self.exp_max[self.level - 1]:
                self.level += 1
                self.exp = 0

    def exp_up(self, d_exp):
        self.exp += d_exp

    def use_skill_1(self, pos_mouse, pos_start, runtime, alpha, screen, pos_role, hp_mana):
        if hp_mana.mana >= self.mana_skill:

            if check_in_distance(pos_mouse, pos_role, self.radius_max) and not check_in_distance(
                    pos_mouse,
                    pos_role,
                    self.radius_min):
                pos_end = [pos_mouse[0] + screen.x, pos_mouse[1] + screen.y]
                bullet = MR_bullet_1(self.hps_box[self.level - 1])
                bullet.fire(pos_start, pos_end, alpha, runtime)
                self.bullets.append(bullet)
                hp_mana.use_mana(self.mana_skill)

                if len(self.bullets) > self.nbms[self.level - 1]:
                    del self.bullets[0]

    def del_bullets(self, pos_role, rects_room, runtime):
        n = 0
        while n < len(self.bullets):
            check_in_rects_room = False
            for rect in rects_room:
                if not process_3(self.bullets[n].pos_start, rect):
                    check_in_rects_room = True
                    break

            if not check_in_distance(self.bullets[n].pos_start, pos_role,
                                     self.radius_max) or not check_in_rects_room or runtime - self.bullets[
                n].time > self.time_life or self.bullets[n].hp <= 0 or self.bullets[n].vsed:
                new_eff = Effect_kind_2_2(pos_center_effect=self.bullets[n].pos_start, alpha_direct=90,
                                          area_alpha=360, v_particle_max=5, size_max=17, size_min=7, in_out=1,
                                          v_size=0.4, g=0.1, color=black, color_light=(20, 20, 20), npm=12, npps=3,
                                          rbp=1, radius_max_effect=0)
                self.effs_dsp.append(new_eff)
                del self.bullets[n]
                n -= 1
            n += 1

    def check_vs_skill_1(self, rect_role_part,mr_vsed):
        if not mr_vsed:
            for n in range(0, len(self.bullets)):
                if self.bullets[n].reached:
                    rect_bullet = self.bullets[n].get_rect()
                    if not process_1(rect_role_part, rect_bullet):
                        return True
            return False
        else:
            return False

    def check_vs_boxs(self):
        for n in range(0, len(self.bullets)):
            if self.bullets[n].reached:
                rect_b_0 = self.bullets[n].get_rect()
                for n1 in range(0, n):
                    rect_b_c = self.bullets[n1].get_rect()
                    if not process_1(rect_b_0, rect_b_c):
                        self.bullets[n].vsed = True
                        self.bullets[n1].hp = self.bullets[n1].hp_max
                        break

    def del_effs_dsp(self):
        n = 0
        while n < len(self.effs_dsp):
            if len(self.effs_dsp[n].particles) == 0:
                del self.effs_dsp[n]
                n -= 1
            n += 1

    def process_skill(self, screen, pos_role, rects_room, runtime):
        for n in range(0, len(self.bullets)):
            self.bullets[n].process_move(screen)

        self.check_vs_boxs()
        self.del_bullets(pos_role, rects_room, runtime)
        for n in range(0, len(self.effs_dsp)):
            self.effs_dsp[n].process_effect(screen, 1)
        self.del_effs_dsp()

    def show_skill(self, suf, runtime):
        for n in range(0, len(self.bullets)):
            self.bullets[n].show(suf, runtime)
        for n in range(0, len(self.effs_dsp)):
            self.effs_dsp[n].show(suf)
        for n in range(0, len(self.bullets)):
            if self.bullets[n].reached:
                text_num_box = Text(self.font_case, 17, str(n + 1), white, 1)
                text_num_box.show(suf, self.bullets[n].pos_on_screen)


class MR_skill_2:
    def __init__(self):
        self.name = 'mind control'
        self.radius_max = 900
        self.radius_min = 50
        self.bullets = []
        self.time = 0
        self.speed_fire = 300
        self.mana_skill = 1
        self.time_load = 3000

    def use_skill_2(self, pos_mouse, pos_start, runtime, alpha, screen, pos_role, hp_mana):
        # pos mouse(pos end on screen)
        if hp_mana.mana >= self.mana_skill:
            if not check_in_distance(pos_mouse, pos_role,
                                     self.radius_min) and runtime - self.time > self.speed_fire:
                pos_end = [pos_mouse[0] + screen.x, pos_mouse[1] + screen.y]
                bullet = MR_bullet_2()
                bullet.fire(pos_start, pos_end, alpha, runtime)
                self.bullets.append(bullet)
                self.time = runtime
                hp_mana.use_mana(self.mana_skill)
                return True
            else:
                return False

    def del_bullets(self, pos_role, rects_room):
        n = 0
        while n < len(self.bullets):
            check_in_rects_room = False
            for rect in rects_room:
                if not process_3(self.bullets[n].pos_start, rect):
                    check_in_rects_room = True
                    break
            if not check_in_distance(self.bullets[n].pos_start, pos_role,
                                     self.radius_max) or not check_in_rects_room:
                del self.bullets[n]
                n -= 1
            n += 1

    def check_vs_skill_2(self, rect_role):
        for n in range(0, len(self.bullets)):
            rect_bullet = self.bullets[n].get_rect()
            if not process_1(rect_role, rect_bullet):
                return True
        return False

    def process_skill(self, screen, pos_role, rects_room):
        for n in range(0, len(self.bullets)):
            self.bullets[n].process_move(screen)
        self.del_bullets(pos_role, rects_room)

    def show_skill(self, suf, runtime):
        for n in range(0, len(self.bullets)):
            self.bullets[n].show(suf, runtime)


class MR_skill_3:
    def __init__(self):
        self.name = 'tele'
        self.stt_use = 0
        self.radius_max = 700
        self.radius_min = 75
        self.bullets = []
        self.time_life = 7000
        self.mana_skill = 1
        self.level = 1
        self.time_load = 3000

    def use_skill_3(self, pos_mouse, pos_start, runtime, alpha, screen, pos_role, hp_mana):
        if hp_mana.mana >= self.mana_skill:

            if check_in_distance(pos_mouse, pos_role, self.radius_max) and not check_in_distance(
                    pos_mouse,
                    pos_role,
                    self.radius_min):
                pos_end = [pos_mouse[0] + screen.x, pos_mouse[1] + screen.y]
                bullet = MR_bullet_3()
                bullet.fire(pos_start, pos_end, alpha, runtime)
                self.bullets.append(bullet)
                hp_mana.use_mana(self.mana_skill)

    def del_bullets(self, pos_role, rects_room, runtime):
        n = 0
        while n < len(self.bullets):
            check_in_rects_room = False
            for rect in rects_room:
                if not process_3(self.bullets[n].pos_start, rect):
                    check_in_rects_room = True
                    break

            if not check_in_rects_room or runtime - self.bullets[
                n].time > self.time_life:
                del self.bullets[n]
                n -= 1
            n += 1

    def check_vs_skill_3(self, rect_role):
        for n in range(0, len(self.bullets)):
            rect_bullet = self.bullets[n].get_rect()
            if not process_1(rect_role, rect_bullet):
                return True
        return False

    def process_skill(self, screen, pos_role, rects_room, runtime):
        for n in range(0, len(self.bullets)):
            self.bullets[n].process_move(screen)
        self.del_bullets(pos_role, rects_room, runtime)

    def show_skill(self, suf, runtime):
        for n in range(0, len(self.bullets)):
            self.bullets[n].show(suf, runtime)
