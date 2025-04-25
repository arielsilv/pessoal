numero = int(input("Digite um número: "))

for multiplicador in range(1, 11):
  produto = numero * multiplicador
  print(f"{numero} x {multiplicador} = {produto}")