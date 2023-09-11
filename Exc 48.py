sm = float(input("\nentre com o salario minimo "))
qtdade = float(input("\nentre com a quantidade em KW"))
preco = sm /700
vp = preco * qtdade
vd = vp * 0.9
print("\no preço do quilowatt: ", preco, "\nvalor a ser pago: ", vp,"\nvalor do desconto: ", vd)
print("\n")