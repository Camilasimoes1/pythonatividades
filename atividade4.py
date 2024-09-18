# Exigência A: Print com o nome completo
print("Bem-vindos à empresa do João Silva!")  

# Exigência B: Lista de funcionários e variável global
lista_funcionarios = []  # Exigência G: Lista contendo dicionários
id_global = 123456  # Exemplo de RU para inicialização

# Exigência C: Função para cadastrar funcionário
def cadastrar_funcionario(id_func):
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    
    # Criando um dicionário com os dados do funcionário
    funcionario = {"id": id_func, "nome": nome, "setor": setor, "salario": salario}
    
    # Adicionando o dicionário à lista de funcionários
    lista_funcionarios.append(funcionario.copy())
    print(f"Funcionário {nome} cadastrado com sucesso!\n")

# Exigência D: Função para consultar funcionários
def consultar_funcionarios():
    while True:
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":  # Consultar todos os funcionários
            if lista_funcionarios:
                for func in lista_funcionarios:
                    print(func)
            else:
                print("Nenhum funcionário cadastrado.")
        elif opcao == "2":  # Consultar por Id
            id_pesquisa = int(input("Digite o ID do funcionário: "))
            funcionario_encontrado = next((f for f in lista_funcionarios if f["id"] == id_pesquisa), None)
            if funcionario_encontrado:
                print(funcionario_encontrado)
            else:
                print("Funcionário não encontrado.")
        elif opcao == "3":  # Consultar por Setor
            setor_pesquisa = input("Digite o setor: ")
            funcionarios_setor = [f for f in lista_funcionarios if f["setor"] == setor_pesquisa]
            if funcionarios_setor:
                for func in funcionarios_setor:
                    print(func)
            else:
                print(f"Nenhum funcionário encontrado no setor {setor_pesquisa}.")
        elif opcao == "4":  # Retornar ao menu
            return
        else:
            print("Opção inválida. Tente novamente.")

# Exigência E: Função para remover funcionário
def remover_funcionario():
    while True:
        id_remover = int(input("Digite o ID do funcionário que deseja remover: "))
        funcionario_encontrado = next((f for f in lista_funcionarios if f["id"] == id_remover), None)
        
        if funcionario_encontrado:
            lista_funcionarios.remove(funcionario_encontrado)
            print(f"Funcionário de ID {id_remover} removido com sucesso!\n")
            return
        else:
            print("ID inválido. Tente novamente.")

# Exigência F: Estrutura de menu principal
while True:
    print("Menu Principal:")
    print("1. Cadastrar Funcionário")
    print("2. Consultar Funcionário")
    print("3. Remover Funcionário")
    print("4. Encerrar Programa")
    
    opcao_menu = input("Escolha uma opção: ")
    
    if opcao_menu == "1":
        id_global += 1  # Incrementa o ID global
        cadastrar_funcionario(id_global)  # Exigência F.a.i
    elif opcao_menu == "2":
        consultar_funcionarios()  # Exigência F.a.ii
    elif opcao_menu == "3":
        remover_funcionario()  # Exigência F.a.iii
    elif opcao_menu == "4":
        print("Encerrando programa...")  # Exigência F.a.iv
        break
    else:
        print("Opção inválida. Tente novamente.")  # Exigência F.a.v

# Exigência H: Inserir comentários relevantes no código
# Comentários adicionados para descrever cada parte do código
