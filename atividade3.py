# Exigência A: Print com o nome completo
print("Bem-vindos à Fábrica de Camisetas do João Silva!")  # Altere para seu nome completo

# Exigência B: Função para escolher o modelo de camiseta
def escolha_modelo():
    while True:
        modelo = input("Escolha o modelo de camiseta (MCS/MLS/MCE/MLE): ").upper()
        if modelo == "MCS":
            return 1.80
        elif modelo == "MLS":
            return 2.10
        elif modelo == "MCE":
            return 2.90
        elif modelo == "MLE":
            return 3.20
        else:
            print("Modelo inválido. Tente novamente.")  # Exigência de saída de console 2

# Exigência C: Função para obter o número de camisetas e calcular desconto
def num_camisetas():
    while True:
        try:
            num = int(input("Digite o número de camisetas: "))
            if num > 20000:
                print("Não aceitamos pedidos com mais de 20.000 camisetas.")  # Exigência de saída de console 3
                continue
            elif num >= 2000:
                return num * 0.88  # 12% de desconto
            elif num >= 200:
                return num * 0.93  # 7% de desconto
            elif num >= 20:
                return num * 0.95  # 5% de desconto
            else:
                return num  # Sem desconto
        except ValueError:
            print("Número inválido. Tente novamente.")

# Exigência D: Função para escolher o frete
def frete():
    while True:
        opcao_frete = input("Escolha o serviço de frete (0 para Retirar, 1 para Transportadora, 2 para Sedex): ")
        if opcao_frete == "0":
            return 0  # Retirar na fábrica
        elif opcao_frete == "1":
            return 100  # Frete por Transportadora
        elif opcao_frete == "2":
            return 200  # Frete por Sedex
        else:
            print("Opção de frete inválida. Tente novamente.")

# Exigência E: Cálculo total a pagar
if __name__ == "__main__":
    # Exibindo nome completo (já feito no início)
    
    # Pegando o modelo e preço
    preco_unitario = escolha_modelo()  # Exigência B
    # Pegando o número de camisetas com desconto
    num_total_camisetas = num_camisetas()  # Exigência C
    # Pegando o frete
    valor_frete = frete()  # Exigência D

    # Cálculo do valor total
    total_a_pagar = (preco_unitario * num_total_camisetas) + valor_frete

    # Exibindo o resultado final
    print(f"Total a pagar: R${total_a_pagar:.2f}")  # Exigência H

# Exigência F: try/except já implementado em num_camisetas()
# Exigência G: Comentários foram adicionados no código
