faturamento = 1200 # tipo: int -> numero inteiro
custo = 750.0 # tipo: float -> numero com casa decimal

imposto = faturamento * 0.1
lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento

print("Faturamento foi de", faturamento)
print("O custo foi de", custo)
print("O lucro foi de", lucro)
print("A margem de lucro foi de", round(margem_lucro, 2))

mensagem = "O faturamento foi de ..." # tipo: string -> texto

teve_lucro = True #tipo: boolean 

# Mod -> % significa resto da divisão
print(10 % 3)

tempo_contrato = 170
tempo_anos = 170 / 12
print("Tempo em anos", int(tempo_anos))
tempo_meses = 170 % 12
print("Tempo em meses", tempo_meses)