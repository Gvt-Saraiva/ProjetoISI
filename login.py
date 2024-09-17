import json
import os

ARQUIVO_DADOS = os.path.join("dados", "usuarios.json")

def carregar_usuarios():
    """
    Carrega os dados dos usuários do arquivo JSON.
    """
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r') as arquivo:
            return json.load(arquivo)
    return []

def salvar_usuarios(usuarios_lista):
    """
    Salva os dados dos usuários no arquivo JSON.
    """

    with open(ARQUIVO_DADOS, 'w') as arquivo:
        json.dump(usuarios_lista, arquivo, indent=4)

def registrar_usuario():
    """
    Registra um novo usuário, solicitando nome de usuário e senha.
    """
    try:
        usuarios = carregar_usuarios()
    except:
        usuarios = []

    while True:
        nome_usuario = input("Digite o nome de usuário: ")
        if nome_usuario in usuarios:
            print("Nome de usuário já existe. Tente outro.")
        else:
            break
    
    senha = input("Digite a senha: ")
    
    user = {
        nome_usuario: senha
    }

    usuarios.append(user)
    salvar_usuarios(usuarios)
    print("Usuário registrado com sucesso!")

def login_usuario():
    """
    Realiza o login do usuário, solicitando nome de usuário e senha.
    """
    usuarios = carregar_usuarios()
    print(usuarios)
    
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    for i in usuarios:
        for nome, senha in i.items():
            if nome_usuario == nome and senha == senha:
                print("Login bem-sucedido!")
                return True

    print("Nome de usuário ou senha incorretos.")
    return False