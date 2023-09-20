#cont = 0
#lista_num = []
#while cont != 2:
#    numero = int(input('Informe um número: '))
#    lista_num.append(numero)
#    cont = cont + 1
#soma = sum(lista_num)
#print('O maior número informado é ',max(lista_num))
num1=int(input("Digite o primeiro valor: "))
num2=int(input("Digite o segundo valor: "))
if num1 > num2 :
    print('O maior número é ', num1,'e a diferença entre os valores é ', num1-num2)
else:
    print('O maior número informado é ', num2,'e a diferença entre ambos é ',num2 - num1)