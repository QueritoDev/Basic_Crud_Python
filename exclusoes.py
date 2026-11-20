import cadastro

def deletar():
    livros = _carregar()
    if 0 <= indice < len(livros):
        removido = livros.pop(indice)
        _salvar(livros)
        return removido
    return None
