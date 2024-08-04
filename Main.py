def altura():
    while True:
        try:
            valor_altura = float(input("Digite a sua altura em metros:  "))
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
            valor_frequencia = int(input("\nCom qual frequência você pratica atividades físicas?\n1 - Nunca\n2 - 1 a 2 horas por semana\n3 - 3 a 4 horas por semana\n4 - mais de 5 horas por semana\n\nDigite a opção desejada: "))
            if validar_frequencia(valor_frequencia):
                return valor_frequencia
        except ValueError:
            print("\nPor favor, digite um número inteiro válido.")

def calcular_calorias(objetivo, peso):
    if objetivo == 1:
        x, y = 2, 3
    if objetivo == 2:
        x, y = 1.5, 3
    if objetivo == 3:
        x, y = 1, 4
    proteinas = peso * x
    carboidratos = peso * y
    gorduras = peso * 1
    calorias = (proteinas * 4) + (carboidratos * 4) + (gorduras * 9)
    print(f"\nPara o seu objetivo, você deve consumir:\n{proteinas:.2f}g de proteínas\n{carboidratos:.2f}g de carboidratos\n{gorduras:.2f}g de gorduras, totalizando {calorias:.2f} calorias\n")
    
def imc(Altura, peso_valor):
    imc = peso_valor / (Altura * Altura)
    if imc < 18.5:
        return f"Seu IMC é: {imc:.2f}. Você está abaixo do peso ideal."
    elif 18.5 <= imc < 24.9:
        return f"Seu IMC é: {imc:.2f}. Você está no peso ideal."
    elif 25 <= imc < 29.9:
        return f"Seu IMC é: {imc:.2f}. Você está com sobrepeso."
    elif 30 <= imc < 34.9:  
        return f"Seu IMC é: {imc:.2f}. Você está com obesidade grau 1."
    elif 35 <= imc < 39.9:
        return f"Seu IMC é: {imc:.2f}. Você está com obesidade grau 2."
    
def menu():
    while True:
        try:
            print("\nO que você deseja fazer?\n\n1 - Deseja calcular o IMC?\n2 - Deseja saber qual nível ideal de atividade física e dicas de exercícios para melhorar a sua saúde?\n3 - Deseja saber a quantidade ideal de macronutrientes a serem ingeridos para uma alimentação equilibrada?\n4 - Deseja receber dicas de exercícios para melhorar a sua saúde?\n")
            opcao = int(input("\nDigite a opção desejada: "))
            if 1 <= opcao <= 4:
                escolha(opcao)
            else:
                print("\nOpção inválida. Por favor, digite um número entre 1 e 4.")
        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número inteiro.")

def escolha(opcao):
    if opcao == 1:
        print(imc(Altura, Peso))
        voltar_menu()
    if opcao == 2:
        exercicios(Frequencia, Idade)
        voltar_menu()
    if opcao == 3:
        macronutrientes(Peso)
        voltar_menu()
    if opcao == 4:
        dicas_exercicios()
        voltar_menu()

def macronutrientes(Peso):
        objetivo = int(input("\nDeseja saber a quantidade de macronutrientes a serem ingeridos para:\n1 - Perder peso\n2 - Manter o peso\n3 - Ganhar peso\n\n"))
        calcular_calorias(objetivo, Peso)

def exercicios(f,idade):
    if idade > 10 and idade < 17:
        if f == 1 or f == 2:
            print("\nSegundo a OMS, você deve praticar atividades físicas por no mínimo 1 hora por dia,  3 vezes na semana, busque alternativas para se exercitar, como esportes ou atividades em grupo, além de brincadeiras ao ar livre e que te agradem. Uma boa dica é tentar praticar atividades em grupo!")
        else:
            print("\nSegundo a OMS, você deve praticar atividades físicas por no mínimo 1 hora por dia,  3 vezes na semana, continue assim, você está no caminho certo!")
    if idade > 18 and idade < 65:
        if f == 1 or f == 2:
            print("\nSegundo a OMS, você deve praticar atividades físicas entre 150 e 300 minutos de atividades moderadas ou 75 a 150 minutos de atividades intensas por semana. Busque alternativas para se exercitar e receba mais dicas neste programa para manter sua saúde em dia!")
        else:
            print("\nSegundo a OMS, você deve praticar atividades físicas entre 150 e 300 minutos de atividades moderadas ou 75 a 150 minutos de atividades intensas por semana. Continue assim, você está no caminho certo!")
        
    elif idade > 65: 
         print("\nÉ recomendado que pessoas na sua idade façam atividades de fortalecimento muscular e equilíbrio, além das atividades aeróbicas. Busque um profissional de saúde para mais informações, e receba dicas de atividades neste programa!")
    print("\nSe desejar dicas de exercícios para melhorar a sua saúde, acesse a opção 4 no menu principal")

def voltar_menu():
    while True:
        try:
            escolha = input("\nDeseja voltar ao menu principal (1) ou fechar o programa (2)?: ")
            if escolha == '1':
                menu()
            elif escolha == '2':
                exit()
            else:
                print("\nOpção inválida. Por favor, digite 1 ou 2.")
        except ValueError:
            print("\nEntrada inválida. Por favor, digite 1 ou 2.")

def dicas_exercicios():
    while True:
        escolha = input("Você deseja receber dicas de exercicios para serem feitos na rua (1) ou em casa (2)?\n")

        if escolha == '1':
            exercicios_rua()
        elif escolha == '2':
            exercicios_casa()
        else:
            print("Opção inválida. Por favor, digite 1, 2.")

def exercicios_rua():
    print("\nDicas de exercícios para serem feitos na rua:\n1 - Caminhada\n2 - Corrida\n3 - Pular corda\n4 - Alongamento\n5 - Exercícios de fortalecimento muscular\n")
def exercicios_casa():
    print("\nDicas de exercícios para serem feitos em casa:\n1 - Alongamento\n2 - Exercícios de fortalecimento muscular\n3 - Yoga\n4 - Pilates\n5 - Dança\n")

Altura = altura()
Peso = peso()
Idade = idade()
Frequencia = frequencia()
menu()

