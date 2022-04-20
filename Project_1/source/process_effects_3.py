from process_1_lighting import Lightning


class Effect_kind_3_1:
    def __init__(self, pos_start, pos_end, num_lighting, color):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.lightings = []
        self.color = color
        self.num = num_lighting
        self.add_lighting(0)

    def upd_pos_end(self, new_pos_end, runtime):
        self.pos_end = new_pos_end
        self.lightings = []
        self.add_lighting(runtime)

    def add_lighting(self, runtime):
        for n in range(0, self.num):
            self.lightings.append(Lightning(self.pos_start, self.pos_end, self.color, runtime, 3))

        # for n in range(0,7):

    def process_effect(self, runtime,screen):
        for lighting in self.lightings:
            lighting.create_poss(runtime,screen)

    def show(self, suf):
        for lighting in self.lightings:
            lighting.show(suf)


class Effect_kind_3_2:
    def __init__(self, pos_start, num_lighting, color, radius):
        self.pos_start = pos_start
        self.radius = radius
        self.lightings = []
        self.color = color
        self.num = num_lighting
        self.add_lighting(0)

    def upd_pos_end(self, new_pos_end, runtime):
        self.pos_end = new_pos_end
        self.lightings = []
        self.add_lighting(runtime)

    def add_lighting(self, runtime):
        for n in range(0, self.num):
            self.lightings.append(Lightning(self.pos_start, self.pos_end, self.color, runtime, 1))

    def process_effect(self, runtime,screen):
        for lighting in self.lightings:
            lighting.create_poss(runtime,screen)

    def show(self, suf):
        for lighting in self.lightings:
            lighting.show(suf)
