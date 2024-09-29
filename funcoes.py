import os
import json
from login import get_nome_usuario_logado, carregar_usuarios, salvar_usuarios
from pontuacoes import saber_pontos, descontar_pontos
from imprimir import print_premios

def altura():
    while True:
        try:
            valor_altura = float(input("Digite a sua altura em metros: "))
            if 1.2 <= valor_altura <= 2.7:
                return valor_altura
            else:
                print("\nAltura inválida. Por favor, digite um valor entre 1.2 e 2.7 metros.")
        except ValueError:
            print("\nEntrada inválida. Digite um número válido para a altura.")

def peso():
    while True:
        try:
            valor_peso = float(input("Digite o peso em kg: "))
            if 15 <= valor_peso <= 725:
                return valor_peso
            else:
                print("\nPeso inválido. Por favor, digite um valor entre 15 e 725 kg.")
        except ValueError:
            print("\nEntrada inválida. Digite um número válido para o peso.")

def validar_idade(idade):
    if idade < 10:
        print("\nVocê é muito novo para utilizar o aplicativo! Busque um profissional de saúde para informações adequadas!")
    elif idade > 85:
        print("\nA sua idade requer cuidados específicos. Busque um profissional de saúde para informações adequadas!")
    else:
        return True

def idade():
    while True:
        try:
            valor_idade = int(input("Digite a sua idade: "))
            if validar_idade(valor_idade):
                return valor_idade
        except ValueError:
            print("\nPor favor, digite um número inteiro válido para a idade.")

        escolha_saida = input("\nDeseja inserir uma nova idade (1) ou encerrar o programa (2)? ")
        if escolha_saida == '2':
            exit()
        elif escolha_saida != '1':
            print("\nOpção inválida. Por favor, digite 1 para continuar ou 2 para sair.")

def validar_frequencia(frequencia):
    if 1 <= frequencia <= 4:
        return True
    else:
        print("\nOpção inválida. Por favor, escolha um número entre 1 e 4.")
        return False

def frequencia():
    while True:
        try:
            valor_frequencia = int(input("\nCom qual frequência você pratica atividades físicas?\n"
                                         "1 - Nunca\n2 - 1 a 2 horas por semana\n"
                                         "3 - 3 a 4 horas por semana\n4 - mais de 5 horas por semana\n\n"
                                         "Digite a opção desejada: \n"))
            if validar_frequencia(valor_frequencia):
                return valor_frequencia
        except ValueError:
            print("\nPor favor, digite um número inteiro válido.\n")

def voltar_menu():
    while True:
        try:
            escolha = input("\nDeseja voltar ao menu principal (1) ou fechar o programa (2)? \n")
            if escolha == '1':
                return  
            elif escolha == '2':
                exit()
            else:
                print("\nOpção inválida. Por favor, digite 1 ou 2.")
        except ValueError:
            print("\nEntrada inválida. Por favor, digite 1 ou 2.")

def dicas_exercicios():
    while True:
        escolha = input("Você deseja receber dicas de exercícios para serem feitos na rua (1) ou em casa (2)?\n")
        if escolha == '1':
            exercicios_rua()
        elif escolha == '2':
            exercicios_casa()
        else:
            print("Opção inválida. Por favor, digite 1 ou 2.")

def exercicios_rua():
    print("\nDicas de exercícios para serem feitos na rua:\n"
          "1 - Caminhada\n"
          "2 - Corrida\n"
          "3 - Pular corda\n"
          "4 - Alongamento\n"
          "5 - Exercícios de fortalecimento muscular\n")
    voltar_menu()

def exercicios(f, idade):
    if idade > 10 and idade < 17:
        if f in (1, 2):
            print("\nSegundo a OMS, você deve praticar atividades físicas por no mínimo 1 hora por dia, 3 vezes na semana.")
        else:
            print("\nContinue assim, você está no caminho certo!")
    elif 18 <= idade < 65:
        if f in (1, 2):
            print("\nBusque alternativas para se exercitar e mantenha sua saúde em dia!")
        else:
            print("\nContinue assim, você está no caminho certo!")
    elif idade >= 65:
        print("\nPessoas com sua idade devem fazer atividades de fortalecimento muscular e equilíbrio.")
    print("\nSe desejar dicas de exercícios, acesse a opção 4 no menu principal.")

def exercicios_casa():
    print("\nDicas de exercícios para serem feitos em casa:\n"
          "1 - Alongamento\n"
          "2 - Exercícios de fortalecimento muscular\n"
          "3 - Yoga\n"
          "4 - Pilates\n"
          "5 - Dança\n")
    voltar_menu()

def salvar_imc(usuario_logado, imc):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario["nome_usuario"] == usuario_logado:
            usuario["imc_atual"] = imc
            salvar_usuarios(usuarios)
            print("Seu IMC foi atualizado!")

def lista_premios():
    print("Você possui %d pontos.\n" % saber_pontos())
    print(print_premios())

    while True:
        try:
            retirar_premio = int(input("Deseja resgatar um prêmio?\n1 - Sim\n2 - Não\n"))
            if retirar_premio in (1, 2):
                break
            else:
                print("Valor inválido, escolha entre 1 e 2.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número entre 1 e 2.")

    if retirar_premio == 1:
        processar_resgate_premio()

def processar_resgate_premio():
    os.system('clear')
    print("Você possui %d pontos.\n" % saber_pontos())
    print(print_premios())

    while True:
        try:
            escolha_premio = int(input("Digite o número do prêmio que deseja resgatar: "))
            if 1 <= escolha_premio <= 4:
                break
            else:
                print("Valor inválido, escolha entre 1 e 4.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número entre 1 e 4.")

    premios = {1: 20, 2: 35, 3: 15, 4: 50}
    print(descontar_pontos(premios[escolha_premio]))
    voltar_menu()
