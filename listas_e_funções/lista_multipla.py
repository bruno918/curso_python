
equipamento = []
valores = []
serials=[]
resposta = 'S'
while resposta == 'S':
    equipamento.append(input(' Equipamento: '))
    valores.append(float(input('valor do equipamento: ')))
    serials.append(int(input('Codigo de série: ')))
    resposta=input('digite para continuar ').upper()

busca = input('o que deseja buscar?')
for listas in range(0, len(equipamento)):
    if busca==equipamento[listas]:
         print('nome : ', equipamento[listas])
         print('valor: ', valores[listas])