print("*****************************************")
print("*          CALCULO DE CALORIAS          *") 
print("*****************************************")

input("Pressione a tecla \'ENTER\' para iniciarmos: ")

i = 1
total = 0

quantidade_alimentos = int(input(("Digite a quantidade de alimentos que você ingeriu hoje: ")))

for x in range(0,quantidade_alimentos):
    x = float(input("Digite a quantidade de calorias do {}º alimento: ".format(i)))
    total = total + x
    i = i + 1

    
print("O total de calorias que você ingeriu hoje foi {} !".format(total))