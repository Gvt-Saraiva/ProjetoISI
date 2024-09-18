from funcoes import altura, peso, idade, frequencia, voltar_menu, dicas_exercicios
from calculos import imc, calcular_calorias
from login import registrar_usuario, login_usuario
from imprimir import imprimir
import time 
import os

def menu():
    """
    Exibe o menu principal e solicita a escolha do usuário.
    """
    os.system('clear')
    while True:
        try:
            print("\nO que você deseja fazer?\n\n"
                  "1 - Deseja calcular o IMC?\n"
                  "2 - Deseja saber qual nível ideal de atividade física e dicas de exercícios para melhorar a sua saúde?\n"
                  "3 - Deseja saber a quantidade ideal de macronutrientes a serem ingeridos para uma alimentação equilibrada?\n"
                  "4 - Deseja receber dicas de exercícios para melhorar a sua saúde?\n")
            opcao = int(input("\nDigite a opção desejada: "))
            if 1 <= opcao <= 4:
                escolha(opcao)
            else:
                print("\nOpção inválida. Por favor, digite um número entre 1 e 4.")
        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número inteiro.")

def escolha(opcao):
    
    """
    Executa a ação apropriada com base na opção escolhida pelo usuário.
    
    param opcao: Opção escolhida pelo usuário (1 a 4)
    """
    if opcao == 1:
        print(imc(altura(), peso()))
        voltar_menu()
    elif opcao == 2:
        exercicios(frequencia(), idade())
        voltar_menu()
    elif opcao == 3:
        objetivo = int(input("\nDeseja saber a quantidade de macronutrientes a serem ingeridos para:\n"
                             "1 - Perder peso\n"
                             "2 - Manter o peso\n"
                             "3 - Ganhar peso\n\n"))
        print(calcular_calorias(objetivo, peso()))
        voltar_menu()
    elif opcao == 4:
        dicas_exercicios()

def exercicios(f, idade):
    """
    Fornece dicas de exercícios baseadas na frequência de atividade física e na idade do usuário.
    
    param f: Frequência de atividade física do usuário (1 a 4)
    param idade: Idade do usuário
    """
    if idade > 10 and idade < 17:
        if f in (1, 2):
            print("\nSegundo a OMS, você deve praticar atividades físicas por no mínimo 1 hora por dia, 3 vezes na semana. Busque alternativas para se exercitar, como esportes ou atividades em grupo, além de brincadeiras ao ar livre e que te agradem.")
        else:
            print("\nSegundo a OMS, você deve praticar atividades físicas por no mínimo 1 hora por dia, 3 vezes na semana. Continue assim, você está no caminho certo!")
    elif 18 <= idade < 65:
        if f in (1, 2):
            print("\nSegundo a OMS, você deve praticar atividades físicas entre 150 e 300 minutos de atividades moderadas ou 75 a 150 minutos de atividades intensas por semana. Busque alternativas para se exercitar e receba mais dicas neste programa para manter sua saúde em dia!")
        else:
            print("\nSegundo a OMS, você deve praticar atividades físicas entre 150 e 300 minutos de atividades moderadas ou 75 a 150 minutos de atividades intensas por semana. Continue assim, você está no caminho certo!")
    elif idade >= 65:
        print("\nÉ recomendado que pessoas na sua idade façam atividades de fortalecimento muscular e equilíbrio, além das atividades aeróbicas. Busque um profissional de saúde para mais informações, e receba dicas de atividades neste programa!")
    print("\nSe desejar dicas de exercícios para melhorar a sua saúde, acesse a opção 4 no menu principal.")

def main():
    """
    Função principal que gerencia o fluxo do programa, incluindo login e registro.
    """
    while True:
        print("1 - Registrar\n2 - Login\n3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar_usuario()
        elif opcao == '2':
            if login_usuario():
                menu()
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, digite 1, 2 ou 3.")

if __name__ == "__main__":
    print(imprimir())
    time.sleep(2)
    main()


