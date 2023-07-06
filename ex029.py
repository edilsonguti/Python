velocidade = float(input('Qual é a velocidade atual do veiculo? '))
if velocidade > 80:
    print('MULTADO! Voçê excedeu o limite de velocidade permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

