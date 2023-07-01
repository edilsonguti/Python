n = int (input('Digite um numero inteiro: '))
ant = n - 1
post = n + 1
print('Você digitou o valor {} seu antecessor é o {} e o seu sucessor é o {}!'.format(n, ant, post))



# Outra forma de fazer

n = int (input('Digite um numero inteiro: '))
print('Você digitou o valor {} seu antecessor é o {} e o seu sucessor é o {}!'.format(n, (n-1), (n+1)))
