'''
As funções permite modularizar o código, dividir ele em partes 
menores que podem ser reaprovaitadas. Isso simplifica a 
codificação.

Estrutura função em python

def nome_funcao(param1, param2, paramN);
    //algum codigo que a funcao faz 
    return valor_retornado
'''
#cria uma função que calcula a área de triângulo
def calculateTrianglArea(base, altura):
    area = (base * altura)/ 2
    return area

#cria uma função que calcula a área de quadrado
def calculateSquareArea(lado1, lado2):
    area = lado1 * lado2
    return area
'''
#Exemplo1: chamar a função
area1 = calculateTrianglArea(100, 10)
print("A area do triângulo 1 é", area1)

#Exemplo2: chamar a função novamente 
base = float(input('Digita a base: '))
altura = float(input('Digita a altura: '))
area2 = calculateTrianglArea(base, altura)
print("A area do triângulo 2 é", area2)
'''