from tv import *


def process_alpha_1(pos1, pos2):
    # pos 1 la goc
    h = pos1[1] - pos2[1]
    d = pos2[0] - pos1[0]
    alpha = 0
    if d == 0:
        if h < 0:
            alpha = -90
        if h > 0:
            alpha = 90
        if h == 0:
            alpha = 0
    else:
        tan_alpha = h / d
        alpha = math.atan(tan_alpha) * 180 / math.pi
        if d < 0:
            if h >= 0:
                alpha += 180
            if h < 0:
                alpha -= 180

    return alpha


def process_alpha_2(alpha1, alpha2):
    alpha1_360 = deg_to_deg_360o(alpha1)
    alpha2_360 = deg_to_deg_360o(alpha2)
    d_alpha = alpha2_360 - alpha1_360
    if d_alpha > 0:
        if d_alpha > 180:
            value = -1
        else:
            value = 1
    else:
        if d_alpha == 0:
            value = 0
        else:
            if abs(d_alpha) >= 180:
                value = 1
            else:
                value = -1
    return value


def process_alpha_plus(alpha):
    if alpha > 180:
        return alpha - 360
    if alpha < -180:
        return 360 + alpha
    return alpha


# alpha 1 la goc


def deg_to_deg_360o(alpha):
    if 0 <= alpha <= 180:
        return alpha
    else:
        if -180 < alpha < 0:
            return alpha + 360


def deg_to_rad(alpha_deg):
    return alpha_deg / 180 * math.pi
