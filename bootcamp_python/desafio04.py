import csv
import os
from typing import List

# Função para ler o arquivo
def ler_csv(path: str) -> List[dict]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"O arquivo {path} não foi encontrado.")
    with open(path, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)

# Função para processar os dados em um dicionário
def processar_dados(dados: List[dict]) -> dict:
    categorias = {}
    for item in dados:
        categoria = item['Categoria']
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(item)
    return categorias

# Função para calcular o total de vendas por categoria
def calcular_vendas_categoria(dados: dict) -> dict:
    vendas_por_categoria = {}
    for categoria, itens in dados.items():
        total_vendas = sum(float(item['Quantidade']) * float(item['Venda']) for item in itens)
        vendas_por_categoria[categoria] = total_vendas
    return vendas_por_categoria

# Função principal para integrar as funções anteriores
def main():
    # Use o caminho absoluto para o arquivo CSV
    nome_arquivo = '/Users/eduardoquelotti/Projetos Python/jornada_dados/bootcamp_python/vendas.csv'
    try:
        dados_brutos: dict = ler_csv(nome_arquivo)
        dados_processados: dict = processar_dados(dados_brutos)
        vendas_categoria: dict = calcular_vendas_categoria(dados_processados)
        for categoria, total in vendas_categoria.items():
            print(f'{categoria}: R$ {total:.2f}')
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == '__main__':
    main()