qnt_casas_construir = int(input("Quantas casas serão construídas? "))

metragem_padrao_casa = int(input("Quantos m2 tem cada casa do seu projeto?"))

preco_saco_cimento = float(input("Informe o valor do saco de cimento de 50kg: "))
print()

#• Quantidade total de m2 a serem construídos
metros_serem_construidos = metragem_padrao_casa * qnt_casas_construir
print(f"O total a ser construído é de {metros_serem_construidos} metros")

# A quantidade de sacos de cimentos a serem comprados
sacos_cimento_necessarios = metros_serem_construidos / 10

print(f"um total de {sacos_cimento_necessarios} sacos de cimento necessitam serem comprados")

#valor gasto com cimento
valor_gasto_cimento = sacos_cimento_necessarios * preco_saco_cimento

print(f"O total gasto com cimento é de {valor_gasto_cimento} reais")