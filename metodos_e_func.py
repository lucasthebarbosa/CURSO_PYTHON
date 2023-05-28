'''
#METODOS DE LISTAS

lista = [1,2,3,7, 9, 8, 10]

# > append
print('Antes do append', lista) 

lista.append(3) #Adiciona o elemento "3" ao final da lista

print("Depois do append", lista)

# > insert

lista.insert(1, 2) #Adiciona o elemento "2" na posição 1 da lista
print("Depois do insert", lista) 

# > extend
lista2=[1,2,3]

lista.extend(lista2) #Pega os elementos da lista2 e coloca no final da lista. Concatena.

print("Depois do extend", lista) 

# > pop
lista.pop() #remove o ultimo elemento da lista
print("Depois do 1º pop", lista)

lista.pop(0) #remove o primeiro elemento da lista
print("Depois do 2° pop", lista)

# > remove

lista.remove(2) #Remove o 1° numero "2" que encontra na lista 
print("Depois do remove", lista)

# > count
print('Quantidade de 2 na lista:', lista.count(2)) #conta quantas vezes o numero "2" aparece na lista

# > index
print("Indice do elemento 10:", lista.index(10)) #retorna o indice do elemento "10"

# > sort
lista.sort() #orndena os elementos
print(lista)

lista.sort(reverse=True) #ordena os elementos, de modo decrescente
print(lista)

#FUNÇÕES PARA LISTAS

#len
print(len(lista)) #imprime o tamanho da lista

#sum
print(sum(lista)) #imprime a soma dos elementos da lista

#max
print("Maior elemento da lista:", max(lista)) #imprime o maior elemento da lista

#min
print("Menor elemento da lista:", min(lista)) #imprime o menor elemento da lista
'''
'''
# > FUNÇÕES

# > 1. CRIANDO FUNÇÕES

def saudacao():
    print("Seja bem-vinda(o)!")
    print("Olá, é um prazer ter você fazendo parte desse curso!")

saudacao()

# Função com parametro

def saudacao(nome,curso):
    print(f"Seja bem-vinda(o), {nome}!")
    print(f"Olá, é um prazer ter você fazendo parte do curso de {curso}!")

saudacao("Majima","Python")
saudacao("Kiryu","Java")

# Função com parametro defaut

def saudacao(nome,curso= "C++"): #Valor padrão, não obrigatorio
    print(f"Seja bem-vinda(o), {nome}!")
    print(f"Olá, é um prazer ter você fazendo parte do curso de {curso}!")

saudacao("Majima", "Python")

# Função com retorno
def soma (num1,num2):
    return num1 + num2 #retorna a soma de num1 e num2

resultado = soma (5,7)
print("O resultado da soma é", resultado)



# > CALCULADORA (desenvolver futuramente)

def calculadora(num1,num2,operação="+"):
    if operação == "+":
        return num1+num2
    elif operação == "-":
        return num1-num2
    
resultado= calculadora(10,20,"-")
print(resultado)
'''
    






