n1 = int(input('Digite o Primeiro Valor: '))
n2 = int(input('Digite o Segundo Valor:'))
opção = 0
while opção != 5:
    print('''
    [1] Somar
    [2] Multiplicar 
    [3] Maior
    [4] Novos Números
    [5] Sair
    [6] Dividir
    ''')
    opção = int(input('Qual é a sua opção:'))
    if opção == 1:
       soma = n1 + n2
       print('Soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção ==2:
         produto = n1 * n2
         print('O resultado de {} * {} é {}'.format(n1 , n2, produto))
    elif opção ==3:
         if n1 > n2:
             maior = n1
         else:maior = n2
         print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção ==4:
         print('informe os numeros novamente: ')
         n1 = int(input('Primeiro Valor '))
         n2 =  int(input('Segundo Valor'))

    elif opção ==6:
         Dividir = n1 / n2
         print('O resultado é {} é {} e {}'.format(n1, n2, Dividir))

    elif opção ==5:
        print('Finalizar ')

    else:
        print("Opeção invalida, tente nova mente ")
    print('=-=' *10)
print("Fim do Programa Volte Sempre")