nome ='Arthur'
sobrenome ='Stark '
list = ['Arthur', 'Pedro', 'João', 'Silvia','Lucas','545122','4452','4']

if nome:
    print('A variavel possui nome')
    print(nome)
else:
    print('A variavel não possui nome')
#vamos mostrar de onde essa variavel está procurando 
if sobrenome:
    print('A variavel 2 possui sobrenome ')
    print(sobrenome)
else:
    print('variavel 2 não possui sobrenome ')  
    #fazendo subprograma   
print('****************************************')
for ordem in list:
    if ordem[0]=='2':  
       print(f'tem na {ordem} o que preocura  ')
    elif ordem[0]=='2':
        print(f'Não tem essa base de dados de nomes {ordem}  ')
    else:
        print(f'Não tem essa base de dados de nomes {ordem} Repita o procedimento  ')