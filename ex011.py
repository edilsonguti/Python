larg = float (input('Digite a largura da parede:'))
alt = float(input('Digite a altura da parede:'))
area = larg * alt
tinta = area / 2
print ('Sua parede tem a dimensão de {} x {} e a sua área é de {} m².' .format(larg, alt, area))
print('Para pintar a sua parede, voçê precisrá de {} litros de tinta.'.format(tinta))

