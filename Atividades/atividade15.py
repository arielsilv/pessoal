salario_fix = int(input("informe o salario atual: "))
vendas = int(input("informe o valor das vendas: "))

comissao = vendas*4/100
salario_final = comissao+salario_fix

print("Comissão é igual á:", comissao)
print("salário final é igual á:",salario_final)