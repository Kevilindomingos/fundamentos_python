#gerador de senha simples

nome = "João"
ano_nascimento = 2006
cidade = "Curitiba"

# gerador
primeira_letra = nome[0].upper()
ultimos_digitos = str(ano_nascimento)[-2:]
primeira_cidade = cidade.split()[0][:3]
numero_especial = len(nome) * len(cidade)

senha = primeira_letra + ultimos_digitos + primeira_cidade + str(numero_especial)

print("===============================")
print("** GERADOR DE SENHA SIMPLES **")
print(f"Nome: {nome}")
print(f"Ano: {ano_nascimento}")
print(f"Cidade: {cidade}")
print("===============================")
print(f"Senha gerada: {senha}")
print(f"Tamanho da senha: {len(senha)} caracteres")
print("===============================")
