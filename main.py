# Função para calcular digito verificador(DAC) e digito vericador gerel (DAC Geral)

def barrasDV(boxe):
    somaBox1 = 0
    somaBox2 = 0
    somaTotal = 0
    lista = ''
    soma = 0
    soma1 = 0
    numero = 0
    somaTotal = 0

    boxNum1 = boxe[0::2]
    boxNum2 = boxe[1::2]

    if int(len(boxe)) == 12:
        boxNum1 = boxe[0:11:2]
        boxNum2 = boxe[1:11:2]

    for i in boxNum1:
        numero = (int(i) * 2)
        if numero >= 10:
            lista += str(numero)
        else:
            soma += numero

    for i in lista:
        soma1 += int(i)

    somaBox1 = soma1 + soma

    for i in boxNum2:
        somaBox2 += int(i)

    somaTotal = 10 - ((somaBox1 + somaBox2) % 10)

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

    pag = 0 # variavel para calcular a quantidade de box certos escritos

    print("-" * 31)
    print("        contas e tributos       ")
    print("   Água,luz,Telefone,IPTU,ISS   ")
    print("-" * 31)
    print("1) Pagamento c/Código de barras ")
    print("2) Imprimir 2ª via de boleto    ")
    print("3) Sair")
    opcao = int(input("Digite a opção desejada?: "))

    # Opção 1 Validar código DAC

    if opcao == 1:

        print("Digite os 4 boxes a seguir...")

        # Estrutura de repetição para ler os 4 box e validar o DAC

        for i in range(1,5):

            pag += 1 # A cada box certo vai somar 1 se o pag = 4 o pagamento foi efetuado

            boxe = str(input(f"Digite o BOXE-{i}: ").format())

            boxLimpo = limpaBox(boxe) # Limpando caracters especias

            # Verificando se box do codigo de barra tem 12 números senão encerra o programa

            if len(boxLimpo) != 12:
                print("DIGITO VERIFICADOR INVÁLIDO!!!!!")
                enter = input("Presione ENTER para continuar: ")
                break

            # Verificando se o DAC e igual ao DAC digitadado

            if barrasDV(boxLimpo) != int(boxLimpo[11]):
                print("DIGÍTO VERIFICARDOR INVÁLIDO!!!!!")
                enter = input("Presione ENTER para continuar: ")
                break

            # Se a quantidade codigos de barras for = 4 o pagamento foi efetuado

            if pag == 4:
                print("PAGAMENTO EFETUADO COM SUCESSO!!!!!")
                enter = input("Presione ENTER para continuar: ")

    # Opção 2 Receber dados do usuario Calcular o DAC geral e depois calcular o DAC individual de cada box de acordo com o modelo proposto no exercecio e escrever o codigo de barras

    elif opcao == 2:

        valorZero = ''
        sequeZero = ''

        codigo  = str(input("Código: "))
        valor   = str(input("Valor da Fatura: "))
        id      = str(input("Identificação da Empresa: "))
        unidade = str(input("Unidade Consumidora: "))
        data    = str(input("Ano-Mês (AAAMMM): "))
        seque   = str(input("Sequencial: "))

        sequeLimpo = limpaBox(seque) # limpando os caracters especias
        valorLimpo = limpaBox(valor) # limpando os caracters especias

        # Estruturas de repetição para calcular a quantidade de 0 a esquerdas de acordo com o modelo proposto no exercicio

        while len(valorLimpo) < 11:
            valorLimpo += '0'
            valorZero += '0'

        while len(sequeLimpo) < 7:
            sequeLimpo += '0'
            sequeZero += '0'

        somaBarras = codigo + valor + id +unidade + data + seque # somando todos os valores recebidos

        if len(somaBarras) == 43 : # Solução encontrada para caso o boleto seja de outra empresa e o usuario saiba todos os 43 caracters para gerar a segunda via
            barraSujo = codigo + valor + id + unidade + data + seque
        elif len(somaBarras) < 43:
            barraSujo = codigo + valorZero + valor + id + unidade + data + "9" + sequeZero + seque + "9" # Vai gerar o boleto de acordo com os critérios exigidos no exercicio 0 a esquerda e 9 como digito separador
        elif len(somaBarras) > 43: # Caso o número execeda 43 não será possivel gerar o código de barras
            barraSujo = ''

        barras = limpaBox(barraSujo) # limpando os caracters especias

        # Separando o codigo completo em box de 12 espaçõs para fazer o calculo do DAC

        box1 = barras[0:3:1] + str(barrasDV(barras)) + barras[3:10:1]
        box2 = barras[10:21:1]
        box3 = barras[21:32:1]
        box4 = barras[32:43:1]

        codigoCompleto = box1 + '-' + str(barrasDV(box1)) + " " + box2 + '-' + str(barrasDV(box2)) + " " + box3 + '-' + str(barrasDV(box3)) + " " + box4 + '-' + str(barrasDV(box4)) # gerando o codigo completo

        # escrevando o codigo de barras completo com 48 caracters, foi usado 55 como parametro por que durante a soma eu coloquei caracters como '-' ' ' caso não contenham o programa e finalizado

        if int(len(codigoCompleto)) == 55:
            print("-" * 31)
            print("Segunda Via do Seu Boleto é:")
            print(codigoCompleto)
            enter = input("Presione ENTER para continuar: ")
        else:
            print("CÓDIGOS DE BARRAS IMCOMPLETO!!!!!")
            enter = input("Presione ENTER para continuar: ")

    # Opção 3 encerrando o programa

    elif opcao == 3:
        break

    # Caso a opção não seja 1,2 ou 3 programa fica em loop

    elif opcao >= 4 or opcao <= 0:
        print("-" * 31)
        print("         Opção invalida         ")