# PISIFitness

Este é um programa de saúde e bem-estar que permite ao usuário fazer login e escolher entre várias funcionalidades para melhorar seu estilo de vida. Utilizando um arquivo JSON para autenticação e armazenamento de dados, o programa oferece as seguintes opções:

1. Calcular o Índice de Massa Corporal (IMC)
2. Ver a frequência ideal de atividade física
3. Determinar a quantidade ideal de macronutrientes
4. Receber dicas para melhorar a saúde

## Funcionalidades

### 1. Calcular o IMC
O programa permite que o usuário insira seu peso e altura para calcular o Índice de Massa Corporal (IMC), fornecendo uma indicação geral do estado de saúde.

### 2. Frequência Ideal de Atividade Física
Com base nas informações fornecidas pelo usuário de quantas horas de exercicio fisico ele pratica semanalmente, o programa sugere a frequência ideal de atividades físicas para manter um estilo de vida saudável, de acordo com sua idade.

### 3. Quantidade Ideal de Macronutrientes
O usuário fornece os dados de peso e idade e o programa calcula a quantidade de proteinas, gorduras e carboidratos devem ser ingeridos, bem como as calorias diarias.

### 4. Dicas para Melhorar a Saúde
O programa oferece dicas práticas e conselhos para melhorar a saúde e o bem-estar geral, como atividades e exercícios físicos que podem ser praticados.

### 5. Login

A funcionalidade consiste em pedir pra o usuário digitar um nome de usuário e uma senha, e então ele cria um dicionário com as informações, e coloca-o em uma lista. Ela também é responsável por checar, quando o usuário tenta fazer um login, se o usuário existe, e se existir, que a senha seja a definida pelo usuário.

## Módulos do projeto

O projeto é dividido basicamente entre o `main` que é responsável pelo start e fincionamento geral do programa, que faz chamadas de funções do arquivo `funcoes.py`, onde foram colocadas todas as funções necessárias para a utilização do programa, além do arquivo `cálculos.py`, onde ficam as duas funções responsáveis por fazer cálculos matemáticos. Por fim, temos o arquivo `login`, onde se encontra todo o código responsável por pedir, criar e verificar o login do usuário. 

## Requisitos/Bibliotecas

- Python 3.x
- Biblioteca `json` (inclusa no Python)
  Foi utilizada para armazenar as informações de login fornecidas pelo usuário.
- OS
    Foi utilizada para o comando `clear`, que serve para limpar o terminal sempre que uma função é chamada, para manter o ambiente um pouco mais limpo para o usuário.

## Versão 3.0

- Melhorado o sistema de cadastro:
  Agora é possível redefinir a senha utilizando o login e a senha atual.
  Também é possível deletar uma conta existente, também utilizando o login e a senha atual do usuário.
- Agora, sempre que uma conta nova é criada, é pedido ao usuário um objetivo, entre ganhar, perder e manter o peso.
- Agora você pode armazenar o seu IMC para poder vê-lo posteriormente.
- Agora você ganha pontuação baseado na sua melhoria tendo em vista o seu IMC. Caso a diferença entre o IMC atual e o que havia sido guardado seja condizente com o seu objetivo, você obtém 10 pontos. Caso se mantenha o mesmo, você receberá uma outra pontuação.
- Adicionado um sistema de recompensas, onde se pode retirar prêmios baseados em um sistema de compras com os pontos obtidos com o seu progresso pessoal.



