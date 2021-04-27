print("*****************************************")
print("*      QUANTIDADE DE TRANSAÇÕES         *") 
print("*****************************************")

input("Pressione a tecla \'ENTER\' para iniciarmos: ")

transacoes = int(input("\nDigite quantas transações financeiras você realizou ao longo de um dia: "))

i = 1
total = 0
soma = 0

while i <= transacoes:
    soma = float(input("\nDigite o valor da {}º transação realizada: ".format(i)))
    total = total + soma
    i = i +1

media = total/transacoes

print("\nVocê realizou {} tranzações, o total gasto foi R${:.2f}, e a sua média de gasto é de R${:.2f}".format(transacoes, total, media))

