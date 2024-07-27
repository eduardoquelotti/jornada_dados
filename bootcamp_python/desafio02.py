import os
os.system('clear')

ADD_BONUS = 1000

def contains_digit(string):
    return any(char.isdigit() for char in string)

while True:
    try:
        # Solicitar nome do usuário
        nome = input("Informe seu nome ou tecle 'S' para sair: ")
        
        if nome == 'S':
            os.system('clear')
            break
        elif contains_digit(nome):
            os.system('clear')
            print('Insira um nome válido: sem números')
            continue
        elif len(nome) == 0:
            os.system('clear')
            print('Insira um nome válido: diferente de vazio')
            continue
        elif nome.isspace():
            os.system('clear')
            print('Insira um nome válido: diferente de vazio')
            continue  
    except ValueError as e:
        print(e)
    
    try:
        # Solicita salário
        salario_input = input("Informe seu salário ou tecle 'S' para sair: ")
        if salario_input == 'S':
            os.system('clear')
            break
        salario = float(salario_input)
        if salario < 0:
            os.system('clear')
            print('O salário deve ser um valor positivo.')
            continue

        # Solicita bônus
        bonus_input = input("Digite seu bônus: ")
        bonus = float(bonus_input)
        if bonus < 0:
            os.system('clear')
            print('O bônus deve ser um valor positivo.')
            continue
            
        # Calcular valor final
        valor_final = ADD_BONUS + salario * bonus

        # Imprimir mensagem
        print(f'O usuário {nome} receberá o valor de R$ {valor_final:.2f}')
        print('')

    except ValueError:
        os.system('clear')
        print('Dados inválidos. Gentileza refazer a operação.')
        print('')