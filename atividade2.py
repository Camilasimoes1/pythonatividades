# Exigência A: Print com o nome completo e o menu para o cliente
print("Bem vindos à Loja de Marmitas de João Silva!")  # Altere para seu nome completo
print("Menu de opções:")
print("Bife Acebolado (BA) - Tamanho P: R$16, M: R$18, G: R$22")
print("Filé de Frango (FF) - Tamanho P: R$15, M: R$17, G: R$21")

# Exigência E: Inicializando o acumulador de pedidos
acumulador = 0

# Exigência G: Usando while para repetir o pedido até o cliente encerrar
while True:
    # Exigência B: Input para o sabor com validação
    sabor = input("Escolha o sabor (BA para Bife Acebolado ou FF para Filé de Frango): ").upper()
    
    if sabor != "BA" and sabor != "FF":
        print("Sabor inválido. Tente novamente.")  # Exigência de console 2
        continue  # Volta para o início do loop

    # Exigência C: Input para o tamanho com validação
    tamanho = input("Escolha o tamanho (P para Pequeno, M para Médio, G para Grande): ").upper()
    
    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print("Tamanho inválido. Tente novamente.")  # Exigência de console 3
        continue  # Volta para o início do loop

    # Exigência D: Estrutura de if/elif/else aninhada para calcular o valor do pedido
    if sabor == "BA":
        if tamanho == "P":
            valor = 16
        elif tamanho == "M":
            valor = 18
        else:  # Tamanho G
            valor = 22
    elif sabor == "FF":
        if tamanho == "P":
            valor = 15
        elif tamanho == "M":
            valor = 17
        else:  # Tamanho G
            valor = 21

    # Exibindo o valor do pedido atual
    print(f"Você pediu {sabor} de tamanho {tamanho}. Valor: R${valor}")

    # Exigência E: Acumulando o valor do pedido
    acumulador += valor

    # Exigência F: Pergunta ao cliente se deseja pedir mais alguma coisa
    mais_pedido = input("Deseja pedir mais alguma coisa? (S para Sim / N para Não): ").upper()
    
    if mais_pedido == "N":
        break  # Sai do loop se o cliente não quiser mais pedidos
    elif mais_pedido != "S":
        print("Opção inválida. Encerrando pedidos.")
        break

# Exigência F: Exibe o valor total acumulado
print(f"Total a pagar: R${acumulador}")

# Exigência de console 4: Exemplo com dois pedidos diferentes
print("Exemplo de pedido com dois sabores e tamanhos diferentes:")
print("Bife Acebolado tamanho M: R$18")
print("Filé de Frango tamanho G: R$21")
