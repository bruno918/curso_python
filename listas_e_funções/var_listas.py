produto = []
marca = []
setor = []
codigo = []
valor = []
resposta = 'S'
while resposta == 'S':
  produto.append(input("Nome: "));
  marca.append(input('Médico: '))
  setor.append(input('Introdução: '))
  codigo.append(input('Urina: '))
  valor.append(float(input('valor')))
  resposta = input("Digite 'S' para continuar: ").upper()

for listas in range(0, len(produto)):
 print('Equipamento..: ', (listas + 1))
 print('Produto......: ', produto[listas])
 print('Marca........: ', marca[listas])
 print('Setor........: ', setor[listas]);
 print('Codigo serial: ', codigo[listas]);