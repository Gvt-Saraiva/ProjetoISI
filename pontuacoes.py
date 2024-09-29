import json
from login import carregar_usuarios, get_nome_usuario_logado, salvar_usuarios
import random

def saber_pontos():
    """
    Retorna a pontuação do usuário logado. Se não houver pontuação, retorna 0.
    """
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario["nome_usuario"] == get_nome_usuario_logado():
            # Se o campo "pontuacao" não existir ou for None, retorne 0
            return int(usuario.get("pontuacao", 0))
    return 0

def somar_pontos(pontos):
    """
    Soma os pontos ao usuário logado. Se a pontuação for None, inicializa como 0.
    """
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario["nome_usuario"] == get_nome_usuario_logado():
            # Pegue a pontuação atual ou 0 se for None
            pontos_usuario = int(usuario.get("pontuacao", 0))
            pontos_usuario += pontos
            usuario["pontuacao"] = pontos_usuario  # Atualiza a pontuação do usuário
            salvar_usuarios(usuarios)
            return 'Pontos somados com sucesso!'
    return 'Usuário não encontrado.'

def descontar_pontos(custo):
    """
    Desconta pontos do usuário logado, se houver pontuação suficiente.
    """
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario["nome_usuario"] == get_nome_usuario_logado():
            # Certifique-se de que o campo "pontuacao" existe e é um inteiro
            pontuacao_atual = int(usuario.get("pontuacao", 0))
            
            if pontuacao_atual < custo:
                return 'Pontuação insuficiente.'
            else:
                usuario["pontuacao"] = pontuacao_atual - custo
                salvar_usuarios(usuarios)
                return 'Operação efetuada com sucesso. Código de retirada: %d' % random.randint(1000, 9999)
    return 'Usuário não encontrado.'
