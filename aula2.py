faturamento = 1200
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento

print(f"Faturamento da empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}")

email_cliente = "karlarenata692@gmail.com"

# maiuscula 
email_cliente = email_cliente.upper()
print(email_cliente)
#minuscula 
email_cliente = email_cliente.lower()
print(email_cliente)

# "@"
print(email_cliente.find("@")) # -1 quando não encontrar

# tamanho do texto
print(len(email_cliente))

# pegar um caractere
print(email_cliente[4])

# pegar um pedaço do texto 
print(email_cliente[1:4])

# trocar um pedaço do texto 
novo_email = email_cliente.replace("gmail.com", "hotmail.com")
print(novo_email)

nome = "karla renata"

print(nome.capitalize()) #deixa apenas a primeira letra maiuscula
print(nome.title()) # deixa a letra de cada palavra maiuscula


# pegar servidor do email
posicao_arroba = email_cliente.find("@") + 1 
servidor = email_cliente[posicao_arroba:]
print(servidor)

# pegar 1 nome 
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]

# pegar sobrenome
sobrenome = nome[posicao_espaco+1:] 
print(primeiro_nome)
print(sobrenome)

#casos especiais - formatações numericas em textos
margem_lucro = round(margem_lucro, 2)
print(f"Faturamento da empresa: R${faturamento:.2f}, Custo: R$ {custo:.2f}, Lucro: R$ {lucro:.2f}, Margem: {margem_lucro:.0%}")
