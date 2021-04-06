print("*****************************************")
print("*    Algoritmo da sorte de Fibonnaci    *") 
print("*****************************************")

input("Pressione a tecla \'ENTER\' para iniciarmos: ")

penultimo = 0
ultimo = 1
i = 0

n = int(input("\nDigite um valor numérico inteiro: "))

while i < n:
    i = penultimo + ultimo
    penultimo = ultimo
    ultimo = i
#    print("{}".format(i))   

if n == i:
    print("\nAção bem sucedida!")
else:
    print("A ação falhou...")

