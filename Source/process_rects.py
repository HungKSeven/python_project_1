from tv import *


def process_1(rect_1, rect_2):
    # check rect 1 vs 2 check vs true: out
    pos_s1 = []
    pos_s1.append((rect_1[0], rect_1[1]))
    pos_s1.append((rect_1[0] + rect_1[2], rect_1[1]))
    pos_s1.append((rect_1[0] + rect_1[2], rect_1[1] + rect_1[3]))
    pos_s1.append((rect_1[0], rect_1[1] + rect_1[3]))

    pos_s2 = []
    pos_s2.append((rect_2[0], rect_2[1]))
    pos_s2.append((rect_2[0] + rect_2[2], rect_2[1]))
    pos_s2.append((rect_2[0] + rect_2[2], rect_2[1] + rect_2[3]))
    pos_s2.append((rect_2[0], rect_2[1] + rect_2[3]))

    check1 = True
    for pos in pos_s1:
        if rect_2[0] <= pos[0] <= rect_2[0] + rect_2[2] and rect_2[1] <= pos[1] <= rect_2[1] + rect_2[3]:
            check1 = False
            break

    check2 = True
    for pos in pos_s2:
        if rect_1[0] <= pos[0] <= rect_1[0] + rect_1[2] and rect_1[1] <= pos[1] <= rect_1[1] + rect_1[3]:
            check2 = False
            break

    check3 = True
    if rect_1[1] < rect_2[1] and rect_1[1] + rect_1[3] > rect_2[1] + rect_2[3] and rect_1[0] > rect_2[0] and rect_1[0] + \
            rect_1[2] < rect_2[0] + rect_2[2]:
        check3 = False

    check4 = True
    if rect_2[1] < rect_1[1] and rect_2[1] + rect_2[3] > rect_1[1] + rect_1[3] and rect_2[0] > rect_1[0] and rect_2[0] + \
            rect_2[2] < rect_1[0] + rect_1[2]:
        check4 = False

    if check1 and check2 and check3 and check4:
        return True
    else:
        return False


def process_2(rect_1, rects):
    # check rect 1 vs rects check out true : out
    if len(rects) == 0:
        return True, 0
    else:
        num = 0
        for n in range(0, len(rects)):
            if not process_1(rect_1, rects[n]):
                num += 1

        if num > 0:
            return False, num
        else:
            return True, 0


def process_3(pos, rect):
    # check out: true:out
    if rect[0] <= pos[0] <= rect[0] + rect[2] and rect[1] <= pos[1] <= rect[1] + rect[3]:
        return False
    else:
        return True


def process_4(rect, rect_box):
    # check rect in rect_box: true:in
    pos_s = []
    pos_s.append((rect[0], rect[1]))
    pos_s.append((rect[0] + rect[2], rect[1]))
    pos_s.append((rect[0] + rect[2], rect[1] + rect[3]))
    pos_s.append((rect[0], rect[1] + rect[3]))
    n = 0
    for pos in pos_s:
        if rect_box[0] <= pos[0] <= rect_box[0] + rect_box[2] and rect_box[1] <= pos[1] <= rect_box[1] + rect_box[3]:
            n += 1
    if n == 4:
        return True
    else:
        return False


def find_s_rect(rect):
    return rect[2] * rect[3]


def poss_in_rect_1(size_rect_in, rect_box):
    pos_1 = [rect_box[0] + int(rect_box[2] / 2), rect_box[1] + 30 + int(size_rect_in[1] / 2)]
    pos_2 = [rect_box[0] + 30 + int(size_rect_in[0] / 2), rect_box[1] + int(rect_box[3] / 2)]
    pos_3 = [rect_box[0] + rect_box[2] - 30 - int(size_rect_in[0] / 2), rect_box[1] + int(rect_box[3] / 2)]
    pos_4 = [int((pos_1[0] + pos_2[0]) / 2), int((pos_1[1] + pos_2[1]) / 2)]
    pos_5 = [int((pos_1[0] + pos_3[0]) / 2), int((pos_1[1] + pos_3[1]) / 2)]
    pos_6 = [rect_box[0] + int(rect_box[2] / 2), rect_box[1] + int(rect_box[3] / 2)]
    poss = pos_1, pos_2, pos_3, pos_4, pos_5, pos_6
    return poss


def check_in_rects_room(rect_check, rects_room):
    n_rect = 0
    for n in range(0, len(rects_room)):
        if process_4(rect_check, rects_room[n]):
            n_rect += 1
    if n_rect > 0:
        return True
    else:
        return False


def check_rect_vs_circle(rect, pcc, radius):
    new_rect = [0, 0, 0, 0]
    new_rect[0] = rect[0] - radius
    new_rect[1] = rect[1] - radius
    new_rect[2] = rect[2] + radius * 2
    new_rect[3] = rect[3] + radius * 2
    if not process_3(pcc, new_rect):
        return True
    else:
        return False
