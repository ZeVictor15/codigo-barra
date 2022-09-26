# Importando biblioteca para gerar codigo de barras
from barcode import EAN13

# Importando biblioteca para salvar codigo de barras em PNG

from barcode.writer import ImageWriter

# Importanto biblioteca random para salvar os arquivos com nome diferentes é numeros aleatorios
import random

# Função para calcular digito verificador(DAC)

def barrasDV(boxe):
    somaBox1 = 0
    somaBox2 = 0
    somaTotal = 0
    somaTotal = 0
    divInteira = ''

    boxNum1 = boxe[0:12:2]
    boxNum2 = boxe[1:12:2]

    for i in boxNum1:
        somaBox1 += int(i)

    for i in boxNum2:
        somaBox2 += (int(i) * 3)

    somaTotal= (10*(1 + ((somaBox1 + somaBox2) // 10))) - (somaBox1 + somaBox2)

    if somaTotal >= 10:
        somaTotal = 0

    return somaTotal

# Função para limpar caracters especias como '.' ',' '+' etc...

def limpaBox(boxe):
    boxLimpo = ''
    for i in boxe:
        if i.isalnum():
            boxLimpo += i
    return boxLimpo

# estrutura de repetição para gerar o menu

while True:

    # Menu

    print("-" * 31)
    print("        VAREJOS S/A      ")
    print("  Código GTIN-13/UCP/EAN13  ")
    print("-" * 31)
    print("1) Validar código GTIN-13 ")
    print("2) Indentificar País   ")
    print("3) Sair")
    opcao = int(input("Digite a opção desejada?: "))

    # Opção 1 Validar código GTIN-13

    if opcao == 1:
        print("Validar Código ")
        codigo = str(input("Digite o código de 13 digitos: "))

        codigoLimpo = limpaBox(codigo) # Limpando caracters especias

        # Verificando se o codigo de barras contém não está faltando digitios

        if len(codigoLimpo) != 13:
            print("Código GTIN-13 não possui 13 dígitos: ")
            enter = input("aperte ENTER para continuar: ")

        else:

            if barrasDV(codigoLimpo) == int(codigoLimpo[12]): # Verificando o DAC

                aleatorio = random.random()  # usando random para dar um nome aleatoria ao arquivo de codigo de barras
                print(f"Digito verificador valido: {barrasDV(codigoLimpo)} ".format())

                codigoBarra = EAN13(codigoLimpo,writer=ImageWriter()) # Gerando arquivo de codigo de barras
                codigoBarra.save(f"codigo-barra{aleatorio}") # salvando arquivo

                print("Código de Barras Salvo")

                enter = input("aperte ENTER para continuar: ")

            else:
                print(f"Digito verificador invalido: {barrasDV(codigoLimpo)} ".format())
                enter = input("aperte ENTER para continuar: ")

    # Opção 2 indentificar o pais do codigo de barras

    elif opcao == 2:

        print("Indentificar pais ")
        codigo = str(input("Digite o código de 13 digitos: "))
        codigoLimpo = limpaBox(codigo)

        # Edentificando o codigo do país e escrevendo

        if int(codigoLimpo[0:3]) == 789 or int(codigoLimpo[0:3]) == 790:
            print(f"GTIN-13 origem BRASIL: {codigoLimpo[0:3]}".format())
            enter = input("aperte ENTER para continuar: ")

        elif int(codigoLimpo[0:3]) == 779:
            print(f"GTIN-13 origem ARGENTINA: {codigoLimpo[0:3]}".format())
            enter = input("aperte ENTER para continuar: ")

        elif int(codigoLimpo[0:3]) == 773:
            print(f"GTIN-13 origem URUGUAI: {codigoLimpo[0:3]}".format())
            enter = input("aperte ENTER para continuar: ")

        elif int(codigoLimpo[0:3]) == 780:
            print(f"GTIN-13 origem CHILE: {codigoLimpo[0:3]}".format())
            enter = input("aperte ENTER para continuar: ")

        elif int(codigoLimpo[0:3]) == 784:
            print(f"GTIN-13 origem PARAGUAI: {codigoLimpo[0:3]}".format())
            enter = input("aperte ENTER para continuar: ")

        elif int(codigoLimpo[0:3]) == 786:
            print(f"GTIN-13 origem EQUADOR: {codigoLimpo[0:3]}".format())
            enter = input("aperte ENTER para continuar: ")

        elif int(codigoLimpo[0:3]) == 770:
            print(f"GTIN-13 origem COLÔMBIA: {codigoLimpo[0:3]}".format())
            enter = input("aperte ENTER para continuar: ")

        elif int(codigoLimpo[0:3]) == 743:
            print(f"GTIN-13 origem NICARÁGUA: {codigoLimpo[0:3]}".format())
            enter = input("aperte ENTER para continuar: ")

        elif int(codigoLimpo[0:3]) == 600 or int(codigoLimpo[0:3]) == 601:
            print(f"GTIN-13 origem AFRÍCA DO SUL: {codigoLimpo[0:3]}".format())
            enter = input("aperte ENTER para continuar: ")

        else:
            print(f"VAREJOS S/A não vende para esse pais: {codigoLimpo[0:3]}".format())
            enter = input("aperte ENTER para continuar: ")

    # Opção 3 encerrando o programa

    elif opcao == 3:
        break

    # Caso a opção não seja 1,2 ou 3 programa fica em loop

    elif opcao >= 4 or opcao <= 0:
        print("-" * 31)
        print("         Opção invalida         ")
