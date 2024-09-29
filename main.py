from funcoes import altura, peso, idade, frequencia, voltar_menu, dicas_exercicios, exercicios, lista_premios
from calculos import imc, calcular_calorias
from login import registrar_usuario, login_usuario, deletar_conta, atualizar_senha
from imprimir import imprimir, print_premios
import time
import os

def menu():
  
    os.system('clear')
    while True:
        try:
            print("\nO que você deseja fazer?\n\n"
                  "1 - Deseja calcular o IMC?\n"
                  "2 - Deseja saber qual nível ideal de atividade física e dicas de exercícios para melhorar a sua saúde?\n"
                  "3 - Deseja saber a quantidade ideal de macronutrientes a serem ingeridos para uma alimentação equilibrada?\n"
                  "4 - Deseja receber dicas de exercícios para melhorar a sua saúde?\n"
                  "5 - Deseja consultar seus pontos e ver os prêmios disponíveis?\n"
                  "6 - Sair\n")

            opcao = int(input("\nDigite a opção desejada: "))
            if 1 <= opcao <= 6:
                escolha(opcao)
            else:
                print("\nOpção inválida. Por favor, digite um número entre 1 e 6.")
        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número inteiro.")

def escolha(opcao):
    if opcao == 1:
            os.system('clear')
            print(imc(altura(), peso()))
            voltar_menu()
    elif opcao == 2:
            os.system('clear')
            exercicios(frequencia(), idade())
            voltar_menu()
    elif opcao == 3:
        os.system('clear')
        while True:
            try:
                objetivo = int(input("\nDeseja saber a quantidade de macronutrientes a serem ingeridos para:\n"
                                         "1 - Perder peso\n"
                                         "2 - Manter o peso\n"
                                         "3 - Ganhar peso\n\n"))
                if objetivo > 3 or objetivo < 1:
                        print("Valor inválido, escolha entre 1 e 3")
                else:
                        break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número entre 1 e 3.")
        print(calcular_calorias(objetivo, peso()))
        voltar_menu()
    elif opcao == 4:
        os.system('clear')
        dicas_exercicios()
    elif opcao == 5:
        os.system('clear')
        lista_premios()
    elif opcao == 6:
         os.system('clear')
         exit()

def main():
    """
    Função principal que gerencia o fluxo do programa, incluindo login e registro.
    """
    while True:
        time.sleep(1)
        os.system('clear')
        print("1 - Registrar\n2 - Login\n3 - Atualizar senha\n4 - Deletar conta\n5 - sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar_usuario()
        elif opcao == '2':
            if login_usuario(): 
                menu()
        elif opcao == '3':
            atualizar_senha()
        elif opcao == '4':
            deletar_conta()
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, digite de 1 a 6.")

if __name__ == "__main__":
    print(imprimir())
    time.sleep(1)
    main()


