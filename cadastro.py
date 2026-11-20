import json
from raylibpy import *
ARQUIVO = "dados.json"

def _carregar():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arq:
            return json.load(arq)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def _salvar(livros):
    with open (ARQUIVO, "w", encoding="utf-8") as arq:
        json.dump(livros, arq, ensure_ascii=False, indent=4)

def cadastrar(livro):
    livros = _carregar()
    livros.append(livro)
    _salvar(livros)


## PARA O RAYLIB
def criar_estado():
    return{
        "digitando": False,
        "texto": "",
        "create_Rec": Rectangle(300, 180, 90, 40),
        "list_Rec":   Rectangle(300, 240, 90, 40)
    }

def update_cadastro_raylib(state):
    # UPDATE
    mouse_pos = get_mouse_position()

    ## RETANGULO DE CRIACAO (COLISÃO)
    if(is_mouse_button_pressed(MOUSE_BUTTON_LEFT) and check_collision_point_rec(mouse_pos, state["create_Rec"])):
        state["digitando"]= True
        state["texto"] = "" #Começa vazio (ou mantem o anterior)

    if state["digitando"]:
        char = get_char_pressed()
        if char > 0:
            state["texto"]+= chr(char)

        if is_key_pressed(KEY_BACKSPACE) and len(state["texto"]) > 0:
            state["texto"] = state["texto"][:-1]

        if is_key_pressed(KEY_ENTER):
            if state["texto"].strip():
                cadastrar({
                    "titulo": state["texto"].strip(),
                    "autor": "",
                    "editora": "",
                    "ano": 0
                })
            state["digitando"]= False
            state["texto"] = ""

        # ESC cancela
        if is_key_pressed(KEY_ESCAPE):
            state["digitando"] = False
            state["texto"] = ""

def draw_cadastro_raylib(state):
    draw_rectangle_rec(state["create_Rec"], GREEN)
    draw_text("Criar", int(state["create_Rec"].x), int(state["create_Rec"].y), 30, WHITE)
    if state["digitando"]:
        draw_text("Digite um nome (ENTER confirma / ESC cancela):", 200, 250, 20, BLACK)
        draw_rectangle(200, 280, 400, 40, RAYWHITE)
        draw_rectangle_lines(200, 280, 400, 40, BLACK)
        draw_text(state["texto"], 210, 290, 20, BLACK)
        # cursor piscando (opcional)
        if int(get_time() * 2) % 2 == 0:
            cursor_x = 210 + measure_text(state["texto"], 20)
            draw_text("|", cursor_x, 290, 20, BLACK)
