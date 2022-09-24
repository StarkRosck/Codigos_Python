#este programa usando uma estrutura pilha criptografia uma 
#mensagem ou decodigficar uma mensagem recebida 

from email import message
from inspect import stack
from pilhalista import pilha 

#****** subprogramas *****
#um subprograma como um menu
def abertura():
    print('*'*20)
    print("Bem-Vindo ao sistema de decodificação")
    print('*'*20)

#Um subprograma para entrada de uma mensagem 
#e inverter essa mensagem 
def mensagem():
    mensagem = input("Digite uma mensagem codificada:\n")
    #inverter a mensagem recebida 
    mensagemInversa = list(revered(message))
    return mensagemInversa
# Um subprograma para verificar as letras vogais 
def vogal(letra):
    if (letra == 'A'):
        return True
    elif (letra == 'E'):
        return True
    elif (letra == 'I'):
        return True
    elif (letra == 'O'):
        return True
    elif (letra == 'U'):
        return True
    elif (letra == 'a'):
        return True
    elif (letra == 'e'):
        return True
    elif (letra == 'i'):
        return True
    elif (letra == 'o'):
        return True
    elif (letra == 'u'):
        return True
    else:
        return False 
#Um subprograma para decodificar a mensagem recebida 
def decodificar(messagem):
    stack = pilha() #stack é objeto pilha 
    pilha = stack.recebeLista() #construindo uma estrutura pilha 
    #Uma lista para amarzenar uma mensagem decodificado 
    mDecodificado = list()
    cont = 0 #contador 

    #Processo de decodificação 
    while ( cont < len(mensagem)):
        if (vogal(message[cont])):
            mDecodificado.append(message[cont])
            cont += 1
        else: #caso não é vogal, usando pilha para inverter os caracteres 
            while (cont<len(message) and (not vogal(menssage[cont]))):
                stack.empilhar(Pilha,message[cont])
                cont += 1 
                #enquanto pilha não varia, desempilha 
                while (not stack.varia(pilha)):
                    mDecodificado.append(stack.desempilhar(Pilha))
    return mDecodificado     

# ******** programa principal *******
abertura()
message = mensagem()
maqSaida = "".join(decodificar(message))
print(f"\nMensagem decodificada:\n{magSaida} ")
input("Fim do Programa!")
