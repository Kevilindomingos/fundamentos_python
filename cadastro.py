# sistema cadastro simples

nome_completo = "maria silva"
idade = 23
cidade = "Curitiba"
email = "maria.silva@gmail.com"

#valida idade
#insistance verifica se idade é um número inteiro
#and idade > 0 verifica se idade é positiva
idade_valida = isinstance(idade, int) and idade > 0

#calculos
ano_atual = 2030 - 2026
calculo_idade = idade + ano_atual

print("===========================")
print("*** FICHA DE CADASTRO ***")
print("===========================")
print(f"Nome completo: {nome_completo}")
print(f"Idade: {idade} anos")
print(f"Reside em: {cidade}")
print(f"E-mail: {email}")
print(f"Idade válida: {'sim' if idade_valida else 'não'}")  #operador ternário if else
print("*** IDADE 2030 ***")
print(f"Em 2030, você terá: {calculo_idade} anos.")
print("==============================")