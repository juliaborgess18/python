n = int(input("N: Digite um número maior que 0 e menor que 10.000: ")) #distância entre os Palantir
while(n <= 0 or n >=10000): #Para garantir que o número digitado em N seja maior que 0 e menor que 10.000
    n = int(input("Digite um número maior que 0 e menor que 10.000: "))

x = int(input("X: Digite um número maior que 0 e menor que 100: ")) #diâmetro do Palantír de Sauron
while(x <=0 or x >=100): #Para garantir que o número digitado em X seja menor que 0
    x = int(input("Digite um número maior que 0 e menor que 100: "))

y = int(input("Y: Digite um número maior que 0 e menor que 100: ")) #diâmetro do Palantír de Saruman
while(y <=0 or y >=100): #Para garantir que o número digitado em Y seja menor que 100
    y = int(input("Digite um número maior que 0 e menor que 100: "))

saida = n / (x + y)

print(f"Saída: {saida: .2f}")
