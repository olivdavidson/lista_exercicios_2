#nota1=int(input("Digite a primeira nota: "))
#nota2=int(input("Digite a segunda nota: "))
while True:
    try:
        n1 = int(input('Informe a primeira nota: '))
        if 0 <= n1 <= 10:
            break
        print('A nota deve ser um valor válido!')
        exit()
    except ValueError:
        print('Não foi digitado uma nota!')
while True:
    try:
        n2 = int(input('Informe a segunda nota: '))
        if 0 <= n2 <= 10:
            break
        print('A nota deve ser um valor válido!')
        exit()
    except ValueError:
        print('Não foi digitado uma nota!')
media = (n1+n2)/2
print('A média das notas informadas é: ',media)