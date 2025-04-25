
umCent = int(input("quantidade de Moedas de 1 centavo: "))
cincoCent = int(input("quantidade de Moedas de 5 centavos: "))
cincoCent = cincoCent*5
dezCent = int(input("quantidade de Moedas de 10 centavo: "))
dezCent = dezCent*10
vinte_cincoCent = int(input("quantidade de Moedas de 25 centavo: "))
vinte_cincoCent = vinte_cincoCent*25
cinquentaCent = int(input("quantidade de Moedas de 50 centavo: "))
cinquentaCent = cinquentaCent*50
umReal = int(input("quantidade de Moedas de 1 real: "))


tot_cent = (umCent + cincoCent + dezCent + vinte_cincoCent + cinquentaCent)/100

totReais = umReal + tot_cent

print("O total de dinheiro poupado foi RS ", totReais)