idade_humana = int(input("Digite a idade humana do pet: "))
idade_cachorro = idade_humana * 7
print(f"A idade do pet em anos de cachorro é: {idade_cachorro}")

porte = input("Porte do cachorro (grande, medio, pequeno): ").lower()
banhos = int(input("Quantidade de banhos em 12 meses: "))

if porte == "grande":
    valor, custo = 75, 20
elif porte == "medio":
    valor, custo = 60, 15
elif porte == "pequeno":
    valor, custo = 50, 5
else:
    print("Porte inválido!")
    exit()

lucro_por_banho = valor - custo
lucro_total = lucro_por_banho * banhos

print(f"Lucro por banho: R$ {lucro_por_banho:.2f}")
print(f"Lucro total em 12 meses ({banhos} banhos): R$ {lucro_total:.2f}")