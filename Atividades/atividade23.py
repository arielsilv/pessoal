ano_nasc = float(input("digite o ano nascimento: "))
ano_atual = float(input("digite o ano atual: "))
idade = ano_atual-ano_nasc
ano = idade*365
mes = ano*12
semana = mes/7
dia = mes*30

print("Você já viveu", idade, "Anos")
print("Você já viveu", mes, " Meses")
print("Você já viveu", semana, " Semanas")
print("Você já viveu", dia, " Dias")