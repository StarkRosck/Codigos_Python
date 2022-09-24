print('*'*10)
print('Seja Bem-Vindo')
n1 = float(input('Digite o primeiro valor'))
n2 = float(input('Digete o Segundo Valor'))
opcao = 0
while opcao !=5: 
      print('''
      [1] soma 
      [2] dividir
      [3] multiplicar 
      [4] Novo Número 
      [5] Finalizar 
      ''')
      opcao = float(input('Escolha um Número '))
      if opcao == 1: 
        soma = n1 + n2 
        print('o valor será {} e {} é {}'.format(n1,n2,soma))
      elif opcao == 2:
        dividir = n1 / n2 
        print('o valor será {} e {} é {}'.format(n1,n2,dividir))
      elif opcao ==3:
        produto = n1 * n2
        print('o valor será {} e {} é {}'.format(n1,n2,produto))
      elif opcao == 5:
        print('sair ')
      elif opcao ==4: 
        print('entre com outro valor')
        n1 = float(input('Digite o primeiro valor'))
        n2 = float(input('Digete o Segundo Valor'))
      else:
        print("Fim do Programa")
   



