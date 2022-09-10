'''- Escreva um programa para ler o ano de nascimento de uma pessoa, o programa deverá
informar para o usuário se ele poderá votar este ano. (não é necessário considerar o mês em
que a pessoa nasceu). Além disto, considere as seguintes informações:
• Jovens que completarem 18 anos até a data da eleição entram no grupo de eleitores
obrigatórios.
• O voto é facultativo entre os 16 e 17 anos e acima dos 70
'''

anoPessoa = int(input("Digite o ano que você nasceu (formato: XXXX): "))
ANOATUAL = 2022
idade = ANOATUAL - anoPessoa

if idade >= 18 and idade <= 70:
    print("Você deve votar esse ano")
elif idade >= 16 or idade >= 70:
    print("Você pode votar esse ano, mas não é obrigatório para sua idade")
else:
    print("Você não pode votar, vá assistir os desenhos!")