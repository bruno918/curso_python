nome=input("Digite o nome: ")
idade=int(input('Digite a idade da pessoa: '))
doenca_inf=input("Possui suspeita de doença infectocontagiosa: ").upper()
if idade>=65:
    print("O paciente" + nome + " possui atendimento prioritario.")
elif doenca_inf=="SIM":
    print("O paciente" + nome + 'deve ser direcionado a sala prioritaria.')
else:
    print("O paciente" + nome + "não possui atendimento prioritario e pode esperar na sala comum")

