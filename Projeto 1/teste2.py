while True:
    try:
       valor=float(input('Digite o valor:'))
       break
    except:
        print('Por favor, digite um valor')
print('''
forma de pagamento
[1] Pagamentos à vista 
[2] Pagamento a prazo''')
while True:
    op=input('Opção:')
    if op=='1':
      novo_valor=0.9*valor
      print('Você teve desconto!!! ')
      break
    elif op=='2':
        print(op=='1')  
        novo_valor=1.08*valor 
        print('Você terá um porcentual de aumento!!!')
        break
    else:
        print('Por favor digite um valor valido')
      
print(f'O valor final é de: R${novo_valor:.2f}')        

            