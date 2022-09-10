
SENHA1 = "3456"
SENHA2 = "1234"
numEscolhido = input("Digite uma senha de 4 dígitos: ")
if len(numEscolhido) < 4 or len(numEscolhido) > 4:
    print("A senha deve ter 4 dígitos")
else:
    if numEscolhido == SENHA1 or numEscolhido == SENHA2:
        print("Acesso permitido")
    else:
        print("Acesso negado")
