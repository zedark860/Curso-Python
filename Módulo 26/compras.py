import json
import os
import time

# Dicionário para armazenar a lista de compras
compras = {}

# Função para limpar a tela do console
def limpar_tela():
    # Verifica o sistema operacional para determinar o comando apropriado para limpar a tela
    os.system('cls' if os.name == "nt" else "clear")

# Função para adicionar um item à lista de compras
def adicionar_item(compras, item, quantidade):
    # Adiciona o item à lista de compras, verificando se o nome do item é válido
    if not item.isalpha():
        raise ValueError('O nome do item deve conter apenas letras.')
    compras[item] = quantidade

# Função para remover um item da lista de compras
def remover_item(compras, item):
    # Remove o item da lista de compras, se ele existir
    if item in compras:
        del compras[item]

# Função para visualizar a lista de compras
def visualizar_compras(compras):
    # Exibe a lista de compras, imprimindo o nome e a quantidade de cada item
    for item, quantidade in compras.items():
        print(f'{item}: {quantidade}')
    print()
    print('Pressione enter para continuar')
    input()

# Função para salvar a lista de compras em um arquivo JSON
def salvar_compras(compras, nome_arquivo):
    # Abre o arquivo JSON para escrita
    with open(nome_arquivo, 'w') as arquivo:
        # Salva a lista de compras no arquivo JSON
        json.dump(compras, arquivo)

# Função para carregar a lista de compras de um arquivo JSON
def carregar_compras(nome_arquivo):
    # Abre o arquivo JSON para leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Carrega a lista de compras do arquivo JSON
        return json.load(arquivo)

# Função principal para gerenciar a lista de compras
def gerenciar_compras(compras, nome_arquivo=None):
    # Enquanto o usuário não escolher a opção 5, o programa irá exibir o menu de opções
    while True:
        limpar_tela()
        # Exibe o menu de opções
        print("""1 Adicionar item
2 Remover item
3 Visualizar lista
4 Salvar e sair
5 Sair sem salvar""")
        # Lê a opção escolhida pelo usuário
        try:
            escolha = int(input('Escolha uma opção: ').strip())
            if escolha < 1 or escolha > 5:
                print('A opção deve conter apenas com números')
                time.sleep(1)
                continue
        except ValueError:
            print('Valor inválido, digite novamente!')
            time.sleep(1)
            continue

        # Executa a ação correspondente à opção escolhida
        if escolha == 1:
            # Adiciona um item à lista de compras
            adicionar_item(compras, input('Digite o nome do item: '), int(input('Digite a quantidade: ')))
        elif escolha == 2:
            # Remove um item da lista de compras
            remover_item(compras, input('Digite o nome do item: '))
        elif escolha == 3:
            # Visualiza a lista de compras
            visualizar_compras(compras)
        elif escolha == 4:
            # Salva a lista de compras em um arquivo JSON e sai do programa
            if nome_arquivo is None:
                nome_arquivo = input('Digite o nome do arquivo para salvar:')
            salvar_compras(compras, nome_arquivo)
            break
        elif escolha == 5:
            # Sai do programa sem salvar
            break
        else:
            print('Opção inválida. Digite novamente!')
            time.sleep(1)
            continue

# Função principal do programa
def main():
    # Inicia um loop infinito.
    while True:

        # Limpa a tela e exibe o menu principal.
        limpar_tela()
        print("""1 Criar uma nova lista de compras
2 Carregar uma lista existente
3 Sair""")

        # Lê a escolha do usuário.
        try:
            escolha = int(input('Escolha uma opção: ').strip())
            if escolha < 1 or escolha > 3:
                print('A opção deve conter apenas com números')
                time.sleep(1)
                continue
        except ValueError:
            print('Valor inválido, digite novamente!')
            time.sleep(1)
            continue

        # Executa a ação correspondente à escolha do usuário.
        if escolha == 1:
            # Cria uma nova lista de compras e a gerencia.
            compras = {}
            gerenciar_compras(compras)
        elif escolha == 2:
            # Carrega uma lista de compras existente e a gerencia.
            
            # **Exibe uma mensagem informando ao usuário que as listas disponíveis serão listadas.**
            print('Listas disponíveis:')

            # **Cria uma lista com os nomes das listas de compras existentes.**
            arquivos = [arquivo for arquivo in os.listdir() if arquivo.endswith('.json')]

            # **Verifica se existem listas de compras disponíveis.**
            if not arquivos:

                # **Imprime uma mensagem de erro se não houver listas de compras disponíveis.**
                print('Nenhuma lista foi encontrada, verifique novamente!')
                time.sleep(2)
                continue

            # **Lista os nomes das listas de compras disponíveis.**
            for i, arquivo in enumerate(arquivos, 1):
                print(f"{i}: {arquivo}")

            # **Lê a escolha do usuário.**
            try:
                escolha = int(input('Escolha uma lista para carregar (0 se nenhuma): ').strip())
                if escolha == 0:
                    continue
                if escolha < 0 or escolha > len(arquivos):
                    print('Opção inválida. Digite novamente!')
                    time.sleep(1)
                    continue
                nome_arquivo = arquivos[escolha - 1]
                compras = carregar_compras(nome_arquivo)
                gerenciar_compras(compras, nome_arquivo)
            except ValueError:
                print('Valor inválido, digite novamente!')
                continue
        elif escolha == 3:
            # Encerra o programa.
            print('Programa encerrado. Volte sempre!')
            break
        else:
            # Imprime uma mensagem de erro e continua o loop.
            print('Opção inválida. Digite novamente!')
            time.sleep(1)
            continue

# Inicia o programa
if __name__ == "__main__":
    main()