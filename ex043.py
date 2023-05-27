p = float(input('Qual o seu peso? (Kg) '))
a = float(input('Qual sua altura? (m) '))
imc = p / (a ** 2)
print('O IMC dessa pessoa é {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc >= 18.5 < 25:
    print('PARABÉNS! Você está em peso NORMAL')
elif imc >= 25 < 30:
    print('Você está ACIMA DO PESO')
elif imc >= 30 < 40:
    print('Vocêstá em OBESIDADE')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA')
