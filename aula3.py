# inputs 
email = input("Escreva seu e-mail: ")
nome = input("Seu primeiro nome: ")

print(nome, email)

print(f"{nome}, verifique seu email: {email} que enviamos um link de confirmação")

#faturamento = float(input("Escreva o faturamento: "))

#imposto = faturamento * 0.1
#print(imposto)
# listas 
vendas = [100, 50, 70, 20, 30, 700]

#soma dos elementos
total_vendas = sum(vendas)
print(total_vendas)

#tamanho da lista
quantidade_vendas = len(vendas)
print(quantidade_vendas)

# max e min

print(max(vendas))
print(min(vendas))

# pegar posição
print(vendas[0])

lista_produtos = ["iphone", "airpod", "ipad", "macbook"]

produto_procurado = input("Pesquise pelo nome do produto: ")
produto_procurado = produto_procurado.lower()

print(produto_procurado in lista_produtos)

# adicionar item
lista_produtos.append("apple watch")
print(lista_produtos)
# remover item
lista_produtos.remove("apple watch") # nome do item
print(lista_produtos)

lista_produtos.pop(0) # posição do item 
# editar item 

precos_produtos = [ 1000, 1500, 3000]
precos_produtos[0] = 6000

# contar quantas vezes um item aparece na lista

lista_produtos = ["iphone", "airpod", "ipad", "macbook"]
print(lista_produtos.count("iphone"))

# ordenar listas
lista_produtos.sort()

#lista_produtos.sort(reverse=True) <- ordena em ordem inversa 