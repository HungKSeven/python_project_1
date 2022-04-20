from tv import *
from process_alpha import *
from process_particles import Particle_1, Particle_2, Particle_3, Particle_4
from colors import *
from process_distance import *


class Effect_kind_2_1:
    def __init__(self, pos_center_effect, alpha_direct, area_alpha,
                 v_particle_max, in_out, case, size_max, size_min, v_size, radius_max_effect, rbp, g, color_light, npm,
                 npps):
        # name: particle effect 1 basic
        self.pce = pos_center_effect
        self.particles = []
        self.alpha_direct = alpha_direct
        self.area_alpha = area_alpha
        self.alpha_min = int(alpha_direct - int(self.area_alpha / 2))
        self.alpha_max = int(alpha_direct + int(self.area_alpha / 2))
        self.v_particle_max = v_particle_max
        self.rbp = rbp
        self.in_out = in_out
        self.size_max = size_max
        self.size_min = size_min
        self.case = case
        self.v_size = v_size
        self.rmaxe = radius_max_effect
        self.rmine = int(radius_max_effect / 3)
        if self.in_out > 0:
            self.g = g
        else:
            self.g = 0
        self.color_light = color_light

        self.npps = npps
        self.npm = npm

    def update_poss_alpha_direct(self, pos_center_effect, alpha_direct):
        if self.in_out < 0:
            if process_distance_1(self.pce, pos_center_effect) > 0:
                self.particles = []
        self.pce = pos_center_effect
        self.alpha_direct = alpha_direct
        self.alpha_min = int(alpha_direct - int(self.area_alpha / 2))
        self.alpha_max = int(alpha_direct + int(self.area_alpha / 2))

    def check_end(self):
        if len(self.particles) == 0:
            return True
        else:
            return False

    def process_effect(self, screen, opt_add):
        if opt_add == 1:
            if self.npm > 0 or self.npm == -7:
                np_add = 0
                while np_add < self.npps:
                    self.add_particle()
                    np_add += 1
        self.process_particle(screen)
        self.del_particle()

    def add_particle(self):
        pos_start = self.pce
        opt_add = rd.randint(1, self.rbp)
        if opt_add == 1:
            if self.npm != -7:
                self.npm -= 1
            if self.in_out > 0:  # out
                size_particle = rd.randint(self.size_min, self.size_max)
                full_size = [size_particle, size_particle]
                new_alpha = rd.randint(self.alpha_min, self.alpha_max)
                new_v = rd.randint(1, self.v_particle_max)
                new_particle = Particle_1(new_v, full_size, new_alpha, self.in_out, self.case, pos_start, self.v_size,
                                          self.g, self.color_light)
                self.particles.append(new_particle)

            else:  # in
                new_pce = self.pce
                new_distance = rd.randint(self.rmine, self.rmaxe)
                new_alpha = rd.randint(self.alpha_min, self.alpha_max)
                new_v = rd.randint(int(self.v_particle_max / 3), self.v_particle_max)
                if new_v == 0:
                    new_v = 1
                new_x = new_distance * math.cos(deg_to_rad(new_alpha)) + new_pce[0]
                new_y = -new_distance * math.sin(deg_to_rad(new_alpha)) + new_pce[1]
                pos_start = [new_x, new_y]
                size_particle = rd.randint(self.size_min, self.size_max)
                full_size = [size_particle, size_particle]
                new_particle = Particle_1(new_v, full_size, new_alpha, self.in_out, self.case, pos_start, self.v_size,
                                          self.g, self.color_light)
                self.particles.append(new_particle)

    def process_particle(self, screen):
        for particle in self.particles:
            particle.process_total(screen)

    def del_particle(self):
        if self.in_out > 0:
            n = 0
            while n < len(self.particles):
                if self.particles[n].size[0] <= 1:
                    del self.particles[n]
                    n -= 1
                n += 1
        else:
            n = 0
            while n < len(self.particles):
                if process_distance_1(self.particles[n].pos, self.pce) <= abs(self.v_particle_max):
                    del self.particles[n]
                    n -= 1
                n += 1

    def show(self, suf, runtime):
        for particle in self.particles:
            particle.show(suf, runtime)


class Effect_kind_2_2:
    def __init__(self, pos_center_effect, alpha_direct, area_alpha, in_out,
                 v_particle_max, size_max, size_min, v_size, radius_max_effect, rbp, g, color, color_light, npm, npps):
        # name: particle effect 2 basic
        self.pce = pos_center_effect
        self.particles = []
        self.alpha_direct = alpha_direct
        self.area_alpha = area_alpha
        self.alpha_min = int(alpha_direct - int(self.area_alpha / 2))
        self.alpha_max = int(alpha_direct + int(self.area_alpha / 2))
        self.v_particle_max = v_particle_max
        self.rbp = rbp
        self.size_max = size_max
        self.size_min = size_min
        self.v_size = v_size
        self.in_out = in_out
        self.npps = npps
        self.rmaxe = radius_max_effect
        self.rmine = int(radius_max_effect / 3)
        if self.in_out > 0:
            self.g = g
        else:
            self.g = 0
        self.color = color
        self.color_light = color_light
        self.npm = npm

    def update_poss_alpha_direct(self, pos_center_effect, alpha_direct):
        if self.in_out < 0:
            if process_distance_1(self.pce, pos_center_effect) > 0:
                self.particles = []
        self.pce = pos_center_effect
        self.alpha_direct = alpha_direct
        self.alpha_min = int(alpha_direct - int(self.area_alpha / 2))
        self.alpha_max = int(alpha_direct + int(self.area_alpha / 2))

    def check_end(self):
        if self.npm == 0:
            return 1
        else:
            return 0

    def process_effect(self, screen, opt_add):
        if opt_add == 1:
            if self.npm > 0 or self.npm == -7:
                np_add = 0
                while np_add < self.npps:
                    self.add_particle()
                    np_add += 1
        self.process_particle(screen)
        self.del_particle()

    def add_particle(self):
        pos_start = self.pce
        opt_add = rd.randint(1, self.rbp)
        if opt_add == 1:
            if self.npm != -7:
                self.npm -= 1
            if self.in_out > 0:  # out
                size_particle = rd.randint(self.size_min, self.size_max)
                new_alpha = rd.randint(self.alpha_min, self.alpha_max)
                new_v = rd.randint(1, self.v_particle_max)
                new_particle = Particle_2(new_v, size_particle, new_alpha, pos_start, self.v_size,
                                          self.g, self.color, self.color_light, self.in_out)
                self.particles.append(new_particle)

            else:  # in
                new_pce = self.pce
                new_distance = rd.randint(self.rmine, self.rmaxe)
                new_alpha = rd.randint(self.alpha_min, self.alpha_max)
                new_v = rd.randint(int(self.v_particle_max / 3), self.v_particle_max)
                if new_v == 0:
                    new_v = 1
                new_x = new_distance * math.cos(deg_to_rad(new_alpha)) + new_pce[0]
                new_y = -new_distance * math.sin(deg_to_rad(new_alpha)) + new_pce[1]
                pos_start = [new_x, new_y]
                size_particle = rd.randint(self.size_min, self.size_max)
                new_particle = Particle_2(new_v, size_particle, new_alpha, pos_start, self.v_size,
                                          self.g, self.color, self.color_light, self.in_out)
                self.particles.append(new_particle)

    def process_particle(self, screen):
        for particle in self.particles:
            particle.process_total(screen)

    def del_particle(self):
        if self.in_out > 0:
            n = 0
            while n < len(self.particles):
                if self.particles[n].size <= 1:
                    del self.particles[n]
                    n -= 1
                n += 1
        else:
            n = 0
            while n < len(self.particles):
                if process_distance_1(self.particles[n].pos, self.pce) <= abs(self.v_particle_max):
                    del self.particles[n]
                    n -= 1
                n += 1

    def show(self, suf):
        for particle in self.particles:
            particle.show(suf)


class Effect_kind_2_3:
    def __init__(self, pos_center_effect, alpha_direct, d_effect,
                 v_particle_max, size_max, size_min, v_size, radius_max_effect, rbp, g, color, color_light, npm, npps):
        # name: straight
        self.pce = pos_center_effect
        self.d_effect = d_effect / 2
        self.particles = []
        self.alpha_direct = alpha_direct
        self.v_particle_max = v_particle_max
        self.rbp = rbp
        self.size_max = size_max
        self.size_min = size_min
        self.v_size = v_size
        self.rmaxe = radius_max_effect
        self.rmine = int(radius_max_effect / 3)
        self.g = g
        self.color = color
        self.color_light = color_light
        self.npm = npm
        self.npps = npps

    def update_poss_alpha_direct(self, pos_center_effect, alpha_direct):
        self.pce = pos_center_effect
        self.alpha_direct = alpha_direct

    def check_end(self):
        if len(self.particles) == 0:
            return True
        else:
            return False

    def process_effect(self, screen, opt_add):
        if opt_add == 1:
            if self.npm > 0 or self.npm == -7:
                np_add = 0
                while np_add < self.npps:
                    self.add_particle()
                    np_add += 1
        self.process_particle(screen)
        self.del_particle()

    def add_particle(self):

        opt_add = rd.randint(1, self.rbp)
        if opt_add == 1:
            if self.npm != -7:
                self.npm -= 1
            pos_start = [0, 0]
            new_d = rd.randint(self.d_effect * -1, self.d_effect)
            new_alpha = self.alpha_direct + 90
            pos_start[0] = self.pce[0] + math.cos(deg_to_rad(new_alpha)) * new_d
            pos_start[1] = self.pce[1] - math.sin(deg_to_rad(new_alpha)) * new_d

            size_particle = rd.randint(self.size_min, self.size_max)
            new_size = size_particle
            new_v = rd.randint(1, self.v_particle_max)
            new_particle = Particle_2(new_v, new_size, self.alpha_direct, pos_start, self.v_size, self.g, self.color,
                                      self.color_light, 1)
            self.particles.append(new_particle)

    def process_particle(self, screen):
        for particle in self.particles:
            particle.process_total(screen)

    def del_particle(self):
        n = 0
        while n < len(self.particles):
            if self.particles[n].size <= 1:
                del self.particles[n]
                n -= 1
            n += 1

    def show(self, suf):
        for particle in self.particles:
            particle.show(suf)


class Effect_kind_2_4:
    def __init__(self, pos_center_effect, alpha_direct, area_alpha,
                 v_particle_max, size_max, size_min, v_size, g, color, color_light, npm):
        # name: explode
        self.pce = pos_center_effect
        self.particles = []
        self.alpha_direct = alpha_direct
        self.area_alpha = area_alpha
        self.alpha_min = int(alpha_direct - int(self.area_alpha / 2))
        self.alpha_max = int(alpha_direct + int(self.area_alpha / 2))
        self.v_particle_max = v_particle_max
        self.size_max = size_max
        self.size_min = size_min
        self.v_size = v_size
        self.g = g
        self.color = color
        self.color_light = color_light
        self.n_particles_max = npm
        self.num_p = 0

    def update_poss_alpha_direct(self, pos_center_effect, alpha_direct):
        self.pce = pos_center_effect
        self.alpha_direct = alpha_direct
        self.alpha_min = int(alpha_direct - int(self.area_alpha / 2))
        self.alpha_max = int(alpha_direct + int(self.area_alpha / 2))

    def check_end(self):
        if len(self.particles) == 0:
            return 1
        else:
            return 0

    def process_effect(self, screen, opt_add):
        if opt_add == 1:
            while self.n_particles_max > 0:
                self.add_particle()
                self.n_particles_max -= 1
        self.process_particle(screen)
        self.del_particle()

    def add_particle(self):
        pos_start = self.pce
        size_particle = rd.randint(self.size_min, self.size_max)
        new_size = size_particle
        new_alpha = rd.randint(self.alpha_min, self.alpha_max)
        new_v = rd.randint(1, self.v_particle_max)
        new_particle = Particle_2(new_v, new_size, new_alpha, pos_start, self.v_size, self.g, self.color,
                                  self.color_light, 1)
        self.particles.append(new_particle)
        self.n_particles_max -= 1

    def process_particle(self, screen):
        for particle in self.particles:
            particle.process_total(screen)

    def del_particle(self):
        n = 0
        while n < len(self.particles):
            if self.particles[n].size <= 1:
                del self.particles[n]
                n -= 1
            n += 1

    def show(self, suf):
        for particle in self.particles:
            particle.show(suf)


class Effect_kind_2_5:
    def __init__(self, pos_center_effect, alpha_direct, area_alpha,
                 v_particle_max, size_max, size_min, v_size, radius_max_effect, rbp, g, color):
        # name: smoke
        self.pce = pos_center_effect
        self.particles = []
        self.alpha_direct = alpha_direct
        self.area_alpha = area_alpha
        self.alpha_min = int(alpha_direct - int(self.area_alpha / 2))
        self.alpha_max = int(alpha_direct + int(self.area_alpha / 2))
        self.v_particle_max = v_particle_max
        self.rbp = rbp
        self.size_max = size_max
        self.size_min = size_min
        self.v_size = v_size
        self.rmaxe = radius_max_effect
        self.rmine = int(radius_max_effect / 3)
        self.g = g
        self.color = color

    def update_poss_alpha_direct(self, pos_center_effect, alpha_direct):
        self.pce = pos_center_effect
        self.alpha_direct = alpha_direct
        self.alpha_min = int(alpha_direct - int(self.area_alpha / 2))
        self.alpha_max = int(alpha_direct + int(self.area_alpha / 2))

    def check_end(self):
        if len(self.particles) == 0:
            return True
        else:
            return False

    def process_effect(self, screen, opt_add):
        if opt_add == 1:
            self.add_particle()
        self.process_particle(screen)
        self.del_particle()

    def add_particle(self):
        pos_start = self.pce
        opt_add = rd.randint(1, self.rbp)
        if opt_add == 1:
            size_particle = rd.randint(self.size_min, self.size_max)
            new_size = size_particle
            new_alpha = rd.randint(self.alpha_min, self.alpha_max)
            new_v = rd.randint(1, self.v_particle_max)
            new_value_color = rd.randint(50, 70)
            new_color = (int(self.color[0] * new_value_color / 100), int(self.color[1] * new_value_color / 100),
                         int(self.color[2] * new_value_color / 100))
            new_particle = Particle_3(new_v, new_size, new_alpha, pos_start, self.v_size, self.g, new_color)
            self.particles.append(new_particle)

    def process_particle(self, screen):
        for particle in self.particles:
            particle.process_total(screen)

    def del_particle(self):
        n = 0
        while n < len(self.particles):
            if self.particles[n].size <= 1:
                del self.particles[n]
                n -= 1
            n += 1

    def show(self, suf):
        for particle in self.particles:
            particle.show(suf)


class Effect_kind_2_6:
    def __init__(self, pos_center_effect, alpha_direct, area_alpha,
                 v_particle_max, case, size_max, size_min, v_size, rbp):
        # name: jet effect 1
        self.pce = pos_center_effect
        self.particles = []
        self.alpha_direct = alpha_direct
        self.area_alpha = area_alpha
        self.alpha_min = int(alpha_direct - int(self.area_alpha / 2))
        self.alpha_max = int(alpha_direct + int(self.area_alpha / 2))
        self.v_particle_max = v_particle_max
        self.rbp = rbp
        self.size_max = size_max
        self.size_min = size_min
        self.case = case
        self.v_size = v_size

    def update_poss_alpha_direct(self, pos_center_effect, alpha_direct):
        self.pce = pos_center_effect
        self.alpha_direct = alpha_direct
        self.alpha_min = int(alpha_direct - int(self.area_alpha / 2))
        self.alpha_max = int(alpha_direct + int(self.area_alpha / 2))

    def check_end(self):
        if len(self.particles) == 0:
            return True
        else:
            return False

    def process_effect(self, screen, opt_add):
        if opt_add == 1:
            self.add_particle()
        self.process_particle(screen)
        self.del_particle()

    def add_particle(self):
        pos_start = self.pce
        opt_add = rd.randint(1, self.rbp)
        if opt_add == 1:
            full_size = [self.size_max, self.size_max]
            new_alpha = rd.randint(self.alpha_min, self.alpha_max)
            new_particle = Particle_4(self.v_particle_max, full_size, new_alpha, self.case, pos_start, self.v_size)
            self.particles.append(new_particle)

    def process_particle(self, screen):
        for particle in self.particles:
            particle.process_total(screen)

    def del_particle(self):
        n = 0
        while n < len(self.particles):
            if self.particles[n].size[0] <= self.size_min:
                del self.particles[n]
                n -= 1
            n += 1

    def show(self, suf, runtime):
        for particle in self.particles:
            particle.show(suf, runtime)
