from etl_fixacao import armazenar_csv, processar_categoria , calcular_categoria

lista_csv = armazenar_csv('vendas.csv')
categoria_dicionario = processar_categoria(lista_csv)
total_da_categoria = calcular_categoria(categoria_dicionario)

print(total_da_categoria)


# def soma(valor_1_para_somar: float, valor_2_para_somar: float = 10) -> float:
#     """
#     uma funcao simples para somar
#     """
#     retorno_soma = valor_1_para_somar + valor_2_para_somar
#     return retorno_soma

# valor3 = soma(6.2,10.8)
# valor2 = soma(2)
# print(valor2)