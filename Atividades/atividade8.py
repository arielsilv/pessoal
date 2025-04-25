altura = float(input("Digite a sua altura em metros: "))
sombra_predio = float(input("Digite a sombra do prédio em metros: "))

sombra_pessoa = altura * 1.5

altura_predio = (altura * sombra_predio) / sombra_pessoa

print("A altura do prédio em metros é:", altura_predio)