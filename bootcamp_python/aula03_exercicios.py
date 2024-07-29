### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

# quantidade = int(input('Informe a quantidade: '))
# preco = float(input('Informe o preço: '))

# if quantidade > 0 and preco > 0:
#     print('Dados válidos inseridos no banco')
# else:
#     print('Dados inválidos inseridos no banco')



### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18 C é baixa
# Temperatura >= 18 e <= 26 é normal
# Temperatura > 26 é alta

# temperatura = float(input('Informe a temperatura do dia: '))

# if temperatura < 18:
#     print('Baixa')
# elif temperatura >= 18 and temperatura <= 26:
#     print('Normal')
# else:
#     print('Alta')



### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] == 'ERROR':
#     print(log['message'])



### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# nome = input('Informe o nome do usuário: ')

# while True:
#     idade = int(input('Informe a idade do usuário: '))
#     if idade < 18 or idade > 65:
#         print('Idade não permitida')
#         continue
#     while True:
#         email = input('Informe o email do usuário: ')
#         if '@' not in email or '.' not in email:
#             print('Email inválido informado')
#         else:
#             print('Usuário adicionado')
#             exit()



### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# transacao = {'valor': 9000, 'hora': 10}


# if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
#     print('Transação suspeita')
# else:
#     print('Transação normal')



### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# texto = "Hoje é um dia diferente. Hoje é um dia especial. Cruzeiro é gigante e será campeão e tudo"

# lista = texto.split()

# contador = {}

# for palavra in lista:
#     if palavra not in contador:
#         contador[palavra] = 1
#     else:
#         contador[palavra] += 1

# print(contador)


# texto = "Hoje é um dia diferente. Hoje é um dia especial. Cruzeiro é gigante e será campeão e tudo"

# lista = texto.split()

# contador = {}

# for palavra in lista:
#     if palavra in contador:
#         contador[palavra] += 1
#     else:
#         contador[palavra] = 1

# print(contador)



### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# numeros = [10, 20, 30, 40, 50]

# menor = min(numeros)
# maior = max(numeros)

# normalizados = []

# for numero in numeros:
#     normalizado = (numero - menor) / (maior - menor)
#     normalizados.append(normalizado)

# print("Normalizados Opção 1: ", normalizados)

# normalizados_02 = [(x - menor) / (maior - menor) for x in numeros]

# print("Normalizados Opção 2: ", normalizados_02)



### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# usuarios_validados = []
# usuarios_invalidos = []

# for usuario in usuarios:
#     if usuario['nome'] != "" and usuario['email'] != "":
#         usuarios_validados.append(usuario)
#     else:
#         usuarios_invalidos.append(usuario)

# print("Usuários Validados:", usuarios_validados)
# print("Usuários Invalidos:", usuarios_invalidos)


# usuarios_validados02 = [user for user in usuarios if user['nome'] != "" and user['email'] != ""]
# usuarios_invalidos02 = [user for user in usuarios if user['nome'] == "" or user['email'] == ""]

# print("Usuários Validados 02:", usuarios_validados02)
# print("Usuários Invalidos 02:", usuarios_invalidos02)



### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# numeros = range(1,11)
# pares = [numero for numero in numeros if numero % 2 == 0]
# print(pares)



### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# total_por_categoria = {}
# for venda in vendas:
#     categoria = venda['categoria']
#     valor = venda['valor']
#     if categoria in total_por_categoria:
#         total_por_categoria[categoria] += valor
#     else:
#         total_por_categoria[categoria] = valor

# print(total_por_categoria)



### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# while True:
#     entrada = input('Escreva a palavra desejada: ')
#     if entrada == 'Sair':
#         exit()
#     else:
#         print('Palavra preenchida: ', entrada)



### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# while True:
#     numero_selecionado = int(input('Informe um número: '))
#     if numero_selecionado not in range(0,6):
#         print('Número inválido informado: ',numero_selecionado)
#         continue
#     else:
#         print('Número válido informado: ', numero_selecionado)



### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

pagina_atual = 1
paginas_totais = 5

while pagina_atual <= paginas_totais:
    print(f'Processando página {pagina_atual} de {paginas_totais}')
    pagina_atual += 1

print('Todas as páginas foram processadas')