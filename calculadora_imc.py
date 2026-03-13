
#calculadora imc
#imc = peso / (altura)^2
#peso 70kg, altura 1.75cm

print("******** calculadora de imc ********")

altura = 1.75
peso = 70
calculo_imc = peso / (altura ** 2)

print(f"peso: {peso}kg, altura: {altura}cm")
print(f"imc total: {calculo_imc:.2f}") #.2f formata para 2 casas decimais
# outra forma: print("seu imc é : ", round(calculo_imc, 2))
print("______________________________")