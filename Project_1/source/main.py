from windowgame import Windowgame
from process_event_wdg import *
from colors import *
from process_role import Main_role
from room import Rooms
from tv import *
from process_mouse import Game_mouse
from screen import Screen
from process_animation import Animation
from text_game import Text
from process_alpha import *
from process_distance import *
from process_effects_2 import Effect_kind_2_1, Effect_kind_2_2, Effect_kind_2_5, Effect_kind_2_6
from process_effects_3 import Effect_kind_3_1, Effect_kind_3_2
from process_rects import *
from process_all_gameplay2 import Cubes49

pg.init()
# sounds


# loading
wdg = Windowgame()
screen_game = Screen()

rooms = Rooms()

main_role = Main_role()

game_mouse = Game_mouse()
pos_center_wdg = [683, 384]

pg.event.set_grab(False)
pg.mouse.set_visible(True)
pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_CROSSHAIR)


def intro():
    pg.mouse.set_pos(683, 384)
    game_mouse.case = 1
    game_mouse.stt_show = 0
    stt_intro = 1
    font_case = 191
    pos_tig_1 = 683, 364
    pos_tig_2 = 683, 454
    pos_tig_3 = 683, 514
    color_bg = [0, 0, 0]
    color_text_1 = [240, 240, 240]
    color_intro_1 = [240, 240, 240]
    radius_intro_1 = 170
    width_intro = 30
    radius_intro_2 = 0
    radius_intro_8 = radius_intro_1
    color_intro_2 = [0, 0, 0]
    radiuss_intro_3 = [0, 0, 0, 0, 0, 0]
    colors_intro_3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    d_intro_1 = 0
    pos_intro_7 = 0, 0
    poss_polygon = [(683, 384)]
    alpha = 240
    x = pos_center_wdg[0] + math.cos(deg_to_rad(alpha)) * radius_intro_1
    y = pos_center_wdg[1] - math.sin(deg_to_rad(alpha)) * radius_intro_1
    poss_polygon.append((x, y))
    case_stt_intro_7 = 0
    case_stt_intro_8 = 0
    effect_intro_1 = Effect_kind_2_1(pos_center_effect=pos_center_wdg, alpha_direct=90, area_alpha=160,
                                     v_particle_max=2,
                                     in_out=1, case=0, size_max=23, size_min=10, v_size=0.2, radius_max_effect=0, rbp=5,
                                     g=0, color_light=black, npm=-7, npps=1)

    effect_intro_2 = Effect_kind_2_1(pos_center_effect=pos_center_wdg, alpha_direct=90, area_alpha=360,
                                     v_particle_max=10,
                                     in_out=-1, case=0, size_max=7, size_min=1, v_size=0.2, radius_max_effect=300,
                                     rbp=2, g=0, color_light=black, npm=-7, npps=1)
    while alpha > -120:
        x = pos_center_wdg[0] + math.cos(deg_to_rad(alpha)) * radius_intro_1
        y = pos_center_wdg[1] - math.sin(deg_to_rad(alpha)) * radius_intro_1
        poss_polygon.append((x, y))
        alpha -= 0.5

    check_1_intro_5 = False
    alpha_intro_5 = -120
    opt_add_effect_intro_1 = 0
    alpha_clock_intro = -120
    pos_clock_circle_intro_5 = [
        pos_center_wdg[0] + math.cos(deg_to_rad(alpha_clock_intro)) * (radius_intro_1 - width_intro / 2),
        pos_center_wdg[1] - math.sin(deg_to_rad(alpha_clock_intro)) * (radius_intro_1 - width_intro / 2)]

    alpha_intro_5_1 = -120
    alpha_intro_5_2 = -120
    pos_intro_5_2 = [
        pos_center_wdg[0] + math.cos(deg_to_rad(alpha_intro_5_2)) * (radius_intro_1 - width_intro / 2),
        pos_center_wdg[1] - math.sin(deg_to_rad(alpha_intro_5_2)) * (radius_intro_1 - width_intro / 2)]
    color_intro_4 = [240, 240, 240]
    pos_intro_4 = pos_intro_5_2
    pos_intro_8_3 = [683, 384]
    v_intro_8_3 = 10
    radiuss_intro_8_3 = radius_intro_1
    opt_add_effect_intro_2 = 0
    pos_effect_intro_1 = [0, 0]
    pos_intro_8_3_2 = [0, 0]
    case_stt_intro_9 = 0
    pos_intro_9_3 = [0, 0]
    alpha_intro_7_3 = 0
    vx_intro_9_3 = 0
    vy_intro_9_3 = 0
    v_intro_9_3 = 0
    pos_intro_9_3_2 = [0, 0]
    radiuss_intro_9_3 = 0
    case_stt_intro_10 = 0
    radiuss_intro_10_3 = 0
    pos_intro_10_3 = 0
    case_stt_intro_11 = 3
    value_intro_11 = 0
    case_stt_intro_12 = 0
    pos_intro_12_3 = [0, 0]
    radiuss_intro_12_3 = width_intro / 2
    v_intro_9_3_2 = 10
    vx_intro_9_3_2 = 0
    vy_intro_9_3_2 = 0
    d_intro_8_3_2 = 0
    vx_intro_8_3 = 0
    vy_intro_8_3 = 0
    case_game_play = 0

    runing = True
    clock = pg.time.Clock()
    runtime = 0

    while runing:
        print(stt_intro)
        # runtime
        dt = clock.tick(60)
        runtime += dt
        '''if runtime > 60000:
            runtime = 0
            room.reset_time(runtime)
            main_role.reset_time(runtime)'''
        print('runtime:', runtime, '|dt:', dt, '|fps:', round(1000 / dt, 1))
        game_mouse.update(pg.mouse.get_pos())

        # process event total
        events = pg.event.get()
        process_quit(events)
        effect_intro_1.process_effect(screen_game, opt_add_effect_intro_1)
        effect_intro_2.process_effect(screen_game, opt_add_effect_intro_2)

        text_in_game_1 = Text(font_case, 90, 'K STORY 0', color_text_1, 0)
        text_in_game_2 = Text(font_case, 45, 'by', color_text_1, 0)
        text_in_game_3 = Text(font_case, 45, 'K Seven', color_text_1, 0)

        if stt_intro == 1:
            if color_bg[0] < 240:
                color_bg[0] += 1
                color_bg[1] += 1
                color_bg[2] += 1
            else:
                stt_intro = 2
        if stt_intro == 2:
            if color_text_1[0] > 0:
                color_text_1[0] -= 1
                color_text_1[1] -= 1
                color_text_1[2] -= 1
            else:
                stt_intro=3

        if stt_intro == 3:
            if color_text_1[0] < 240:
                color_text_1[0] += 1
                color_text_1[1] += 1
                color_text_1[2] += 1
            else:
                stt_intro = 4
                pg.mouse.set_pos(pos_center_wdg)

        if stt_intro == 4:
            if color_intro_4[0] > 0:
                color_intro_4[0] -= 2
                color_intro_4[1] -= 2
                color_intro_4[2] -= 2
            else:
                stt_intro = 5
                opt_add_effect_intro_1 = 1

        if stt_intro == 5:
            if color_intro_1[0] > 0:
                color_intro_1[0] -= 2
                color_intro_1[1] -= 2
                color_intro_1[2] -= 2
            if len(poss_polygon) >= 3:
                del poss_polygon[len(poss_polygon) - 1]
                pos_effect_intro_1 = [
                    pos_center_wdg[0] + math.cos(deg_to_rad(alpha_intro_5)) * (radius_intro_1 - width_intro / 2),
                    pos_center_wdg[1] - math.sin(deg_to_rad(alpha_intro_5)) * (radius_intro_1 - width_intro / 2)]
                alpha_intro_5 += 0.5
                effect_intro_1.update_poss_alpha_direct(pos_effect_intro_1, alpha_intro_5 - 90)
                check_1_intro_5 = True
            else:
                opt_add_effect_intro_1 = 0
                check_1_intro_5 = False
            if not check_1_intro_5 and effect_intro_1.check_end():
                stt_intro = 6
                pg.mouse.set_pos(pos_center_wdg)
                game_mouse.update(pos_center_wdg)
                game_mouse.stt_show = 1

        if stt_intro == 6:
            d_intro_1 = process_distance_1(game_mouse.pos, pos_center_wdg)
            if process_key_4(events):
                stt_intro = 7
                pos_intro_7 = game_mouse.pos
                if d_intro_1 < radius_intro_1 - width_intro:
                    case_stt_intro_7 = 1
                else:
                    if radius_intro_1 - width_intro <= d_intro_1 < radius_intro_1:
                        case_stt_intro_7 = 2
                    else:
                        case_stt_intro_7 = 3
                        pos_intro_8_3_2 = pos_intro_7
                        d_intro_8_3_2 = process_distance_1(pos_intro_8_3_2, pos_center_wdg)
                        alpha_intro_7_3 = process_alpha_1(pos_center_wdg, pos_intro_7)
                        vx_intro_8_3 = v_intro_8_3 * math.cos(deg_to_rad(alpha_intro_7_3 + 180))
                        vy_intro_8_3 = -v_intro_8_3 * math.sin(deg_to_rad(alpha_intro_7_3 + 180))

        if stt_intro == 7:
            if case_stt_intro_7 == 1:
                if radius_intro_2 < radius_intro_1 - width_intro - d_intro_1:
                    radius_intro_2 += 4
                    check_1 = True
                else:
                    check_1 = False
                if not check_1:
                    stt_intro = 8
                    case_stt_intro_8 = 1
            if case_stt_intro_7 == 3:
                if radius_intro_2 + radius_intro_1 < d_intro_1:
                    radius_intro_2 += 7
                    check_1 = True
                else:
                    check_1 = False
                if not check_1:
                    stt_intro = 8
                    case_stt_intro_8 = 3

        if stt_intro == 8:
            if case_stt_intro_8 == 1:
                if radius_intro_1 < 700:
                    radius_intro_1 += 5
                if color_intro_1[0] < 240:
                    color_intro_1[0] += 2
                    color_intro_1[1] += 2
                    color_intro_1[2] += 2

                if radiuss_intro_3[5] < radius_intro_8:
                    radiuss_intro_3[0] += 5
                    if colors_intro_3[0][0] < 240:
                        colors_intro_3[0][0] += 2
                        colors_intro_3[0][1] += 2
                        colors_intro_3[0][2] += 2
                    for n in range(1, 6):
                        if radiuss_intro_3[n - 1] > radius_intro_8 and radiuss_intro_3[n] < 900:
                            radiuss_intro_3[n] += 5
                            if colors_intro_3[n][0] < 240:
                                colors_intro_3[n][0] += 2
                                colors_intro_3[n][1] += 2
                                colors_intro_3[n][2] += 2
                else:
                    stt_intro = 9
                    case_stt_intro_9 = 1

            if case_stt_intro_8 == 3:
                if radiuss_intro_8_3 < 40000:
                    pos_intro_8_3[0] += vx_intro_8_3
                    pos_intro_8_3[1] += vy_intro_8_3
                    if process_distance_1(pos_intro_8_3, pos_center_wdg) > d_intro_8_3_2:
                        radiuss_intro_8_3 += v_intro_8_3
                        v_intro_8_3 += 50
                        if opt_add_effect_intro_2 == 0:
                            opt_add_effect_intro_2 = 1
                            effect_intro_2.update_poss_alpha_direct(pos_center_wdg, 90)
                    vx_intro_8_3 = v_intro_8_3 * math.cos(deg_to_rad(alpha_intro_7_3 + 180))
                    vy_intro_8_3 = -v_intro_8_3 * math.sin(deg_to_rad(alpha_intro_7_3 + 180))
                else:
                    stt_intro = 9
                    case_stt_intro_9 = 3
                    d_intro_9 = radiuss_intro_8_3 * 2 - width_intro
                    radiuss_intro_9_3 = radiuss_intro_8_3
                    pos_intro_9_3_2 = [int(pos_intro_8_3_2[0]), int(pos_intro_8_3_2[1])]
                    pos_intro_9_3[0] = int(round(pos_intro_8_3[0] + math.cos(deg_to_rad(alpha_intro_7_3)) * d_intro_9))
                    pos_intro_9_3[1] = int(round(pos_intro_8_3[1] - math.sin(deg_to_rad(alpha_intro_7_3)) * d_intro_9))
                    v_intro_9_3 = v_intro_8_3

        if stt_intro == 9:
            if case_stt_intro_9 == 1:
                stt_intro = 10
                case_stt_intro_10 = 1
            if case_stt_intro_9 == 3:
                if process_distance_1(pos_intro_9_3, pos_center_wdg) > v_intro_9_3:
                    if v_intro_9_3 > 1000:
                        v_intro_9_3 -= 50
                    vx_intro_9_3 = v_intro_9_3 * math.cos(deg_to_rad(alpha_intro_7_3 + 180))
                    vy_intro_9_3 = -v_intro_9_3 * math.sin(deg_to_rad(alpha_intro_7_3 + 180))
                    pos_intro_9_3[0] += vx_intro_9_3
                    pos_intro_9_3[1] += vy_intro_9_3
                    radiuss_intro_9_3 -= v_intro_9_3
                else:
                    d_intro_9_3 = process_distance_1(pos_intro_9_3, pos_center_wdg)
                    pos_intro_10_3 = pos_center_wdg
                    radiuss_intro_10_3 = int(radiuss_intro_9_3 - d_intro_9_3)
                    stt_intro = 10
                    case_stt_intro_10 = 3

        if stt_intro == 10:
            if case_stt_intro_10 == 1:
                runing = False
                case_game_play = 1
            if case_stt_intro_10 == 3:
                if radiuss_intro_10_3 > width_intro / 2:
                    radiuss_intro_10_3 -= 70
                else:
                    stt_intro = 11
                    case_stt_intro_11 = 3
                    opt_add_effect_intro_2 = 0

        if stt_intro == 11:
            if case_stt_intro_11 == 3:
                if value_intro_11 < 236:
                    value_intro_11 += 2
                else:
                    stt_intro = 12
                    case_stt_intro_12 = 3
                    opt_add_effect_intro_2 = 0

        if stt_intro == 12:
            if case_stt_intro_12 == 3:
                runing = False
                case_game_play = 1

        # show
        wdg.suf.fill(color_bg)

        if stt_intro == 2 or stt_intro == 3:
            text_in_game_1.show(wdg.suf, pos_tig_1)
            text_in_game_2.show(wdg.suf, pos_tig_2)
            text_in_game_3.show(wdg.suf, pos_tig_3)

        if stt_intro == 4:
            pg.draw.circle(wdg.suf, color_intro_4, pos_intro_4, width_intro / 2)
            pg.draw.circle(wdg.suf, white, pos_intro_4, 8, 2)
        if stt_intro == 5:
            pg.draw.circle(wdg.suf, black, (683, 384), radius_intro_1, width_intro)
            pos_intro_5_1 = [
                pos_center_wdg[0] + math.cos(deg_to_rad(alpha_intro_5_1)) * (radius_intro_1 - width_intro / 2),
                pos_center_wdg[1] - math.sin(deg_to_rad(alpha_intro_5_1)) * (radius_intro_1 - width_intro / 2)]
            if check_1_intro_5:
                pg.draw.circle(wdg.suf, white, pos_intro_5_1, width_intro / 2)

            if len(poss_polygon) >= 3:
                pg.draw.polygon(wdg.suf, color_bg, poss_polygon)
            if check_1_intro_5:
                pg.draw.circle(wdg.suf, black, pos_intro_5_2, width_intro / 2)

            if check_1_intro_5:
                pg.draw.circle(wdg.suf, white, pos_clock_circle_intro_5, 7)
                # pg.draw.circle(wdg.suf, black, pos_intro_5_1, width_intro / 2, 5)
            alpha_intro_5_1 += 0.5
            effect_intro_1.show(wdg.suf, runtime)
            pg.draw.circle(wdg.suf, black, pos_effect_intro_1, 7)

        if stt_intro == 6 or stt_intro == 7 or stt_intro == 8:
            if case_stt_intro_8 != 3:
                pg.draw.circle(wdg.suf, color_intro_1, (683, 384), radius_intro_1, width_intro)
            if stt_intro == 7:
                pg.draw.circle(wdg.suf, color_intro_2, pos_intro_7, radius_intro_2, 2)
            if stt_intro == 8:
                if case_stt_intro_8 == 1:
                    for n in range(0, 6):
                        pg.draw.circle(wdg.suf, colors_intro_3[n], pos_center_wdg, radiuss_intro_3[n], width_intro)
                if case_stt_intro_8 == 3:
                    effect_intro_2.show(wdg.suf, runtime)
                    pg.draw.circle(wdg.suf, black, pos_intro_8_3, radiuss_intro_8_3, width_intro)

        if stt_intro == 9:
            if case_stt_intro_9 == 3:
                effect_intro_2.show(wdg.suf, runtime)
                pg.draw.circle(wdg.suf, black, pos_intro_9_3, radiuss_intro_9_3, width_intro)
        if stt_intro == 10:
            if case_stt_intro_10 == 3:
                effect_intro_2.show(wdg.suf, runtime)
                pg.draw.circle(wdg.suf, black, pos_center_wdg, radiuss_intro_10_3, width_intro)

        if stt_intro == 11:
            if case_stt_intro_11 == 3:
                effect_intro_2.show(wdg.suf, runtime)
                pg.draw.circle(wdg.suf, black, pos_center_wdg, width_intro / 2)
                pg.draw.circle(wdg.suf, white, pos_center_wdg, 8, 2)

        if stt_intro == 12:
            if case_stt_intro_12 == 3:
                pg.draw.circle(wdg.suf, black, pos_intro_10_3, width_intro / 2)

        game_mouse.show_mouse(wdg.suf, runtime)
        # flip
        pg.display.flip()

    return case_game_play


def gameplay_1():
    pos_start_gameloop = pos_center_wdg
    runing = 1
    clock = pg.time.Clock()
    runtime = 0
    rooms.set_start_pos_role(main_role)
    stt_gameloop = 1
    game_mouse.case = 2
    game_mouse.stt_show = 0
    radius_gl_1 = 800
    color_gl_1 = [240, 240, 240]
    pg.mouse.set_pos(1163, 533)
    main_role.can_control = False

    while runing:
        # runtime
        dt = clock.tick(60)
        runtime += dt
        '''if runtime > 60000:
        runtime = 0
        room.reset_time(runtime)
        main_role.reset_time(runtime)'''
        if dt > 19:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1')
        print('runtime:', runtime, '|dt:', dt, '|fps:', round(1000 / dt, 1))
        game_mouse.update(pg.mouse.get_pos())

        # process event total
        events = pg.event.get()
        process_quit(events)

        if stt_gameloop == 1:
            main_role.direct_gun(-90, 2)
            if radius_gl_1 < 1600:
                radius_gl_1 += 23
            else:
                stt_gameloop = 2
                main_role.can_control = True
            if color_gl_1[0] > 0:
                color_gl_1[0] -= 10
                color_gl_1[1] -= 10
                color_gl_1[2] -= 10

        rooms.run_events_room(runtime, main_role, screen_game, game_mouse)

        if rooms.room_case == 2:
            game_mouse.case = 0

            check_focus_mr(events, screen_game)
            if screen_game.focus:
                screen_game.focus_mainrole(main_role)

        if rooms.room_case == 1:
            game_mouse.case = 2

        main_role.process_move(events, runtime, rooms.rects_room, screen_game)
        if stt_gameloop == 2:
            if process_event_wdg_1(events):
                main_role.can_control_hand = True
                game_mouse.stt_show = 1

        main_role.direct_gun(game_mouse.pos, 1)
        main_role.use_skills(events, game_mouse.pos, runtime, screen_game, pg.mouse.get_pressed(3)[2])
        main_role.process_skills(screen_game, rooms.rects_room, runtime)
        main_role.hp_and_mana.process_hp_mana(screen_game)

        if main_role.hp_and_mana.hp == 0:
            runing = False

        # show
        screen_game.show_off(main_role, rooms, wdg.suf, runtime)
        game_mouse.show_mouse(wdg.suf, runtime)

        # flip
        if stt_gameloop == 1:
            pg.draw.circle(wdg.suf, color_gl_1, pos_start_gameloop, radius_gl_1, 800)
        pg.display.flip()


def gameplay_2_1(n):
    game_mouse.stt_show = 1
    runing = True
    clock = pg.time.Clock()
    runtime = 0
    game_mouse.case = 2
    mt = Cubes49(n)

    while runing:
        # runtime
        dt = clock.tick(60)
        runtime += dt
        '''if runtime > 60000:
        runtime = 0
        room.reset_time(runtime)
        main_role.reset_time(runtime)'''
        print('runtime:', runtime, '|dt:', dt, '|fps:', round(1000 / dt, 1))
        game_mouse.update(pg.mouse.get_pos())

        print(pg.mouse.get_pos())
        # process event total
        events = pg.event.get()
        process_quit(events)
        mt.process_event_play(events, runtime, game_mouse.pos)

        wdg.suf.fill(black)

        mt.show(wdg.suf, runtime)

        #game_mouse.show_mouse(wdg.suf, runtime)
        pg.display.flip()


def effect_test():
    effect = Effect_kind_2_2(pos_center_effect=pos_center_wdg, alpha_direct=-90, area_alpha=360, in_out=-1,
                             v_particle_max=5,
                             size_max=1, size_min=1, v_size=0.5, radius_max_effect=300, rbp=3, g=0, color=red,
                             color_light=(70, 20, 20), npm=-7, npps=4)

    runing = True
    clock = pg.time.Clock()
    runtime = 0
    pg.mouse.set_visible(True)

    kx = []
    ky = []
    kx1 = []
    ky1 = []




'''case_game_play = intro()
if case_game_play == 1:'''
gameplay_2_1(7)



