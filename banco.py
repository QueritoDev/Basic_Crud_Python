import json
ARQUIVO = "dados.json"

def _carregar():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arq:
            return json.load(arq)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def listar():
    return _carregar()


def _salvar(livros):
    with open (ARQUIVO, "w", encoding="utf-8") as arq:
        json.dump(livros, arq, ensure_ascii=False, indent=4)

def cadastrar(livro):
    livros = _carregar()
    livros.append(livro)
    _salvar(livros)

def deletar(indice):
    livros = _carregar()
    if 0 <= indice < len(livros):
        removido = livros.pop(indice)
        _salvar(livros)
        return removido
    return None
