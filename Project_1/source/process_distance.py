def process_distance_1(pos1, pos2):
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    d = (dx ** 2 + dy ** 2) ** (1 / 2)
    return d


def check_in_distance(pos, pos_check, radius):
    if process_distance_1(pos, pos_check) <= radius:
        return True
    else:
        return False


