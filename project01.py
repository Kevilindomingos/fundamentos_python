#primeiro contato com o python

print("Hello World!")

print("teste soma: ", 2 + 3)
print("teste subtração: ", 10 - 4)
print("teste multiplicação: ", 6 * 7)
print("teste divisão: ", 15 / 3)

print("python")
print("python " + "é legal")
print("python " * 3)
print(len("python")) #leitura de caracteres da palavra

#diferentes tipos de dados em py

print(type(42))
print(type("python"))
print(type(3.14))
print(type(True))

#operações básicas com texto

nome = "maria"
sobrenome = "silva"
nome_completo = nome + " " + sobrenome
print("nome: ", nome)
print("sobrenome: ", sobrenome)
print("nome completo: ", nome_completo)
print("total de caracteres: ", len(nome_completo))
print("___________________________________________")

#funções built-in
#trabalhando com números

print(abs(-15)) #retorna o valor absoluto
print(round(3.14159, 2)) #redonda para 2 casas decimais
print(max(10, 25, 5, 30)) #encontra o maior valor
print(min(10, 25, 5, 30)) #encontra o menor valor
print(sum([1, 2, 3, 4, 5])) #soma todos os valores da lista


#trabalhando com strings
print("python".upper()) #tranforma o texto em maiusculas
print("PYTHON".lower()) #transforma o texto em minusculas
print("  espaços  ".strip()) #remove os espaços brancos
print("Olá mundo".replace("mundo", "python")) #substitui uma parte do texto por outra
