# analisa notas

# 8.5, 7.0, 9.5, 6.0, 8.0, 7.5, 9.0

notas = [8.5, 7.0, 9.5, 6.0, 8.0, 7.5, 9.0]
maior_nota = max(notas)
menor_nota = min(notas)
media_notas = sum(notas) / len(notas)

#soma notas maiores que 8.0
soma_notas = [nota for nota in notas if nota > 8.0]
quantidade_notas = len(soma_notas)


print(" ======= SISTEMA NOTAS =======")
print(f" ======== Total notas: ========\n{notas}")
print("======================================")
print(f"Sua maior nota foi: {maior_nota}")
print(f"Sua menor nota foi: {menor_nota}")
print(f"A média geral das notas é: {media_notas:.1f}")
print(f"Notas maiores que 8.0: {soma_notas}")
print("======================================")