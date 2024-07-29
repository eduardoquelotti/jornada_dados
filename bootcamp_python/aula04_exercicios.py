# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

# lista = range(0,11)

# for x in lista:
#     print(x**2)



# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

# lista_original = ["Python", "Java", "C++", "JavaScript"]
# print('[Lista Original]: ', lista_original)

# lista_original.remove('C++')
# print('[Remove C++]: ', lista_original)

# lista_original.append('Ruby')
# print('[Add Ruby]: ', lista_original)



# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

# livros = [
#     {'titulo': 'Dexter', 'autor': 'João da Silva', 'ano': 1995},
#     {'titulo': 'God of War', 'autor': 'Kleber', 'ano': 1995},
#     {'titulo': 'Game of Thrones', 'autor': 'Rodolfo', 'ano': 1995},
#     {'titulo': 'O dia depois de amanhã', 'autor': 'Maria', 'ano': 1995},
# ]

# for livro in livros:
#     titulo = livro['titulo']
#     autor = livro['autor']
#     ano = livro['ano']
#     print(f"O livro {titulo} foi escrito por {autor} em {ano}")



# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# while True:
#     palavra = input('Informe a palavra desejada: ')

#     contagem = {}
#     for caract in palavra:
#         if caract.lower() in contagem:
#             contagem[caract.lower()] += 1
#         else:
#             contagem[caract.lower()] = 1

#     print(f'A palavra escolhida foi: {palavra}')
#     print(contagem)


# def contar_caract(palavra):
#     contagem = {}
#     for caract in palavra:
#         if caract.lower() in contagem:
#             contagem[caract.lower()] += 1
#         else:
#             contagem[caract.lower()] = 1
#     return contagem

# palavra = input('Informe a palavra desejada: ')
# print(contar_caract(palavra))


# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

# lista_compras = ["maçã", "banana", "cereja"]

# tabela_preco = {"maçã": 0.45, 
#                 "banana": 0.30, 
#                 "cereja": 0.65}

# preco_total = 0
# for item in lista_compras:
#     preco_total = preco_total + tabela_preco[item]

# print('O valor total da compra é: R$ ', preco_total)