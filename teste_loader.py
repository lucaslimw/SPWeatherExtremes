from utils.loader import carregar_dados, listar_cidades

dados = carregar_dados()

print("Arquivos encontrados:", len(dados))
print()

print("Cidades:")
print(listar_cidades(dados))

print()

for chave in dados:
    print(chave)