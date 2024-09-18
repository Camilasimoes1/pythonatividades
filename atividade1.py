# Exigência A: Print com o nome completo
print("Bem-vindos à Loja de João Silva!")  # Altere para o seu nome completo

# Exigência B: Input do valor do pedido e da quantidade de parcelas
valor_do_pedido = float(input("Digite o valor do pedido: R$"))
quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))

# Exigência C: Definindo a taxa de juros conforme a quantidade de parcelas
if quantidade_parcelas < 4:
    juros = 0  # Sem juros
elif 4 <= quantidade_parcelas < 6:
    juros = 4  # 4% de juros
elif 6 <= quantidade_parcelas < 9:
    juros = 8  # 8% de juros
elif 9 <= quantidade_parcelas < 13:
    juros = 16  # 16% de juros
else:
    juros = 32  # 32% de juros

# Exigência D: Cálculo do valor total parcelado e valor da parcela
valor_total_parcelado = valor_do_pedido * (1 + juros / 100)  # Aplica o juros sobre o valor do pedido
valor_da_parcela = valor_total_parcelado / quantidade_parcelas  # Divide o valor total pelo número de parcelas

# Exigência E: Exibe o valor total parcelado e o valor de cada parcela
print(f"O valor total parcelado é: R${valor_total_parcelado:.2f}")
print(f"O valor de cada parcela será: R${valor_da_parcela:.2f}")

# Exigência G: Comentários explicativos no código

# O programa primeiro calcula o valor total parcelado com base nos juros, que dependem da quantidade de parcelas.
# O valor de cada parcela é então obtido dividindo o valor total parcelado pela quantidade de parcelas.

# Exigências de saída de console:
# Exigência G: O nome completo já foi exibido na saída.
# Exigência H: Exibindo os resultados do parcelamento com juros, caso a quantidade de parcelas seja maior ou igual a 4.
