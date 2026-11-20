## Crud Basic - QueritoDEV
import json

def listar():
    #tô colocando um tratamento de erros aqui
    try:
        arq = open("dados.txt", "r")
        for linha in arq:
            print(linha)
        arq.close()
    except:
        print("Arquivo não encontrado")

def remover():
    try:
        arq = open("dados.txt", "r")
        linhas = arq.readlines()
        arq.close()

        #verificando se o arquivo está vazio
        if not linhas:
            print("Arquivo vazio")
            return

        #faz uma varredura na lista de livros e mostra o índice de cada um
        print("-- Nomes Cadastrados --")
        for i, linha in enumerate(linhas):
            print(f"[{i}] {linha.strip()}")

        print("-------------------------")

        #variável que vai guardar a escolha do usuário
        escolha = int(input("Digite o índice do nome que deseja remover: "))

        #verifica se o índice é válido (maior que zero) e se é menor que o tamanho da lista de livros
        if 0 <= escolha < len(linhas):
            #remove o elemento da lista de livros e guarda o nome removido em uma variável (para mostrar depois)
            removido = linhas.pop(escolha)

            #reescreve o arquivo com os nomes restantes
            arq = open("dados.txt", "w")
            for linha in linhas:
                arq.write(linha)
            arq.close()

            print(f"Nome '{removido.strip()}' removido com sucesso.")
        else:
            print("Índice inválido.")

    #aqui tem dois tratamentos de erro, um para caso o arquivo não exista e outro para caso o usuário digite algo que não seja um número inteiro
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
    


"""
while True:
    print("-------MENU--------")
    print("[1] Cadastrar")
    print("[2] Listar")
    print("[3] Remover")
    print("[4] Sair")
    op = int(input(">>>"))

    if op == 4:
        break;
    elif op == 1:
        elemento = Input()
        cadastrar(elemento)
    elif op == 2:
        Listar()
    elif op == 3:
        Remover()
    else:
        print("Opcao Invalida")
"""
