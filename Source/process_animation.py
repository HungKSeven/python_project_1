from PIL import Image
from tv import *
from colors import *


class Animation():
    def __init__(self, path, size, alpha, fps):
        self.path = path
        self.size = size
        self.alpha = alpha
        self.fps = fps
        self.pil_imgs = []
        self.pil_imgs_resize = []
        self.pyg_imgs = []
        self.rect_imgs = []
        self.timestart = 0
        self.show_time = 1000
        self.frame = 0
        self.n_frame = 0
        self.load_imgs()
        self.rect_img = self.rect_imgs[self.frame]

    def load_imgs(self):
        dir_imgs = listdir(self.path)
        for dir_img in dir_imgs:
            self.pil_imgs.append(Image.open(self.path + dir_img))

        for pil_img in self.pil_imgs:
            pil_img_resize = pil_img.resize(self.size)
            self.pyg_imgs.append(
                pg.image.fromstring(pil_img_resize.tobytes(), pil_img_resize.size, pil_img_resize.mode))

            self.pil_imgs_resize.append(pil_img_resize)

        for img in self.pyg_imgs:
            self.rect_imgs.append(img.get_rect())
        self.n_frame = len(self.pyg_imgs)

    def rotate_imgs(self, alpha):
        # for n in range(0, self.n_frame):
        img_rotated_resize = self.pil_imgs_resize[self.frame].rotate(alpha)
        # img_rotated = img_rotated.resize(self.size)
        self.pyg_imgs[self.frame] = pg.image.fromstring(img_rotated_resize.tobytes(), img_rotated_resize.size,
                                                        img_rotated_resize.mode)

    def resize_imgs(self, new_size):
        img_resize = self.pil_imgs[self.frame].resize(new_size)
        self.pyg_imgs[self.frame] = pg.image.fromstring(img_resize.tobytes(), img_resize.size,
                                                        img_resize.mode)
        self.rect_imgs[self.frame] = self.pyg_imgs[self.frame].get_rect()

    def rotate_resize_imgs(self, alpha, new_size):
        new_img = self.pil_imgs[self.frame].rotate(alpha).resize(new_size)
        self.pyg_imgs[self.frame] = pg.image.fromstring(new_img.tobytes(), new_img.size,
                                                        new_img.mode)
        self.rect_imgs[self.frame] = self.pyg_imgs[self.frame].get_rect()

    def update_rect(self, pos):
        for rect in self.rect_imgs:
            rect.center = pos
        self.rect_img = self.rect_imgs[self.frame]

    def get_check_end(self):
        if self.frame == self.n_frame:
            return True
        else:
            return False

    def show(self, suf, runtime, pos):
        self.update_rect(pos)
        suf.blit(self.pyg_imgs[self.frame], self.rect_img)
        #pg.draw.rect(suf, green, self.rect_img, 1)
        if runtime - self.timestart >= self.show_time / self.fps:
            self.timestart = runtime
            self.frame += 1
            if self.frame == self.n_frame:
                self.frame = 0
