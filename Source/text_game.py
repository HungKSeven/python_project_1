from tv import *


class Text:
    def __init__(self, font_case, size, content, color, opt_bold):
        self.font_names = pg.font.get_fonts()
        self.num_fonts = len(self.font_names)
        self.font_name = self.font_names[font_case]
        self.font = pg.font.SysFont(self.font_name, size, opt_bold)
        self.text = self.font.render(content, False, color)
        self.textRect = self.text.get_rect()

    def show(self, suf, pos):
        self.textRect.center = pos
        suf.blit(self.text, self.textRect)
