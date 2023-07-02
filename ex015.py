dias = int(input('Digite quantos dias alugado:'))
km = float(input('Digite quantos Km rodado:'))
pago = (dias * 60) + (km * 0.15)
print('Valor a pagar é R$ {:.2f}'.format(pago))


