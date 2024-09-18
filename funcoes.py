import os

def altura():
    """
    Solicita ao usuário que informe sua altura em metros e valida o valor informado.
    A altura deve estar entre 1.2 e 2.7 metros.
    """

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
    """
    Solicita ao usuário que informe seu peso em kg e valida o valor informado.
    O peso deve estar entre 15 e 725 kg.
    """
    
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
    """
    Valida a idade do usuário e fornece recomendações baseadas na faixa etária.
    
    param idade: Idade do usuário
    return: True se a idade estiver na faixa válida, caso contrário, imprime uma mensagem e retorna False.
    """
  
    if idade < 10:
        print("\nVocê é muito novo para utilizar o aplicativo! Busque um profissional de saúde para informações adequadas!")
    elif idade > 85:
        print("\nA sua idade requer cuidados específicos. Busque um profissional de saúde para informações adequadas!")
    else:
        return True

def idade():
    """
    Solicita ao usuário que informe sua idade e valida o valor informado.
    Oferece a opção de inserir uma nova idade ou encerrar o programa.
    """

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
    """
    Valida a frequência de atividades físicas do usuário.
    
    frequencia: Frequência de atividades físicas do usuário
    return: True se a frequência estiver entre 1 e 4, caso contrário, imprime uma mensagem e retorna False.
    """
    
    if 1 <= frequencia <= 4:
        return True
    else:
        print("\nOpção inválida. Por favor, escolha um número entre 1 e 4.")
        return False

def frequencia():
    """
    Solicita ao usuário que informe com que frequência pratica atividades físicas e valida o valor informado.
    """
   
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
    """
    Oferece ao usuário a opção de voltar ao menu principal ou encerrar o programa.
    """
    
    while True:
        try:
            escolha = input("\nDeseja voltar ao menu principal (1) ou fechar o programa (2)? \n")
            if escolha == '1':
                return  # Retorna ao menu principal
            elif escolha == '2':
                exit()
            else:
                print("\nOpção inválida. Por favor, digite 1 ou 2.")
        except ValueError:
            print("\nEntrada inválida. Por favor, digite 1 ou 2.")

def dicas_exercicios():
    """
    Oferece ao usuário a opção de receber dicas de exercícios para serem feitos na rua ou em casa.
    """
    
    while True:
        escolha = input("Você deseja receber dicas de exercícios para serem feitos na rua (1) ou em casa (2)?\n")
        if escolha == '1':
            exercicios_rua()
        elif escolha == '2':
            exercicios_casa()
        else:
            print("Opção inválida. Por favor, digite 1 ou 2.")

def exercicios_rua():
    """
    Fornece dicas de exercícios que podem ser realizados ao ar livre.
    """
   
    print("\nDicas de exercícios para serem feitos na rua:\n"
          "1 - Caminhada\n"
          "2 - Corrida\n"
          "3 - Pular corda\n"
          "4 - Alongamento\n"
          "5 - Exercícios de fortalecimento muscular\n")
    voltar_menu()

def exercicios_casa():
    """
    Fornece dicas de exercícios que podem ser realizados em casa.
    """
   
    print("\nDicas de exercícios para serem feitos em casa:\n"
          "1 - Alongamento\n"
          "2 - Exercícios de fortalecimento muscular\n"
          "3 - Yoga\n"
          "4 - Pilates\n"
          "5 - Dança\n")
    voltar_menu()
