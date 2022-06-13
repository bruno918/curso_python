tabuada=int(input("digite um numero para fazer a tabuada"))
print("tabuada do ", tabuada)
for multiplicacao in range(1,11,1):
        print(str(multiplicacao) + " x " + str(tabuada) +  ' = ' +  str(tabuada*multiplicacao))
