from tv import *
from process_animation import Animation
from process_distance import *
from colors import *
from process_alpha import *
from process_bullets_case_1 import OR_1_bullet_0, OR_1_bullet_1, OR_1_bullet_2, OR_1_bullet_3
from process_effects_2 import Effect_kind_2_4, Effect_kind_2_2, Effect_kind_2_1
from process_rects import *


class OR_1_skill_pass_1:
    def __init__(self, pos_role):
        self.radius_min = 200
        self.box_in_area = False
        self.mr_in_area = False
        self.damage = 3
        self.pos_role = pos_role
        self.pos_role_on_screen = [0, 0]
        self.pos_eye_role_on_screen = [0, 0]
        self.pcs = [self.radius_min, self.radius_min]
        self.pos_mr = [0, 0]
        self.pos_mr_on_screen = [0, 0]
        self.poss_box = []
        self.poss_box_on_screen = []
        self.eff_mr = Effect_kind_2_2(pos_center_effect=[0, 0], alpha_direct=-90, area_alpha=360, in_out=1,
                                      v_particle_max=3,
                                      size_max=7, size_min=3, v_size=0.2, radius_max_effect=20, rbp=1, g=0.1,
                                      color=red,
                                      color_light=(70, 20, 20), npm=-7, npps=1)
        self.opt_eff_mr = 0
        self.effs_box = []
        for n in range(0, 7):
            new_eff = Effect_kind_2_2(pos_center_effect=[0, 0], alpha_direct=-90, area_alpha=360, in_out=1,
                                      v_particle_max=3,
                                      size_max=7, size_min=3, v_size=0.2, radius_max_effect=20, rbp=1, g=0.1,
                                      color=red,
                                      color_light=(70, 20, 20), npm=-7, npps=1)
            self.effs_box.append(new_eff)

    def damage_boxs(self, main_role):
        self.box_in_area = False
        self.poss_box = []
        self.poss_box_on_screen = []
        for box in main_role.skills[1].bullets:
            if process_distance_1(self.pos_role, box.pos_start) < self.radius_min:
                self.box_in_area = True
                self.poss_box.append(box.pos_start)
                self.poss_box_on_screen.append(box.pos_on_screen)
                box.damage_hp(self.damage)

    def damage_mr(self, main_role):
        if process_distance_1(self.pos_role, main_role.pos_body) < self.radius_min:
            self.mr_in_area = True
            self.pos_mr = main_role.pos_body
            self.pos_mr_on_screen = main_role.pos_body_on_screen
            main_role.hp_and_mana.hurt(self.damage)
            self.opt_eff_mr = 1
            self.eff_mr.update_poss_alpha_direct(self.pos_mr, 90)
        else:
            self.mr_in_area = False
            self.opt_eff_mr = 0

    def process_skill(self, main_role, pos_eye_on_screen, pos_on_screen, screen):
        self.damage_mr(main_role)
        self.damage_boxs(main_role)
        self.pos_role_on_screen = pos_on_screen
        self.pos_eye_role_on_screen = pos_eye_on_screen
        self.eff_mr.process_effect(screen, self.opt_eff_mr)
        for n in range(0, len(self.effs_box)):
            if n < len(self.poss_box):
                self.effs_box[n].update_poss_alpha_direct(self.poss_box[n], 90)
                self.effs_box[n].process_effect(screen, 1)

    def show(self, suf):
        if self.mr_in_area:
            pg.draw.line(suf, red, self.pos_eye_role_on_screen, self.pos_mr_on_screen, 2)
            self.eff_mr.show(suf)

        if self.box_in_area:
            for n in range(0, len(self.poss_box)):
                pg.draw.line(suf, red, self.pos_eye_role_on_screen, self.poss_box_on_screen[n], 2)
                self.effs_box[n].show(suf)


class OR_1_skill_0:
    def __init__(self):
        self.name = 'normal'
        self.radius_max = 900
        self.radius_min = 50
        self.bullets = []
        self.time = 0
        self.effect_explode = []
        self.effect_fire = []
        self.ulti_mode = 0
        self.speed_fire = 0

    def use_skill(self, pos_target, pos_start, runtime, pos_role, alpha):
        if self.ulti_mode == 0:
            self.speed_fire = 1000
        else:
            self.speed_fire = rd.randint(400, 700)
        if not check_in_distance(pos_target, pos_role,
                                 self.radius_min) and runtime - self.time > self.speed_fire:
            pos_end = [pos_target[0], pos_target[1]]
            bullet = OR_1_bullet_0()
            bullet.fire(pos_start, pos_end, runtime, alpha)
            self.bullets.append(bullet)
            self.time = runtime
            new_effect_fire = Effect_kind_2_4(pos_center_effect=pos_start, alpha_direct=alpha,
                                              area_alpha=90, v_particle_max=7, size_max=5, size_min=3,
                                              v_size=0.6, g=0, color=red, color_light=(60, 20, 20), npm=15)
            self.effect_fire.append(new_effect_fire)
            return True
        else:
            return False

    def del_bullets(self, pos_role, rects_room, main_role):
        n = 0
        while n < len(self.bullets):
            check_in_rects_room = False
            for rect in rects_room:
                if not process_3(self.bullets[n].pos_start, rect):
                    check_in_rects_room = True
                    break
            if not check_in_distance(self.bullets[n].pos_start, pos_role, self.radius_max) or not check_in_rects_room or \
                    self.bullets[n].check_vs_main_role(main_role) or self.bullets[n].check_vs_mr_boxs(main_role):
                ef_explode_bullet = Effect_kind_2_4(pos_center_effect=self.bullets[n].pos_start, alpha_direct=90,
                                                    area_alpha=360, v_particle_max=5, size_max=4, size_min=1,
                                                    v_size=0.1, g=0.1, color=red, color_light=(60, 20, 20), npm=20)
                self.effect_explode.append(ef_explode_bullet)
                del self.bullets[n]
                n -= 1
            n += 1

    def del_ef_explode(self):
        n = 0
        while n < len(self.effect_explode):
            if self.effect_explode[n].check_end == 1:
                del self.effect_explode[n]
                n -= 1
            n += 1

    def del_ef_fire(self):
        n = 0
        while n < len(self.effect_fire):
            if self.effect_fire[n].check_end == 1:
                del self.effect_fire[n]
                n -= 1
            n += 1

    def process_skill(self, screen, pos_role, rects_room, main_role):
        for n in range(0, len(self.bullets)):
            self.bullets[n].process_move(screen)
        self.del_bullets(pos_role, rects_room, main_role)
        for n in range(0, len(self.effect_explode)):
            self.effect_explode[n].process_effect(screen, 1)
        for n in range(0, len(self.effect_fire)):
            self.effect_fire[n].process_effect(screen, 1)
        self.del_ef_fire()
        self.del_ef_explode()

    def show_skill(self, suf, runtime):
        for n in range(0, len(self.bullets)):
            self.bullets[n].show(suf, runtime)
        for n in range(0, len(self.effect_explode)):
            self.effect_explode[n].show(suf)
        for n in range(0, len(self.effect_fire)):
            self.effect_fire[n].show(suf)


class OR_1_skill_1:
    def __init__(self):
        self.name = 'super'
        self.radius_max = 900
        self.radius_min = 50
        self.bullets = []
        self.time = 0
        self.effect_explode = []
        self.effect_fire = []
        self.effect_nap = Effect_kind_2_2(pos_center_effect=[0, 0], alpha_direct=-90, area_alpha=360, in_out=-1,
                                          v_particle_max=1,
                                          size_max=2, size_min=1, v_size=0.1, radius_max_effect=20, rbp=2, g=0,
                                          color=red,
                                          color_light=(70, 20, 20), npm=10, npps=2)

        self.stt = 1
        self.ulti_mode = 0

    def use_skill(self, pos_target, pos_start, runtime, pos_role, alpha):
        if not check_in_distance(pos_target, pos_role,
                                 self.radius_min):
            self.stt = 0
            self.effect_nap.npm = 30
            self.effect_nap.update_poss_alpha_direct(pos_start, 90)
            pos_end = [pos_target[0], pos_target[1]]
            bullet = OR_1_bullet_1()
            bullet.fire(pos_start, pos_end, runtime, alpha)
            self.bullets.append(bullet)
            self.time = runtime
            new_effect_fire = Effect_kind_2_4(pos_center_effect=pos_start, alpha_direct=alpha,
                                              area_alpha=20, v_particle_max=10, size_max=7, size_min=5,
                                              v_size=0.4, g=0.1, color=red, color_light=(60, 20, 20), npm=23)
            self.effect_fire.append(new_effect_fire)

    def del_bullets(self, pos_role, rects_room, main_role):
        n = 0
        while n < len(self.bullets):
            check_in_rects_room = False
            for rect in rects_room:
                if not process_3(self.bullets[n].pos_start, rect):
                    check_in_rects_room = True
                    break
            if not check_in_distance(self.bullets[n].pos_start, pos_role, self.radius_max) or not check_in_rects_room or \
                    self.bullets[n].check_vs_main_role(main_role) or self.bullets[n].check_vs_mr_boxs(main_role):
                if self.bullets[n].stt_show != 0:
                    ef_explode_bullet = Effect_kind_2_4(pos_center_effect=self.bullets[n].pos_start, alpha_direct=90,
                                                        area_alpha=360, v_particle_max=5, size_max=20, size_min=10,
                                                        v_size=0.4, g=0.2, color=red, color_light=(60, 20, 20), npm=30)
                    self.effect_explode.append(ef_explode_bullet)
                    del self.bullets[n]
                    n -= 1
            n += 1

    def del_ef_explode(self):
        n = 0
        while n < len(self.effect_explode):
            if self.effect_explode[n].check_end == 1:
                del self.effect_explode[n]
                n -= 1
            n += 1

    def del_ef_fire(self):
        n = 0
        while n < len(self.effect_fire):
            if self.effect_fire[n].check_end == 1:
                del self.effect_fire[n]
                n -= 1
            n += 1

    def process_skill(self, screen, pos_role, rects_room, main_role):
        if self.stt == 0:
            if self.effect_nap.npm <= 0:
                self.effect_nap.particles = []
                self.stt = 1
                self.bullets[len(self.bullets) - 1].stt_show = 1

            for n in range(0, len(self.bullets) - 1):
                self.bullets[n].process_move(screen)
            self.del_bullets(pos_role, rects_room, main_role)
            for n in range(0, len(self.effect_fire) - 1):
                self.effect_fire[n].process_effect(screen, 1)
            self.del_ef_fire()

        self.effect_nap.process_effect(screen, 1)

        if self.stt == 1:
            for n in range(0, len(self.bullets)):
                self.bullets[n].process_move(screen)
            self.del_bullets(pos_role, rects_room, main_role)
            for n in range(0, len(self.effect_fire)):
                self.effect_fire[n].process_effect(screen, 1)
            self.del_ef_fire()

        for n in range(0, len(self.effect_explode)):
            self.effect_explode[n].process_effect(screen, 1)
        self.del_ef_explode()

    def show_skill(self, suf, runtime):
        for n in range(0, len(self.bullets)):
            self.bullets[n].show(suf, runtime)
        for n in range(0, len(self.effect_explode)):
            self.effect_explode[n].show(suf)
        for n in range(0, len(self.effect_fire)):
            self.effect_fire[n].show(suf)
        self.effect_nap.show(suf)


class OR_1_skill_2:
    def __init__(self):
        self.name = 'follow'
        self.radius_max = 900
        self.radius_min = 50
        self.bullets = []
        self.time = 0
        self.effect_explode = []
        self.effect_fire = []
        self.ulti_mode = 0

    def use_skill(self, pos_target, pos_start, runtime, pos_role, alpha):
        if not check_in_distance(pos_target, pos_role,
                                 self.radius_min):
            pos_end = [pos_target[0], pos_target[1]]
            bullet = OR_1_bullet_2()
            bullet.fire(pos_start, pos_end, runtime, alpha)
            self.bullets.append(bullet)
            self.time = runtime
            new_effect_fire = Effect_kind_2_4(pos_center_effect=pos_start, alpha_direct=alpha + 180,
                                              area_alpha=20, v_particle_max=6, size_max=10, size_min=4,
                                              v_size=0.6, g=0, color=red, color_light=(60, 20, 20), npm=15)
            self.effect_fire.append(new_effect_fire)
            return True
        else:
            return False

    def del_bullets(self, pos_role, rects_room, main_role):
        n = 0
        while n < len(self.bullets):
            check_in_rects_room = False
            for rect in rects_room:
                if not process_3(self.bullets[n].pos_start, rect):
                    check_in_rects_room = True
                    break
            if not check_in_distance(self.bullets[n].pos_start, pos_role, self.radius_max) or not check_in_rects_room or \
                    self.bullets[n].check_vs_main_role(main_role) or self.bullets[n].check_vs_mr_boxs(main_role) or \
                    self.bullets[n].check_vs_mr_normal(main_role):
                ef_explode_bullet = Effect_kind_2_4(pos_center_effect=self.bullets[n].pos_start, alpha_direct=90,
                                                    area_alpha=360, v_particle_max=5, size_max=15, size_min=7,
                                                    v_size=0.4, g=0.2, color=red, color_light=(60, 20, 20), npm=30)
                self.effect_explode.append(ef_explode_bullet)
                del self.bullets[n]
                n -= 1
            n += 1

    def del_ef_explode(self):
        n = 0
        while n < len(self.effect_explode):
            if self.effect_explode[n].check_end == 1:
                del self.effect_explode[n]
                n -= 1
            n += 1

    def del_ef_fire(self):
        n = 0
        while n < len(self.effect_fire):
            if self.effect_fire[n].check_end == 1:
                del self.effect_fire[n]
                n -= 1
            n += 1

    def process_skill(self, screen, pos_role, rects_room, main_role):
        for n in range(0, len(self.bullets)):
            self.bullets[n].process_move(screen, main_role)
        self.del_bullets(pos_role, rects_room, main_role)
        for n in range(0, len(self.effect_explode)):
            self.effect_explode[n].process_effect(screen, 1)
        for n in range(0, len(self.effect_fire)):
            self.effect_fire[n].process_effect(screen, 1)
        self.del_ef_fire()
        self.del_ef_explode()

    def show_skill(self, suf, runtime):
        for n in range(0, len(self.bullets)):
            self.bullets[n].show(suf, runtime)
        for n in range(0, len(self.effect_explode)):
            self.effect_explode[n].show(suf)
        for n in range(0, len(self.effect_fire)):
            self.effect_fire[n].show(suf)


class OR_1_skill_3:
    def __init__(self):
        self.name = 'boom fall'
        self.radius_max = 900
        self.bullets = []
        self.time = 0
        self.effect_explode = []

        self.effs_creat = []
        self.stt = 1
        self.pos_eye_role_on_screen = [0, 0]
        self.ulti_mode = 0
        for n in range(0, 3):
            new_eff_creat = Effect_kind_2_1(pos_center_effect=[0, 0], alpha_direct=90,
                                            area_alpha=360, in_out=-1, case=1, v_particle_max=6, size_max=15,
                                            size_min=10,
                                            v_size=0.6, radius_max_effect=70, rbp=2, g=0, color_light=(20, 20, 20),
                                            npm=15, npps=1)
            self.effs_creat.append(new_eff_creat)

    def use_skill(self, pos_target, runtime, rects_room):
        if runtime - self.time > rd.randint(4, 7) * 1000 and len(self.bullets)==0:
            self.stt = 0
            if self.ulti_mode == 0:
                self.effs_creat[0].npm = 10
                pos_set = [0, 0]
                pos_set[0] = pos_target[0]
                pos_set[1] = pos_target[1] - rd.randint(300, 400)
                self.effs_creat[0].update_poss_alpha_direct(pos_set, 90)
                bullet = OR_1_bullet_3()
                bullet.use_skill(pos_set)
                self.bullets.append(bullet)
            else:
                for n in range(0, 3):
                    pos_set = [0, 0]
                    pos_set[0] = pos_target[0]
                    pos_set[0] += (n - 1) * rd.randint(7, 20) * 10
                    pos_set[1] = pos_target[1] - rd.randint(300, 400)
                    bullet = OR_1_bullet_3()
                    bullet.use_skill(pos_set)
                    bullet.get_rect()
                    if check_in_rects_room(bullet.rect_bullet, rects_room):
                        self.bullets.append(bullet)
                        self.effs_creat[n].npm = 10
                        self.effs_creat[n].update_poss_alpha_direct(pos_set, 90)

            self.time = runtime

            return 1
        else:
            return 0

    def del_bullets(self, pos_role, rects_room, main_role):
        n = 0
        while n < len(self.bullets):
            check_in_rects_room = False
            for rect in rects_room:
                if not process_3(self.bullets[n].pos_start, rect):
                    check_in_rects_room = True
                    break
            if not check_in_distance(self.bullets[n].pos_start, pos_role, self.radius_max) or not check_in_rects_room or \
                    self.bullets[n].check_vs_main_role(main_role) or self.bullets[n].check_vs_mr_boxs(main_role) or \
                    self.bullets[n].hp <= 0:
                if self.bullets[n].stt_show != 0:
                    ef_explode_bullet = Effect_kind_2_4(pos_center_effect=self.bullets[n].pos_start, alpha_direct=90,
                                                        area_alpha=360, v_particle_max=5, size_max=23, size_min=15,
                                                        v_size=0.4, g=0.2, color=black, color_light=(60, 20, 20), npm=17)
                    self.effect_explode.append(ef_explode_bullet)
                    del self.bullets[n]
                    n -= 1
            n += 1

    def del_ef_explode(self):
        n = 0
        while n < len(self.effect_explode):
            if self.effect_explode[n].check_end == 1:
                del self.effect_explode[n]
                n -= 1
            n += 1

    def process_skill(self, screen, pos_role, rects_room, main_role, pos_eye_on_screen):
        self.pos_eye_role_on_screen = pos_eye_on_screen

        if self.ulti_mode == 0:

            self.effs_creat[0].process_effect(screen, 1)

            if self.stt == 0:
                self.bullets[len(self.bullets) - 1].find_on_screen(screen)
                if self.effs_creat[0].npm == 0:
                    self.stt = 1
                    self.effs_creat[0].particles=[]
                    self.bullets[len(self.bullets) - 1].stt_show = 1

            if self.stt == 1:
                for n in range(0, len(self.bullets)):
                    self.bullets[n].process_move(screen, main_role)
                self.del_bullets(pos_role, rects_room, main_role)

        else:

            for n in range(0, 3):
                self.effs_creat[n].process_effect(screen, 1)

            if self.stt == 0:
                for n in range(0, len(self.bullets)):
                    self.bullets[n].find_on_screen(screen)
                if self.effs_creat[0].npm == 0:
                    self.stt = 1
                    for n in range(0,3):
                        self.effs_creat[n].particles=[]
                    for n in range(0, len(self.bullets)):
                        self.bullets[n].stt_show = 1

            if self.stt == 1:
                for n in range(0, len(self.bullets)):
                    self.bullets[n].process_move(screen, main_role)
                self.del_bullets(pos_role, rects_room, main_role)

        for n in range(0, len(self.effect_explode)):
            self.effect_explode[n].process_effect(screen, 1)
        self.del_ef_explode()

    def show_skill(self, suf, runtime):
        if self.stt == 0:
            if self.ulti_mode == 0:
                if len(self.bullets) > 0:
                    pg.draw.line(suf, red, self.pos_eye_role_on_screen,
                                 self.bullets[len(self.bullets) - 1].pos_on_screen,
                                 1)
            else:
                for n in range(0, len(self.bullets)):
                    if self.bullets[n].stt_show == 0:
                        pg.draw.line(suf, red, self.pos_eye_role_on_screen,
                                     self.bullets[n].pos_on_screen,
                                     1)

        for n in range(0, len(self.bullets)):
            self.bullets[n].show(suf, runtime)
        for n in range(0, len(self.effect_explode)):
            self.effect_explode[n].show(suf)

        if self.ulti_mode == 0:
            if self.stt == 0:
                self.effs_creat[0].show(suf, runtime)

        if self.ulti_mode == 1:
            if self.stt == 0:
                for n in range(0, 3):
                    self.effs_creat[n].show(suf, runtime)
