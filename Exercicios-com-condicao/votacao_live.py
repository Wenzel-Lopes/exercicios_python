print('****************************************')
print('*  VOTAÇÃO PARA DECIDIR O DIA DA LIVE  *')
print('****************************************')

input('Pressione a tecla \'ENTER\' para informar a quantidade de votos: ')

segunda = int(input('\nInforme a quantidade de votos na segunda-feira: '))
terça = int(input('Informe a quantidade de votos na terça-feira: '))
quarta = int(input('Informe a quantidade de votos na quarta-feira: '))
quinta = int(input('Informe a quantidade de votos na quinta-feira: '))
sexta = int(input('Informe a quantidade de votos na sexta-feira: '))

print('| RESULTADO DA VOTAÇÃO PARA DECIDIR O DIA DA LIVE: ')
print('| Segunda-feira............... ',segunda)
print('| Terça-feira................. ',terça  )
print('| Quarta-feira................ ',quarta)
print('| Quinta-feira................ ',quinta)
print('| Sexta-feira................. ',sexta )

if segunda > terça and segunda > quarta and segunda > quinta and segunda > sexta:
    print('\nO dia mais votado foi a Segunda-Feira com', segunda, 'votos. Esse será o dia da live!')
elif terça > segunda and terça > quarta and terça > quinta and terça > sexta:
    print('\nO dia mais votado foi a Terça-Feira com', terça, 'votos. Esse será o dia da live!' ) 
elif quarta > segunda and quarta > terça and quarta > quinta and quarta > sexta:
    print('\nO dia mais votado foi a Quarta-Feira com', quarta, 'votos. Esse será o dia da live!') 
elif quinta > segunda and quinta > terça and quinta > quarta and quinta > sexta:
    print('\nO dia mais votado foi a Quinta-Feira com', quinta, 'votos. Esse será o dia da live!')
elif sexta > segunda and sexta > terça and sexta > quarta and sexta > quinta:
    print('\nO dia mais votado foi a Sexta-Feira com', sexta, 'votos. Esse será o dia da live!')
else:
    print('\nHouve um empate, terá que fazer uma nova votação entre os dias empatados.')  





