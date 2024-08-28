lista_precos = [1500, 1000, 800, 3000]

#imposto
#aliquota - Imposto de Renda = 0.2 se o preço do protudo for ate 2000, acima disso a aliquota é 0.3
#aliquota - ISS = 0.15
#aliquota - CSLL= 0.05

def calcula_imposto_total(preco):
    if preco <= 2000:
        imposto_ir = 0.2 * preco 
    else:
        imposto_ir = 0.3 * preco
    imposto_iss = 0.15 * preco
    imposto_csll = 0.05 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    return imposto_total

for preco in lista_precos:
    imposto_total = calcula_imposto_total(preco)
    print(f"Imposto total sobre o produto de R$ {preco}: R${imposto_total}")

nova_lista_produto = [3000, 5000, 2500, 10000]

for preco in  nova_lista_produto:
    imposto_total = calcula_imposto_total(preco)
    print(f"Imposto total sobre o produto de R$ {preco}: R${imposto_total}")