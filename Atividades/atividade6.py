lata =int(input("Quantas latas você deseja?"))
garrafa_p = int(input("Quantas garrafas pequenas você deseja?"))
garrafa_g = int(input("Quantas garrafas grandes você deseja?"))

lata_ml = lata*350
garrafa_p_ml = garrafa_p*600
garrafa_g_ml = garrafa_g*2000

total_ml = lata_ml + garrafa_p_ml + garrafa_g_ml

print("O total em ML que voce deseja é igual á:",total_ml,"ML de refrigerante")