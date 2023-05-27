'''notas= [7.9, 9.7, 8.2]

notas() #metodo
lista = [19,"nat", 3.14, True] #diferentes tipos de dados
lista_de_listas = [10,[1,2,3]]
'''
'''
#indexação e slices

lista = [19,"amo a nat", 3.14, True]

print(lista[0]) #indexa e printa o elemento na posição 0 na lista
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1]) #indexa e printa o ultimo elemento da lista


'''
#Slices
notas= [7.9, 9.7, 8.2, 10]
'''print(notas[0:3]) #imprime elementos da posção 0 a 2
print(notas[1:3])
print(notas[2:])
print(notas[0:3:2])'''


# > Iterações com FOR

# 1. Utilizando os elementos da lista

for elemento in notas:
    print(elemento)

# 2. Utilizando indices
print('Comprimento da lista ', len(notas)) 

for i in range(len(notas)):
    print(notas[i]) #imprime todos os elementos da lista notas usando len(lenght), usando o indice.






