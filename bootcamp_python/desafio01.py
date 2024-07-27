ADD_BONUS = 1000

# Solicitar nome do usuário
nome = input("Informe seu nome: ")

# Solicita salário
salario = float(input("Informe seu salário: "))

# Solicita bônus
bonus = float(input("Digite seu bônus: "))

# Calcular valor final
valor_final = ADD_BONUS + salario * bonus

# Imprimir mensagem
print(f'O usuário {nome} receberá o valor de R$ {valor_final}')

# Qual a quantidade de bugs que esse programa pode ter?
# inputs de dados errados (valores negativos ou strings nos campos float)