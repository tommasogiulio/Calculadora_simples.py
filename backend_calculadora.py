print('-----INICIO-----')

numero1 = float(input('Digite o primeiro número: '))
operacao = input('Selecione a operação desejada:\nA)soma\nB)divisão\nC)multiplicação\nD)subtração\nE)Porcentagem\n').upper()
numero2 = float(input('Digite o segundo número: '))

if operacao == 'A':
    resultadosoma = numero1 + numero2
    print('O resultado da soma é: ', resultadosoma)

elif operacao == 'B':
    if numero2 != 0:
        resultadodivisao = numero1 / numero2
        print('O resultado da divisão é:', resultadodivisao)
    else: 
        print('Não é possível dividir um valor por 0')

elif operacao == 'C':
    resultadomulti = numero1 * numero2
    print('O resultado da multiplicação é:', resultadomulti)

elif operacao == 'D':
    resultadosub = numero1 - numero2
    print('O resultado da subtração é:', resultadosub)

elif operacao == 'E':
    resultadoporcent = (numero1 / 100) * numero2
    print('O resultado da porcentagem é: ', resultadoporcent) 

else:   
    print('A operação que você escolheu é inválida, o programa aceita apenas as opções !')