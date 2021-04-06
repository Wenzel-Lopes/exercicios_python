print('********************************')
print('* PORCETAGEM SOBRE FATURAMENTO *')
print('********************************')

input('Pressione \'ENTER\' para iniciarmos: ')

print('\nTabela de assinaturas: ')
print('\n|  Tipo Assinatura  |  Porcetagem sobre faturamento |')
print('|      Basic        |              30%              |')
print('|      Silver       |              20%              |')
print('|      Gold         |              10%              |')
print('|      Platinium    |               5%              |')

assinatura = input('Digite o tipo da sua assinatura: ').upper()
faturamento = float(input('Digite o faturamento do canal ao longo do ano: R$'))

if assinatura == 'BASIC':
    faturamentoB = faturamento * 30 / 100
    print('\nValor a ser pago pela prestação do serviço Basic é: R${:.2f}'.format(faturamentoB))
elif assinatura == 'SILVER':
    faturamentoS = faturamento * 20 / 100
    print('\nValor a ser pago pela prestação do serviço Silver é: R${:.2f}'.format(faturamentoS))
elif assinatura == 'GOLD':
    faturamentoG = faturamento * 10 / 100
    print('\nValor a ser pago pela prestação do serviço Gold é: R${:.2f}'.format(faturamentoG))
elif assinatura == 'PLATINIUM':
    faturamentoP = faturamento * 5 / 100
    print('\nValor a ser pago pela prestação do serviço Platinium é: R${:.2f}'.format(faturamentoP))
else:
    print('\nOps! Erro de digitação: Por favor digite o tipo de assinatura corretamente.')
    




