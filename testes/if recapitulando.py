nome=input('digite seu nome: ')
idade=int(input('sua idade: '))
doeca=input('voce possui doença infecciosa?').upper()

if idade >= 65:
    print('com urgencia')
elif doeca =='SIM':
    print('ultra urgente')
else:
    print('sem urgencia')
