import os
os.system('clear')

ADD_BONUS = 1000
nome_valido = False
salario_valido = False
bonus_valido = False

print('====================================================')
print('================CALCULADORA DE RENDA================')
print('====================================================')
print('Tecle "S" para sair')
print('')
def contains_digit(string):
    return any(char.isdigit() for char in string)

def contains_alpha(string):
    return any(char.isalpha() for char in string)

while True:
    while nome_valido == False:
        try:
            # Solicitar nome do usuário
            nome = input("Informe seu nome: ")
            
            if nome == 'S':
                os.system('clear')
                exit()
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
            else:
                nome_valido = True
        except ValueError as e:
            print(e)

    while salario_valido == False:
        try:
            # Solicita salário
            print('')
            salario_input = input(f"{nome}, informe seu salário: ")
            if salario_input == 'S':
                os.system('clear')
                exit()
            salario = float(salario_input)
            if salario < 0:
                print('O salário deve ser um valor positivo.')
                continue
            elif contains_alpha(salario_input):
                print('Insira um valor numérico')
                continue 
            else:
                print(f'Salário declarado: R${salario_input}')
                salario_valido = True
        except ValueError as e:
            print(e)

    while bonus_valido == False:
        try:
            # Solicita bônus
            print('')
            bonus_input = input("Digite seu bônus: ")
            bonus = float(bonus_input)
            if bonus < 0:
                print('O bônus deve ser um valor positivo.')
                continue
            else:
                # Calcular valor final
                print('')
                valor_final = ADD_BONUS + salario * bonus     
                print(f'O salário declarado pelo usuário(a) {nome} é R${salario_input}, com um bônus de {bonus}, sendo assim, o usuário receberá o valor de R$ {valor_final:.2f}')  
                print('')
                print('====================================================')
                print('================CALCULADORA DE RENDA================')
                print('====================================================')
                print('Tecle "S" para sair')
                print('')
                bonus_valido = True     

        except ValueError:
            os.system('clear')
            print('Dados inválidos. Gentileza refazer a operação.')
            print('')
            

    nome_valido = False
    salario_valido = False
    bonus_valido = False  
