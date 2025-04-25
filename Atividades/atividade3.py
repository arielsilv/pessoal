hora_n = int(input("Quantas horas normais o trabalhador trabalhou? "))
hora_e = int(input("Quantas horas extras o trabalhador trabalhou? "))

hora_normais = hora_n * 10
hora_extra = hora_e * 15

dinheiro_bruto = hora_normais + hora_extra

dinheiro_liquido1 = 10*dinheiro_bruto/100
dinheiro_liquido2 = dinheiro_bruto - dinheiro_liquido1

print("O dinheiro bruto desse trabalhador é igual á ", dinheiro_bruto)
print("O dinheiro liquido desse trabalhador é igual á ", dinheiro_liquido2 )