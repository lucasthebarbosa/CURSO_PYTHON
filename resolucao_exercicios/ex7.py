cont = 0
resultado = 1
n = 1000

while cont != n:

    resultado = resultado + 1/(2**cont)

    cont = cont + 1

print(resultado)

#R: Sinceramente, acho que nessa houve um erro tecnico da ADA. Pois as alternativas sao:
"""
Ao ser executado, o que o trecho de código acima mostra na tela?


A soma dos n-1 (no caso, n-1 = 999) primeiros termos da série 1/2, 1/2, 1/2, 1/2,...


A soma dos n (no caso, n = 1000) primeiros termos da série 1, 1/2, 1/4, 1/8,...


A soma dos n (no caso, n = 1000) primeiros termos da série 1/2, 1/4, 1/8, 1/16,...


A soma dos n (no caso, n = 1000) primeiros termos da série 1/2, 1/2, 1/2, 1/2,...


A soma dos n-1 (no caso, n-1 = 999) primeiros termos da série 1, 1/2, 1/4, 1/8,...
"""

#enfim, posso olhar com mais calma depois...