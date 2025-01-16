import csv


def armazenar_csv(local_csv:str) -> list[dict]:
    with open (local_csv, mode='r', encoding='utf-8') as arquivo:
        resultado = csv.DictReader(arquivo)
        return list(resultado)


def processar_categoria(lista_dicionario:dict) -> dict:
    categoria = {}
    for item_categoria in lista_dicionario:
        vcat = item_categoria['Categoria']
        if vcat not in categoria:
            categoria[vcat] = []

        categoria[vcat].append(item_categoria)

    return dict(categoria)

def calcular_categoria(parametro_lista: dict) -> dict[list]:
    categoria_total = {}
    for categoria, itemcategoria in parametro_lista.items():
        total = sum(float(itens['Venda']) * int(itens['Quantidade']) for itens in itemcategoria)
        categoria_total[categoria]=total
    return categoria_total

lista_csv = armazenar_csv('vendas.csv')
categoria_dicionario = processar_categoria(lista_csv)
total_da_categoria = calcular_categoria(categoria_dicionario)

print(total_da_categoria)



# categoria_temp = [{'Produto': 'Notebook', 'Categoria': 'Electronics', 'Quantidade': '5', 'Venda': '3000'}, {'Produto': 'Smartphone', 'Categoria': 'Electronics', 'Quantidade': '10', 'Venda': '500'}, {'Produto': 'Camiseta', 'Categoria': 'Apparel', 'Quantidade': '20', 'Venda': '20'}, {'Produto': 'Cafeteira', 'Categoria': 'Kitchen', 'Quantidade': '3', 'Venda': '100'}, {'Produto': 'Tênis', 'Categoria': 'Apparel', 'Quantidade': '10', 'Venda': '50'}, {'Produto': 'Tablet', 'Categoria': 'Electronics', 'Quantidade': '2', 'Venda': '1500'}]

# categoria2 = {}
# for item in categoria_temp:
#     categoria2[item]
#     print(item['Categoria'])
