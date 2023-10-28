precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}
dicionario_precos = {}

for produto, preco in precos.items():
    if preco == 1000:
        novo_preco = preco * 1.10
    elif preco > 1000 and preco <= 2000:
        novo_preco = preco * 1.15
    else:
        novo_preco = preco * 1.20
    dicionario_precos[produto] = novo_preco
print(f'Os novo preços são {dicionario_precos}')