primos = []

print("\nPor gentileza, entre com 5 valores inteiros para receber o MMC e o MDC: \n")
# leia o valor de n
n1 = int(input('Digite o valor de n1: '))
n2 = int(input('Digite o valor de n2: '))
n3 = int(input('Digite o valor de n3: '))
n4 = int(input('Digite o valor de n4: '))
n5 = int(input('Digite o valor de n5: '))


#Realização dos cálculos matemáticos
#MDC
mdc = n1
while n1 % mdc != 0 or n2 % mdc != 0 or n3 % mdc != 0 or n4 % mdc != 0 or n5 % mdc != 0: 
    mdc = mdc - 1

#MMC
m = 0
for m in range (1,n1*n2*n3*n4*n5 +1):
    if m%n1 == 0 and m%n2 == 0 and m%n3 == 0 and m%n4 ==0 and m%n5 == 0:
        break


#item a)
if n1 > 0 and n1 <=10000 and n2 > 0 and n2 <=10000 and n3 > 0 and n3 <=10000 and n4 > 0 and n4 <=10000 and n5 > 0 and n5 <=10000:  
    print("Entrada: %d,%d,%d,%d,%d" %(n1,n2,n3,n4,n5))
    print("Saída: mmc =",m, "mdc = %d" %(mdc))

#Item b)
if n1 > 10000 or n2 > 10000 or n3 > 10000 or n4 > 10000 or n5 > 10000:
    print('Entrada: {},{},{},{},{}.'.format(n1,n2,n3,n4,n5))
    print('Meu programa não é obrigado a calcular isso.')

#Item d
if n1 < 0 or n2 < 0 or n3 < 0 or n4 < 0 or n5 < 0:
    print("Entrada: %d,%d,%d,%d,%d" %(n1,n2,n3,n4,n5))
    print('Não é possível calcular m.m.c e o m.d.c com os números fornecidos.')

#item c)
if n1%2==1:
    primos.append(n1)
if n2%2==1:
    primos.append(n2)
if n3%2==1:
    primos.append(n3)
if n4%2==1:
    primos.append(n4)
if n5%2==1:
    primos.append(n5)
    print(f'\nEntrada tipo 1: {n1},{n2},{n3},{n4},{n5}.')
    print('Saída tipo 1: Os números primos são =', primos)
else:
    print(f'\nEntrada tipo 2: {n1},{n2},{n3},{n4},{n5}.')
    print("Saída tipo 2: Nenhum número lido é primo.")

