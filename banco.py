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

def update(indice:int, info:dict):
    # abre o arquivo e guarda os dados em uma variável
    with open(ARQUIVO, "r", encoding="utf-8") as arqv:
        dados = json.load(arqv)

    # Troca os dados de acordo com o dicionario passado como parametro
    for chave, valor in info.items():
        dados[indice][chave] = info.get(chave, valor)

        if chave == "ano":
            dados[indice][chave] = int(info.get(chave, valor))

    # Salva os dados atualizados no arquivo
    with open(ARQUIVO, "w", encoding="utf-8") as arqv:
        json.dump(dados, arqv, ensure_ascii=False, indent=4)