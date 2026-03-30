#soma dos números inteiros de 1 a 10, sem contar o 11
soma = 0
for num in range(1, 11):
    soma += num
    print("A soma dos números é: ", soma)

print("--------------------------")
# soma de 10 a 50
numeros = [10, 25, 1, 40, -4]
soma = 0
for num in numeros:
    soma += num
    print("A soma dos números é: ", soma)

print("--------------------------")
#quadrado de cada número
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    quadrado = num **2
    print(quadrado)

print("--------------------------")
#for para strings
# nome = input("digite seu nome: ")
# for letra in nome:
#     print(letra)

print("--------------------------")
# listas de palavras
for palavra in ["casa", "amor", "árvore", "abacaxi"]:
    if 'r' in palavra:
        print(palavra)

print("--------------------------")
#filtrando números pares
for num in range(1, 21):
    if num % 2 == 0:
        print(num, "é um número par")

print("--------------------------")


#loop while (enquanto)
i = 1
while i <= 1000:
    print(i)
    i = i + 1
print("--------------------------")

#soma de 1 a 10
i = 1
soma = 0
while i <= 10:
    soma += i
    print(soma)

    i += 1
print("--------------------------")

#teste de senha
# senha = ""
# while senha != "12345":
#     senha = input("digite a senha: ")
#     print("Acesso permitido!")
#     break
# print("--------------------------")

#menu com while
opcao = ''
while opcao != "s":
    print("Menu:")
    print("a. Opção 1")
    print("b. Opção 2")
    print("c. Opção 3")
    print("s. Sair")

    opcao = input("Digite uma opção: ")
    if opcao == 'a':
        print("opção 1 selecionada")
    elif opcao == 'b':
        print("opção 2 selecionada")
    elif opcao == 'c':
        print("opção 3 selecionada")
    elif opcao == 's':
        print("Saindo...")
    else:
        print("Opção inválida!")
print("--------------------------")


