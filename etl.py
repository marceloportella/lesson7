import csv

def ler_csv(nome_arquivo: str) -> list[dict]:
    """
    Funcao que le os arquivos
    """
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)
    
def processar_dados(dados):
    categorias = {}
    for item in dados:
        categoria = item['Categoria']
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(item)
    return categorias


## Calcular por categoria

def calcular_categoria(dados_categoria: dict) -> dict:
    categorias = {}
    valor = 0
    for categoria, itens in dados_categoria.items():
        for item in itens:
            valor += float(item["Venda"]) * int(item["Quantidade"])
        categorias[categoria]=valor

    return categorias




# local_arquivo = 'vendas.csv'
# lista_arquivo = ler_csv(local_arquivo)
# categoria = processar_dados(lista_arquivo)
# total_categorias = calcular_categoria(categoria)
# print (total_categorias)

# teste_categorias = {'Electronics': [{'Produto': 'Notebook', 'Categoria': 'Electronics', 'Quantidade': '5', 'Venda': '3000'}, 
#                                     {'Produto': 'Smartphone', 'Categoria': 'Electronics', 'Quantidade': '10', 'Venda': '500'}, 
#                                     {'Produto': 'Tablet', 'Categoria': 'Electronics', 'Quantidade': '2', 'Venda': '1500'}], 
#                     'Apparel': [{'Produto': 'Camiseta', 'Categoria': 'Apparel', 'Quantidade': '20', 'Venda': '20'}, 
#                                 {'Produto': 'Tênis', 'Categoria': 'Apparel', 'Quantidade': '10', 'Venda': '50'}], 
#                     'Kitchen': [{'Produto': 'Cafeteira', 'Categoria': 'Kitchen', 'Quantidade': '3', 'Venda': '100'}]}



# categoria_valor = {}
# valor=0
# for categoria, itens in teste_categorias.items():
#     for item in itens:
#         valor += float(item["Venda"]) * int(item["Quantidade"])
#     categoria_valor[categoria]=valor    

# print(categoria_valor)
       
   
