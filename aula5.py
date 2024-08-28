lista_vendas = [1000, 500, 2500, 1300, 800]

meta = 1200
percentual_bonus = 0.1 

for venda in lista_vendas:
    if venda >= meta:
        bonus = percentual_bonus * venda
    else:
        bonus = 0

    print(bonus)


# for i in range(10): #contador
   # print ("vá estudar")

# for item in lista_vendas:
   # print(item)
   # print("próximo item")
    #tudo o que você quer que seja executado várias vezes
