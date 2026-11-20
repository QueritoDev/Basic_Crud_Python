from raylibpy import *

def criar_estado():
    return {
        "cadastrar_Rec": Rectangle(300, 150, 200, 50),
        "listar_Rec": Rectangle(300, 230, 200, 50),
        "sair_Rec": Rectangle(300, 310, 200, 50)
    }


def update_menu(state):
    mouse_pos = get_mouse_position()

    if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
        if check_collision_point_rec(mouse_pos, state["cadastrar_Rec"]):
            return "cadastro"
        if check_collision_point_rec(mouse_pos, state["listar_Rec"]):
            return "listar"
        if check_collision_point_rec(mouse_pos, state["sair_Rec"]):
            return "sair"

    return None

def draw_menu(state):
    draw_text("BIBLIOTECA", 300, 50, 40, DARKGRAY)

    draw_rectangle_rec(state["cadastrar_Rec"], GREEN)
    draw_text("Cadastrar", int(state["cadastrar_Rec"].x) + 20, int(state["cadastrar_Rec"].y) + 10, 25, WHITE)

    draw_rectangle_rec(state["listar_Rec"], BLUE)
    draw_text("Listar", int(state["listar_Rec"].x) + 20, int(state["listar_Rec"].y) + 10, 25, WHITE)

    draw_rectangle_rec(state["sair_Rec"], RED)
    draw_text("Sair", int(state["sair_Rec"].x) + 20, int(state["sair_Rec"].y) + 10, 25, WHITE)
