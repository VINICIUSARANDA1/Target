ntermos = int(input("Que termo deseja encontrar: "))

n1, n2 = 0, 1 
contador = 0

print ("Sequência de Fibonacci")
print ('-'*30)

while contador < ntermos:
    print(n1)
    n = n1 + n2
    n1 = n2
    n2 = n
    contador += 1
    
    print(" Pertencente a sequência de Fibonacci")