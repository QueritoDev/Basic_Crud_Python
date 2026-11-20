ARQUIVO = "dados.json"

def _carregar():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arq:
            return json.load(arq)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

def _salvar(livros):
    with open (ARQUIVO, "w", encoding="utf-8") as arq:
        json.dump(livros, arq, ensure_ascii=False, indent=4)

def cadastrar(elemento):
    livros = _retornaJson()
    livros.append(livro)
    _salvar(livros)


