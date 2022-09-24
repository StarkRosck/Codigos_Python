ordens = ['58552','4155','514','4455','741']

for ordem in ordens:
    if ordem[0]=='2':
       print(f'Ordem {ordem} - Chamado de Manutenção')
    elif ordem[0]=='3':
        print(f'Ordem {ordem} - Manutenção')
    else:
        print(f'Ordem {ordem} - Casos não atendido')