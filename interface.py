from raylibpy import *
import crud

def main():

    # INIT

    init_window(800, 450, "raylib [core] example - basic window")
    set_target_fps(60)
    
    create_Rec = Rectangle(300,180, 90, 40)
    list_Rec = Rectangle(300,180, 90, 40)

    digitando = False
    texto = ""
    
    while not window_should_close():
        
        # UPDATE
        mouse_pos = get_mouse_position()

        ## RETANGULO DE CRIACAO (COLISÃO)
        if(is_mouse_button_pressed(MOUSE_BUTTON_LEFT) and check_collision_point_rec(mouse_pos, create_Rec)):
            digitando = True
            texto = "" #Começa vazio (ou mantem o anterior)

        if digitando:
            char = get_char_pressed()
            if char > 0:
                texto += chr(char)

            if is_key_pressed(KEY_BACKSPACE) and len(texto) > 0:
                texto = texto[:-1]

            if is_key_pressed(KEY_ENTER):
                if texto.strip():
                    crud.cadastrar(texto.strip())
                digitando = False
                texto = ""

            # ESC cancela
            if is_key_pressed(KEY_ESCAPE):
                digitando = False
                texto = ""            
        
        # DRAW
        begin_drawing()
        clear_background(GRAY)
        draw_rectangle_rec(create_Rec, GREEN)
        draw_text("Criar", create_Rec.x, create_Rec.y, 30, WHITE)
        if digitando:
            draw_text("Digite um nome (ENTER confirma / ESC cancela):", 200, 250, 20, BLACK)
            draw_rectangle(200, 280, 400, 40, RAYWHITE)
            draw_rectangle_lines(200, 280, 400, 40, BLACK)
            draw_text(texto, 210, 290, 20, BLACK)
            # cursor piscando (opcional)
            if int(get_time() * 2) % 2 == 0:
                cursor_x = 210 + measure_text(texto, 20)
                draw_text("|", cursor_x, 290, 20, BLACK)

        end_drawing()

    
    # UNLOAD
    close_window()


if __name__ == '__main__':
    main()