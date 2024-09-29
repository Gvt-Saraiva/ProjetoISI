import json
import os

ARQUIVO_DADOS = os.path.join("dados", "usuarios.json")

def imprimir_cadastro():
    return "=== Tela de Cadastro ==="

def carregar_usuarios():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding="utf-8") as arquivo:
            return json.load(arquivo)

def salvar_usuarios(usuarios_list):
    with open(ARQUIVO_DADOS, 'w', encoding="utf-8") as arquivo:
        json.dump(usuarios_list, arquivo, indent=1)

def registrar_usuario():
    print(imprimir_cadastro())
    usuarios = carregar_usuarios()

    while True:
        nome_usuario = input("Digite o nome de usuário: ").strip()
        if any(usuario['nome_usuario'] == nome_usuario for usuario in usuarios):
            print("Nome de usuário já existe. Tente outro.")
        else:
            break   
    senha = input("Digite a senha: ").strip()
    while True:
        objetivo_atual = input("Qual seu objetivo?\n1 - Perder peso\n2 - ganhar peso\n3 - manter peso\n")
        if(int(objetivo_atual) < 1 or int(objetivo_atual) > 3):
            print("Opção inválida. Por favor, digite 1, 2 ou 3.")
        else:
            break
    imc_atual = None
    pontuacao = 0.0
    usuarios.append({
        "nome_usuario": nome_usuario,
        "senha": senha,
        "imc_atual": imc_atual,
        "objetivo": objetivo_atual,
        "pontuacao": pontuacao
    })

    salvar_usuarios(usuarios)
    print("Usuário registrado com sucesso!")

def login_usuario():
    usuarios = carregar_usuarios()
    
    nome_usuario = input("Digite o nome de usuário: ").strip()
    senha = input("Digite a senha: ").strip()
    
    for usuario in usuarios:
        if usuario["nome_usuario"] == nome_usuario and usuario["senha"] == senha:
            print("Login bem-sucedido!")
            global nome_usuario_logado
            nome_usuario_logado = nome_usuario
            return True
    
    print("Usuário ou senha inválidos. Tente novamente.")
    return False

def atualizar_senha():
    usuarios = carregar_usuarios()
    
    nome_usuario = input("Digite o nome de usuário: ").strip()
    senha_atual = input("Digite a senha atual: ").strip()
    
    for usuario in usuarios:
        if usuario["nome_usuario"] == nome_usuario and usuario["senha"] == senha_atual:
            nova_senha = input("Digite a nova senha: ").strip()
            usuario["senha"] = nova_senha
            salvar_usuarios(usuarios)
            print("Senha atualizada com sucesso!")
            return
    
    print("Usuário ou senha inválidos. Tente novamente.")

def deletar_conta():
    usuarios = carregar_usuarios()
    
    nome_usuario = input("Digite o nome de usuário: ").strip()
    senha = input("Digite a senha: ").strip()
    
    for usuario in usuarios:
        if usuario["nome_usuario"] == nome_usuario and usuario["senha"] == senha:
            usuarios.remove(usuario) 
            salvar_usuarios(usuarios)
            print("Conta deletada com sucesso!")
            return
    
    print("Usuário ou senha inválidos. Tente novamente.")

def get_nome_usuario_logado():
    try:
        return nome_usuario_logado
    except NameError:
        print("Nenhum usuário logado.")
        return None
    
def get_imc_atual():
    usuarios = carregar_usuarios()
    usuario_logado = get_nome_usuario_logado()

    for usuario in usuarios:
        if usuario["nome_usuario"] == usuario_logado:
            return usuario.get("imc_atual", 0)
        
def get_objetivo():
    usuarios = carregar_usuarios()
    usuario_logado = get_nome_usuario_logado()

    for usuario in usuarios:
        if usuario["nome_usuario"] == usuario_logado:
            return usuario.get("objetivo")