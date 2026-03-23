# Lê a linha de entrada e separa os produtos em uma lista
produtos = input().strip().split()

# TODO: Crie uma estrutura para contar quantas vezes cada produto aparece na lista
contagens = []
# Dica: Use um laço para percorrer a lista e atualizar a contagem de cada produto
for produto in produtos:
    ja_contado = False
    for i in range(len(contagens)):
        if contagens[i][0] == produto:
            contagens[i] = (produto, contagens[i][1] + 1)
            ja_contado = True
            break
    if not ja_contado:
        contagens.append((produto, 1))

# Inicialize variáveis para armazenar o produto mais frequente e sua contagem
mais_frequente = None
maior_contagem = -1

# Percorra a lista original para garantir o critério de desempate (primeira ocorrência)
for produto in produtos:
    # TODO: Obtenha a contagem do produto atual e atualize mais_frequente se necessário
    #pass  # Substitua pelo código que compara e atualiza o produto mais frequente
    # Obtenha a contagem do produto atual
    for prd, qtd in contagens:
        if prd == produto:
            contagem = qtd
            break

    if contagem > maior_contagem:
        maior_contagem = contagem
        mais_frequente = produto

# Imprima o produto mais frequente
print(mais_frequente)