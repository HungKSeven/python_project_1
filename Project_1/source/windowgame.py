from tv import *


class Windowgame:
    def __init__(self):
        self.iconwdg = None
        self.title = 'project1'
        self.mode =0
        self.listsize = pg.display.list_modes()
        self.nummode = len(self.listsize)
        self.desktopsize = self.listsize[0]
        self.hcap = 30
        self.size = self.listsize[self.mode]
        self.w = self.size[0]
        self.h = self.size[1]
        self.suf = pg.display.set_mode((self.w, self.h),pg.NOFRAME)
        pg.display.set_caption(self.title)
