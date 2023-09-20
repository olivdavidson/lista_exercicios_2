salario = float(input('Informe seu salário para realizarmos a análise do Empréstimo: '))
prest = float(input('Informe o valor da parcela que gostaria de pagar mensalmente: '))
if prest > salario * 0.2:
    print('Emprestimo concedido!')
else:
    print('Empréstimo não concedido!')
        