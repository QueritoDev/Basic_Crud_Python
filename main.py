from raylibpy import *
import crud_antigo
import tela_cadastro
import tela_menu
import tela_listar

def main():
    # INIT
    init_window(800, 450, "Biblioteca")
    set_target_fps(60)

    state_menu = tela_menu.criar_estado()
    state_listar = tela_listar.criar_estado()
    state_cadastro = tela_cadastro.criar_estado()
    
    tela_atual = "main_menu"

    while not window_should_close():

        if tela_atual == "main_menu":
            proxima_tela = tela_menu.update_menu(state_menu)
            if proxima_tela: tela_atual = proxima_tela

        elif tela_atual == "cadastro":
            if tela_cadastro.update_cadastro(state_cadastro) == True:
                tela_atual = "main_menu"
        elif tela_atual == "listar":
            if tela_listar.update_listar(state_listar) == True:
                tela_atual = "main_menu"
        elif tela_atual == "sair":
            break

        # DRAW
        begin_drawing()
        clear_background(GRAY)
        if tela_atual == "main_menu":
            tela_menu.draw_menu(state_menu)
        elif tela_atual == "cadastro":
            tela_cadastro.draw_cadastro(state_cadastro)
        elif tela_atual == "listar":
            tela_listar.draw_listar(state_listar)

        end_drawing()
    
    # UNLOAD
    close_window()

if __name__ == '__main__':
    main()
