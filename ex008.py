medida = float (input('Digite aqui a distancia em metros:'))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000

print('Valor convertido em Kilometros é {}Km'.format(km))
print('Valor convertido em hectometro é {}hm'.format(hm))
print('Valor convertido em decametro é {}dam'.format(dam))
print('Valor convertido em decimetro é {:.0f}dm'.format(dm))
print('Valor convertido em centimetro é {:.0f}cm'.format(cm))
print('Valor convertido em milimetro é {:.0f}mm'.format(mm))

