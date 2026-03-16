#simulador conta bancária

print("============ CONTA BANCÁRIA ============")
saldo = 1000.0
historico = []
print(f"Saldo inicial: R${saldo:.2f}")

#depósito
deposito = 500.0

saldo += deposito
historico.append(f"Depósito: +R$ {deposito:.2f}")
print(f"Depósito de R$ {deposito:.2f} realizado")

#saque
saque = 200.0

if saque <= saldo:
    saldo -= saque
    historico.append(f"Saque: -R$ {saque:.2f}")
    print(f"Saque de R$ {saque:.2f} realizado")
else:
    print(f"Saldo insuficiente para saque!")

#consulta
historico.append(f"Consulta: Saldo R$ {saldo:.2f}")
print(f"Saldo atual: R$ {saldo:.2f}")
print("========================================")

#Mostrando histórico
print("\n=== Histórico (últimas 3 operações) ===")
for i, operacao in enumerate(historico[-3:], 1):
    print(f"{i}. {operacao}")
print("========================================")