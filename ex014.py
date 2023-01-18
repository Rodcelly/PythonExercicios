# Informe a temperatura em graus Celsius, e converta para Fahrenheit #

c = float(input('Qual a temperatura em °C? '))
f = ((c * 9)/5) + 32
print('A temperatura esta {:.1f}°F Fahrenheit.'.format(f))
