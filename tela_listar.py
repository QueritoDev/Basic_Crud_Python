from raylibpy import *
import banco

def criar_estado():
    return {
        "pagina": 0,
        "livros_por_pagina": 6,
        "item_selecionado": None, # Guarda o indice do livro no JSON
        "voltar_Rec": Rectangle(50, 380, 120, 40),
        "ant_Rec": Rectangle(300, 380, 100, 40),
        "prox_Rec": Rectangle(420, 380, 100, 40),
        "remover_Rec": Rectangle(650, 380, 120, 40)
    }

def update_listar(state):
    mouse_pos = get_mouse_position()
    livros = banco.listar()
    voltar = False
    if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
        if check_collision_point_rec(mouse_pos, state["voltar_Rec"]):
            return True

        # Navegacao de Paginas
        if check_collision_point_rec(mouse_pos, state["ant_Rec"]) and state["pagina"] > 0:
            state["pagina"] -= 1
            state["item_selecionado"] = None # Limpa a seleção ao trocar de página

        if check_collision_point_rec(mouse_pos, state["prox_Rec"]):
            # Só avança se ainda tiver livros na próxima página
            if (state["pagina"] + 1) * state["livros_por_pagina"] < len(livros):
                state["pagina"] += 1
                state["item_selecionado"] = None


        # Calcula quais livros estão na página atual
        inicio = state["pagina"] * state["livros_por_pagina"]
        livros_na_tela = livros[inicio : inicio + state["livros_por_pagina"]]

        for i in range(len(livros_na_tela)):
            rect_livro = Rectangle(100, 80 + (i * 45), 600, 40) # Retangulo de fundo de cada livro

            if check_collision_point_rec(mouse_pos, rect_livro):
                # O índice real no JSON é a posição na tela + o pulo das páginas anteriores
                state["item_selecionado"] = i + inicio

        # remover item selecionado
        if state["item_selecionado"] is not None:
            if check_collision_point_rec(mouse_pos, state["remover_Rec"]):
                banco.deletar(state["item_selecionado"])
                state["item_selecionado"] = None

                # volta uma pagina se ficar vazia
                if state["pagina"] > 0 and len(banco.listar()) <= (state["pagina"] * state["livros_por_pagina"]):
                    state["pagina"] -= 1

    return False

def draw_listar(state):
    livros = banco.listar()
    inicio = state["pagina"] * state["livros_por_pagina"]
    livros_na_tela = livros[inicio : inicio + state["livros_por_pagina"]]

    draw_text("LISTA DE LIVROS", 300, 20, 30, DARKGRAY)

    if not livros:
        draw_text("Nenhum livro cadastrado.", 300, 200, 20, GRAY)
    else:
        for i, livro in enumerate(livros_na_tela):
            index_real = i + inicio
            rect_livro = Rectangle(100, 80 + (i * 45), 600, 40)

            # Se o livro está selecionado, fica verde, senão fica cinza claro
            cor = GREEN if state["item_selecionado"] == index_real else LIGHTGRAY
            draw_rectangle_rec(rect_livro, cor)
            draw_rectangle_lines(int(rect_livro.x), int(rect_livro.y), int(rect_livro.width), int(rect_livro.height), DARKGRAY)

            # Formata o texto para ficar bonito na tela
            texto = f"{livro['titulo']} - {livro['autor']} ({livro['ano']})"
            draw_text(texto, int(rect_livro.x) + 10, int(rect_livro.y) + 10, 20, BLACK)

    draw_rectangle_rec(state["voltar_Rec"], RED)
    draw_text("Voltar", int(state["voltar_Rec"].x) + 15, int(state["voltar_Rec"].y) + 10, 20, WHITE)

    draw_rectangle_rec(state["ant_Rec"], ORANGE)
    draw_text("< Ant", int(state["ant_Rec"].x) + 15, int(state["ant_Rec"].y) + 10, 20, WHITE)

    draw_rectangle_rec(state["prox_Rec"], ORANGE)
    draw_text("Prox >", int(state["prox_Rec"].x) + 10, int(state["prox_Rec"].y) + 10, 20, WHITE)

    # desenha o botão remover se tiver um item selecionado
    if state["item_selecionado"] is not None:
        draw_rectangle_rec(state["remover_Rec"], RED)
        draw_text("Remover", int(state["remover_Rec"].x) + 15, int(state["remover_Rec"].y) + 10, 20, WHITE)
