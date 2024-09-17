def calcular_calorias(objetivo, peso):
    """
    Calcula a quantidade ideal de macronutrientes e calorias com base no objetivo e no peso.
    
    param objetivo: O objetivo do usuário (1 - Perder peso, 2 - Manter o peso, 3 - Ganhar peso)
    param peso: O peso do usuário em kg
    """
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

def imc(altura, peso):
    """
    Calcula o IMC (Índice de Massa Corporal) e retorna a classificação.
    
    param altura: Altura do usuário em metros
    param peso: Peso do usuário em kg
    return: Mensagem com a classificação do IMC
    """
    imc = peso / (altura * altura)
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
    else:
        return f"Seu IMC é: {imc:.2f}. Você está com obesidade grau 3."
