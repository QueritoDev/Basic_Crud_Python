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
        "clicouCadastrar": False,
        "campo_ativo": None,
        "campos": {
            "titulo": "",
            "autor": "",
            "editora": "",
            "ano": ""
        },
        "save_Rec": Rectangle(600, 380, 120, 40),
        "cadastrar_Rec": Rectangle(300, 380, 120, 40),
        "rects": {
            "titulo": Rectangle(200, 100, 400, 40),
            "autor": Rectangle(200, 170, 400, 40),
            "editora": Rectangle(200, 240, 400, 40),
            "ano": Rectangle(200, 310, 400, 40)
        }
    }

def update_cadastro_raylib(state):
    # UPDATE

    mouse_pos = get_mouse_position()

    # Verifica se clicou em algum campo de texto
    if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
        state["campo_ativo"] = None # reseta por padrão
        for nome, rect in state["rects"].items():
            if check_collision_point_rec(mouse_pos, rect):
                state["campo_ativo"] = nome
                break # achou o campo, para o loop

    if is_mouse_button_pressed(MOUSE_BUTTON_LEFT) and check_collision_point_rec(mouse_pos, state["save_Rec"]):
        if state["campos"]["titulo"].strip(): # Só cadastra se tiver título
            # Transforma ano em número (ou 0 se estiver vazio)
            ano_str = state["campos"]["ano"].strip()
            ano_num = int(ano_str) if ano_str.isdigit() else 0

            cadastrar({
                "titulo": state["campos"]["titulo"].strip(),
                "autor": state["campos"]["autor"].strip(),
                "editora": state["campos"]["editora"].strip(),
                "ano": ano_num
            })

            # Limpa o formulário após cadastrar
            state["campos"] = {"titulo": "", "autor": "", "editora": "", "ano": ""}

        state["campo_ativo"] = None

    if state["campo_ativo"] is not None:
        print(state["campo_ativo"])
        campo = state["campo_ativo"]
        char = get_char_pressed()

        if char > 0:
            if campo == "ano" and not chr(char).isdigit():
                pass # ignora letras
            else:
                state["campos"][campo] += chr(char)

        if is_key_pressed(KEY_BACKSPACE) and len(state["campos"][campo]) > 0:
            state["campos"][campo] = state["campos"][campo][:-1]

        if is_key_pressed(KEY_ENTER):
            state["campo_ativo"] = None

        # ESC cancela
        if is_key_pressed(KEY_ESCAPE):
            state["campo_ativo"] = None

def draw_cadastro_raylib(state):
    # Desenha os campos
    for nome, rect in state["rects"].items():
        # Desenha o texto de ajuda (Título:, Autor:, etc)
        draw_text(nome.capitalize() + ":", int(rect.x), int(rect.y) - 25, 20, BLACK)

        # Muda a cor do fundo se o campo estiver ativo
        cor_fundo = WHITE if state["campo_ativo"] == nome else LIGHTGRAY
        draw_rectangle_rec(rect, cor_fundo)
        draw_rectangle_lines(int(rect.x), int(rect.y), int(rect.width), int(rect.height), BLACK)

        # Desenha o texto digitado dentro do campo
        draw_text(state["campos"][nome], int(rect.x) + 10, int(rect.y) + 10, 20, BLACK)

        # Desenha o cursor piscando no campo ativo
        if state["campo_ativo"] == nome and int(get_time() * 2) % 2 == 0:
            cursor_x = int(rect.x) + 10 + measure_text(state["campos"][nome], 20)
            draw_text("|", cursor_x, int(rect.y) + 10, 20, BLACK)

    # Desenha o botão Cadastrar
    draw_rectangle_rec(state["save_Rec"], GREEN)
    draw_text("Salvar", int(state["save_Rec"].x) + 10, int(state["save_Rec"].y) + 10, 20, WHITE)

def update_crud(state):
    mouse_pos = get_mouse_position()

    if(is_mouse_button_pressed(MOUSE_BUTTON_LEFT) and check_collision_point_rec(mouse_pos, state["cadastrar_Rec"])):
        state["clicouCadastrar"] = True

def draw_crud(state):
    if(state["clicouCadastrar"]==True):
        draw_cadastro_raylib(state)
        return

    draw_rectangle_rec(state["cadastrar_Rec"], GREEN)
    draw_text("Cadastrar", int(state["cadastrar_Rec"].x) + 10, int(state["cadastrar_Rec"].y) + 10, 20, WHITE)


