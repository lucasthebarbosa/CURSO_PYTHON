# Utilizamos listas para armazenar em um único objeto uma coleção de valores. Muitas vezes, desejamos criar uma nova lista a partir de uma lista original. Observe o código abaixo:



lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]
print(lista_inicial)

lista_final = []

for item in lista_inicial:

    if item % 2 == 0:

        if item < 0:

            lista_final.append(item)
            print(lista_final)
    
        else:

            lista_final.append(-item)
            print(lista_final)
    else:

        if item < 0:
            
            lista_final.append(-2*item)
            print(lista_final)
    
        else:

            lista_final.append(2*item)
            print(lista_final)


print(lista_final)


# Qual deve ser o valor de A, B, C e D, respectivamente, para que o código acima gere a seguinte lista_final: [10, 10, 14, 6, 42, 126, 8, 10, 26]?