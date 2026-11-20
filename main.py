from raylibpy import *
import crud
import cadastro

def main():

    # INIT

    init_window(800, 450, "raylib [core] example - basic window")
    set_target_fps(60)

    state = cadastro.criar_estado()
    
    while not window_should_close():

        cadastro.update_cadastro_raylib(state)

        # DRAW
        begin_drawing()
        clear_background(GRAY)
        cadastro.draw_cadastro_raylib(state)

        end_drawing()

    
    # UNLOAD
    close_window()


if __name__ == '__main__':
    main()
