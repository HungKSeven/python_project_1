from tv import pg


def process_quit(events):
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                quit()


def process_key_2(events):
    # change room case
    for event in events:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                return True
            else:
                return False


def process_key_3(events):
    # change room case
    for event in events:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_c:
                return True
            else:
                return False


def process_key_4(events):
    # change room case
    for event in events:
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                return True
            else:
                return False


def process_event_wdg_1(events):
    for event in events:
        if event.type == pg.MOUSEMOTION:
            return True
        else:
            return False


def process_event_wdg_2(events):
    for event in events:
        if event.type == pg.MOUSEBUTTONDOWN:
            return True
        else:
            return False


def process_event_wdg_3(events):
    for event in events:
        if event.type == pg.KEYDOWN:
            return True
        else:
            return False


def check_focus_mr(events,screen):
    for event in events:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                screen.focus=True

        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                screen.focus=False
