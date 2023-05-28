# > DICIONÁRIOS

# Criando dicionários

dicionario = {}

dicionario = dict()

dicionario = {'nome': 'Lucas', 'idade': 24, 'altura': 1.77}

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos a um dicionário

dicionario['programador'] = True # Adiciona o elemendo progamador ao dict, e retorna seu booleano.
print(dicionario)


dicionario['altura'] = 1.86 # Sobreescreve o elemento "altura" no dict.
print(dicionario)

# Iterando sobre um dicionario

for chave in dicionario:
    print(chave, dicionario[chave])

#Testando a existencia de uma chave

print('peso' in dicionario)
print('altura' in dicionario)
print('nome' in dicionario)



