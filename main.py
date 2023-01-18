
# Calculo de IMC - Indice de Massa Corporal

altura = float(input('Qual é a altura em cm:'))
peso = float(input('Qual é o peso em kg:'))

Imc = peso / (altura/100)**2

if Imc < 18.5:
     print('Magreza')
elif Imc >= 18.5 and Imc < 24.9: 
     print('Normal')

elif Imc >= 25.0 and Imc < 29.9:
     print('Sobrepeso')

elif Imc >= 30.0 and Imc < 39.9:
   print('Obesidade')

elif Imc >= 40.0:
   print('Obesidade grave')

else:
  print('morte')