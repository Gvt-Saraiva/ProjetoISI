from funcoes import salvar_imc
from login import get_nome_usuario_logado, get_imc_atual, get_objetivo
from pontuacoes import somar_pontos

def calcular_calorias(objetivo, peso):
    if objetivo == 1:
        x, y = 2, 3
    elif objetivo == 2:
        x, y = 1.5, 3
    elif objetivo == 3:
        x, y = 1, 4
    else:
        raise ValueError("Objetivo inválido. Deve ser 1, 2 ou 3.")
    
    proteinas = peso * x
    carboidratos = peso * y
    gorduras = peso * 1
    calorias = (proteinas * 4) + (carboidratos * 4) + (gorduras * 9)
    return (f"\nPara o seu objetivo, você deve consumir:\n"
            f"{proteinas:.2f}g de proteínas\n"
            f"{carboidratos:.2f}g de carboidratos\n"
            f"{gorduras:.2f}g de gorduras, totalizando {calorias:.2f} calorias\n")

def pontuacao(diferenca_imc, objetivo):
    """
    Calcula a pontuação do usuário com base na diferença do IMC e no objetivo escolhido.
    
    objetivo:
    1 - Aumentar o IMC
    2 - Diminuir o IMC
    3 - Manter o IMC
    """
    if objetivo == 1:
        if diferenca_imc > 0:
            return 10
        elif -0.3 <= diferenca_imc <= 0.3:
            return 5
        else:
            return 0
    elif objetivo == 2: 
        if diferenca_imc < 0:
            return 10
        elif -0.3 <= diferenca_imc <= 0.3:
            return 5
        else:
            return 0
    elif objetivo == 3: 
        if -0.3 <= diferenca_imc <= 0.3:
            return 10
        else:
            return 0

def imc(altura, peso):
    imc = peso / (altura * altura)
    if imc < 18.5:
        print(f"Seu IMC é: {imc:.2f}. Você está abaixo do peso ideal.")
    elif 18.5 <= imc < 24.9:
        print(f"Seu IMC é: {imc:.2f}. Você está no peso ideal.")
    elif 25 <= imc < 29.9:
        print(f"Seu IMC é: {imc:.2f}. Você está com sobrepeso.")
    elif 30 <= imc < 34.9:  
        print(f"Seu IMC é: {imc:.2f}. Você está com obesidade grau 1.")
    elif 35 <= imc < 39.9:
        print(f"Seu IMC é: {imc:.2f}. Você está com obesidade grau 2.")
    else:
        print(f"Seu IMC é: {imc:.2f}. Você está com obesidade grau 3.")

    while True:
        escolha_salvar = input("Deseja salvar o resultado do seu IMC?\n1 - Sim\n2 - Não\n")
        if escolha_salvar == '1' or escolha_salvar == '2':
            break
        else:
            print("Valor inválido, escolha entre 1 e 2.")

    if escolha_salvar == '1':
        imc_anterior = get_imc_atual()
        if imc_anterior is None:
            salvar_imc(get_nome_usuario_logado(), imc)
            print("Seu IMC foi salvo! Parabéns por se cuidar!") 
        else:
            diferenca_imc = imc - imc_anterior
            pontos = pontuacao(diferenca_imc, 1)
            
            somar_pontos(pontos)
            salvar_imc(get_nome_usuario_logado(), imc)
            
            print(f"Você ganhou {pontos} pontos.")

