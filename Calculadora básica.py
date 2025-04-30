numero = int(input('Informe um número:'))
numero2 = int(input('Informe outro número:'))
operação = input('Escolha uma operação matemática:')

if operação == '+':
    resultado = numero + numero2
    print(f'O resultado é {resultado}.')

elif operação == '-':
    resultado = numero - numero2
    print(f'O resultado é {resultado}.')

elif operação == '*':
    resultado = numero * numero2
    print(f'O resultado é {resultado}.')

elif operação == '/':
    if numero2 != 0:
        resultado = numero / numero2
        print(f'O resultado é {resultado}.')
    else:
        print('Erro: não é possível dividir por zero.')

else:
    print('Operação inválida. Tente novamente.')