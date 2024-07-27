# #### Inteiros (`int`)

# print('1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.')

# num1 = int(input('Informe um número inteiro: '))
# num2 = int(input('Informe outro número inteiro: '))
# resultado = num1 + num2
# print(f'A soma dos números {num1} e {num2} é {resultado}')
# print('')

# print('2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.')
# num3 = int(input('Informe um número inteiro: '))
# resultado = num3 % 5
# print(f'O resto da divisão do número {num3} por 5 é {resultado}')
# print('')


# print('3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.') 
# num4 = int(input('Informe um número inteiro: '))
# num5 = int(input('Informe outro número inteiro: '))
# resultado = num4 * num5
# print(f'A multiplicação dos números {num4} e {num5} é {resultado}')
# print('')

# print('4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.')
# num6 = int(input('Informe um número inteiro: '))
# num7 = int(input('Informe outro número inteiro: '))
# resultado = num6 // num7
# print(f'A divisão inteira dos números {num6} e {num7} é {resultado}')
# print('')


# print('5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.')
# num8 = int(input('Informe um número inteiro: '))
# resultado = num8 ** 2
# print(f'O número {num8} ao quadrado é {resultado}')
# print('')


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# num1 = float(input('Informe um número decimal: '))
# num2 = float(input('Informe outro número decimal: '))
# resultado = num1 + num2
# print(f'A soma dos números {num1} e {num2} é {resultado}')

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# num1 = float(input('Informe um número decimal: '))
# num2 = float(input('Informe outro número decimal: '))
# resultado = (num1 + num2)/2
# print(f'A média dos números {num1} e {num2} é {float(resultado)}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# num1 = float(input('Informe a base da potência: '))
# num2 = float(input('Informe o expoente: '))
# resultado = num1 ** num2 
# print(f'O resultado do valor {num1} elevado a {num2} é {float(resultado)}')

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# num1 = float(input('Informe a temperatura em Celsius: '))
# resultado = (num1 * 1.8) + 32 
# print(f'A temperatura em {num1} graus Celsius corresponde a {resultado} em Fahrenheit')

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# import math
# raio = float(input('Informe o raio do círculo: '))
# area = math.pi * raio ** 2
# print(f'A área de um círculo com raio igual a {raio} é {area:.2f}')

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# nome = input('Informe seu nome completo: ')
# print(f'O nome informado em letras maiúsculas é: {nome.upper()}')

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = input('Informe seu nome completo: ')
# print(f'O nome informado em letras minúsculas é: {nome.lower()}')

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input('Escreva uma mensagem ou uma frase qualquer: ')
# print(f'{frase.strip()}')


# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data_informada = input('Informe a data de hoje no formato dd/mm/aaaa: ')
# lista = data_informada.split('/')
# print(f'O dia informado foi: {lista[0]}')
# print(f'O mês informado foi: {lista[1]}')
# print(f'O ano informado foi: {lista[2]}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# nome_usuario = input('Informe seu nome: ')
# sobrenome_usuario = input('Informe seu sobrenome: ')
# nome_completo = nome_usuario + " " + sobrenome_usuario
# print(f'O nome completo do usuário é: {nome_completo}')

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# var1 = True
# var2 = True

# print(f'{var1 and var2}')

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# var1 = True
# var2 = True

# print(f'{var1 or var2}')

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# var1 = True
# if var1 == True:
#     var2 = False
#     print(var2)
# else:
#     print(var1)


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# num1 = int(input('Informe um número inteiro: '))
# num2 = int(input('Informe outro número inteiro: '))
# if num1 == num2:
#     print('Os números informados pelo usuário são iguais')
# else:
#     print('Os números informados pelo usuário são diferentes')

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# num1 = int(input('Informe um número inteiro: '))
# num2 = int(input('Informe outro número inteiro: '))
# if num1 != num2:
#     print('Os números informados pelo usuário são diferentes')
# else:
#     print('Os números informados pelo usuário são iguais')


# #### try-except e if

# 21: Conversor de Temperatura

# while True:
#     try:
#         num1 = float(input('Informe a temperatura: '))
#         escala = input('Informe a escala utilizada (C ou F): ')

#         if escala != 'C' and escala != 'F':
#             print('Informe a escala termométrica válida')
#             print('')
#         elif isinstance(num1, float) and escala == 'C':
#             resultado = (num1 * 1.8) + 32 
#             print(f'A temperatura em {num1} graus Celsius corresponde a {resultado} em Fahrenheit')
#             print('')
#         elif isinstance(num1, float) and escala == 'F':
#             resultado = (num1 - 32)/1.8 
#             print(f'A temperatura em {num1} graus Fahrenheit corresponde a {resultado} em Celsius')
#             print('')
#     except:
#         print('Por favor, informe um número válido para temperatura')
#         print('')

# 22: Verificador de Palíndromo => Meu métododo

# def reverse(string):
#     frase_reverse = string[::-1]
#     return frase_reverse

# try:
#     frase = input('Informe sua palavra ou frase para avaliarmos se é ou não um palíndromo: ')

#     if isinstance(frase, str):
#         if frase == reverse(frase):
#             print('A frase/palavra informada é um palíndromo')
#         else:
#             print('A frase/palavra informada não é um palíndromo')
#     else:
#         print('Entrada inválida. Gentileza informar uma frase ou palavra válida')

# except ValueError:
#     print('A frase informada não é um palíndromo')

## Método Luciano Galvão

# entrada = input("Digite uma palavra ou frase: ")
# if isinstance(entrada, str):
#     formatado = entrada.replace(" ", "").lower()
#     if formatado == formatado[::-1]:
#         print("É um palíndromo.")
#     else:
#         print("Não é um palíndromo.")
# else:
#     print("Entrada inválida. Por favor, digite uma palavra ou frase.")


# 23: Calculadora Simples

# def printar_resultado(resultado):
#     print('Resultado: ', resultado)
#     print('')

# while True:
#     try:

#         num1 = float(input('Informe o primeiro número: '))
#         num2 = float(input('Informe o segundo número: '))
#         operador = input('Digite o operador (+, -, *, /): ')

#         if operador == '+':
#             printar_resultado(num1 + num2)
#         elif operador == '-':
#             printar_resultado(num1 - num2)
#         elif operador == '*':
#             printar_resultado(num1 * num2)
#         elif operador == '/' and num2 != 0:
#             printar_resultado(num1 / num2)
#         else:
#             print('Operação inválida. Certifique-se de escolher um operador válido ou utilizar números válidos para a operação desejada')
#             print('')

#     except ValueError:
#         print('Erro: Entrada inválida. Certifique-se de inserir números')
#         print('')

# 24: Classificador de Números

# try:
#     numero = int(input("Digite um número: "))
#     if numero > 0:
#         print("Positivo")
#     elif numero < 0:
#         print("Negativo")
#     else:
#         print("Zero")
#     if numero % 2 == 0:
#         print("Par")
#     else:
#         print("Ímpar")
# except ValueError:
#     print("Por favor, digite um número inteiro válido.")

# 25: Conversão de Tipo com Validação

# entrada_lista = input("Digite uma lista de números separados por vírgula: ")
# numeros_str = entrada_lista.split(",")
# numeros_int = []
# try:
#     for num in numeros_str:
#         numeros_int.append(int(num.strip()))
#     print("Lista de inteiros:", numeros_int)
# except ValueError:
#     print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")