## Crud Basic - QueritoDEV

def cadastrar(elemento):
    arq = open("dados.txt", "a")
    arq.write("%s\n" %elemento)
    arq.close()

def Input():
    return input("Digite um nome: ")

def Listar():
    #tô colocando um tratamento de erros aqui
    try:
        arq = open("dados.txt", "r")
        for linha in arq:
            print(linha)
        arq.close()
    except:
        print("Arquivo não encontrado")

while True:
    print("-------MENU--------")
    print("[1] Cadastrar")
    print("[2] Listar")
    print("[3] Sair")
    op = int(input(">>>"))

    if op == 3:
        break;
    elif op == 1:
        elemento = Input()
        cadastrar(elemento)
    elif op == 2:
        Listar()
    else:
        print("Opcao Invalida")

    
