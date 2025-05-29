import matplotlib.pyplot as plt
import numpy as np

# variaveis globais
diasDaSemana = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
anoAtual = 2025
continuar = ['sim', 'não']

# Função para forçar o usuário a escolher uma opção válida de uma lista
def forcaOpcao(stg, listaOpcao):
    exibirOpcoes = '\n'.join((listaOpcao))
    opcao = input(f"{stg}\n{exibirOpcoes}\n")
    while not opcao in listaOpcao:
        opcao = input(f"{stg}\n")
    return opcao

# Função para garantir que o usuário digite uma string (não numérica)
def garanteString(stg):
    string = input(stg)
    while string.isnumeric():
        print("Inválido")
        string = input(stg)
    return string

# Função para calcular a média de valores inseridos pelo usuário para cada dia da semana
def calcularMedia(stg, array, stg1, medida):
    i = 0
    soma = 0
    while i < 7:
        informacao = garanteNumero(f"{stg} {i + 1}° dia da semana:")
        array.append(informacao)
        i += 1

    print("\n")

    for i in range(len(diasDaSemana)):
        print(f"{diasDaSemana[i]} {stg1} {array[i]} {medida}")
        soma += array[i]
    media = soma / len(array)
    print("\n")
    print(f"A media semanal {stg1} foi {int(media)} {medida}")

    return media

# Função para garantir que o usuário digite um número com quantidade de dígitos específica
def garanteNumero(stg,qtd):
    telefone = input(stg)
    if len(telefone) != qtd:
        telefone = garanteNumero(stg)
    else:
        while not telefone.isnumeric():
            telefone = garanteNumero()
        telefone = int(telefone)
    return telefone

# Função para calcular a média de um array e exibir os valores
def media(array, stg1, medida):
    soma = 0
    for i in range(len(array)):
        print(f"{diasDaSemana[i]} {stg1} {array[i]} {medida}")
        soma += array[i]
    medias = soma / len(array)
    return medias

# Função para alertar sobre o nível médio da água
def alertaMediaAgua(mediaNvlAgua):
    if mediaNvlAgua > 200:
        print("PERIGO!!! nível da água está muito alto")
    elif mediaNvlAgua > 130:
        print("Cuidado!! o nível da água está meio alto")
    else:
        print("Fique tranquilo, o nível da água está baixo")

# Função para alertar sobre a possibilidade de chuva com base na umidade
def alertaChuva(historicoUmidade):
    for i in range(len(historicoUmidade)):
        if historicoUmidade[i] > 70 and historicoUmidade[i] < 85:
            print(f"{diasDaSemana[i]}, poderá chover")
        elif historicoUmidade[i] > 85:
            print(f"{diasDaSemana[i]}, índices altos de umidade, cuidado ao sair de casa!!!")
        else:
            print(f"{diasDaSemana[i]}, umidade normal sem riscos de chuva")

# Função para alertar sobre a média de temperatura
def alertaMediaTerperatura(mediaTemperatura):
    if mediaTemperatura > 30:
        print("Está muito quente")
    elif mediaTemperatura > 25:
        print("Está calor")
    elif mediaTemperatura > 21:
        print("Temperatura normal")
    elif mediaTemperatura > 15:
        print("Frio")
    else:
        print("Muito frio")

# Função para gerar gráfico dos dados semanais
def gerarGrafico(diasDaSemana,historicoNvlAgua,historicoUmidade,historicoTemperatura):
    dias = np.arange(len(diasDaSemana))
    plt.figure(figsize=(10, 6))
    plt.plot(dias, historicoNvlAgua, marker='o', label='Nível da Água (cm)')
    plt.plot(dias, historicoUmidade, marker='o', label='Umidade (%)')
    plt.plot(dias, historicoTemperatura, marker='o', label='Temperatura (°C)')
    plt.xticks(dias, diasDaSemana)
    plt.xlabel('Dias da Semana')
    plt.ylabel('Valores')
    plt.title('Dados Semanais do AquaGuard')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    print("Obrigado por usar o AquaGuard, tenha uma boa semana, flw 🙋‍♀️🙋‍♂️")

# Função para exibir mensagem final ao usuário
def mensagemFinal(pode):
    if pode == 'sim':
        print(f"Ok, quaso haja futuros incidentes na sua região mandaremos uma menagem, muito obrigado {nome}")
    else:
        print(f"Tudo bem, qualquer coisa acesse o AquaGuard e mude sua opção, até mais {nome}")

# Início do programa - Boas vindas
comecar = forcaOpcao("Olá poderia preencher um pré cadastro para usar o site?", continuar)
if comecar == 'não':
    print("Tudo bem, tenha uma boa semana, flw 🙋‍♀️🙋‍♂️")

    # continua codigo
else:

    # cadastro do usuário
    nome = garanteString("Digite seu nome: ")
    anoDeNascimento = garanteNumero("Digite seu ano de nascimento: ",4)
    idade = anoAtual - anoDeNascimento
    cep = garanteNumero("Digite seu cep: ",8)
    telefone = garanteNumero("Digite seu telefone (formato = 5511999999999): ",13)
    cargo = garanteString("Qual seu cargo? ")

    print("\n")
    print("Obrigado por preencher os dados 🧑‍💻😁👍")
    print(f"Seja bem vindo {nome} ao AquaGuard🧊🧊🧊!!!")
    print(
        "Aqui você poderá ver sobre o nível da aguá e umidade em cada dia da semana e sua média, alem da temperatura diaria da semana 🌡️🌡")

    # entrada para escolher tipo de usuário
    opcao = ["civil", "funcionário público"]
    escolha = forcaOpcao(
        "Você é um civil ou um funcionário público (diferença, civil dados semanais já computados, funcioário terá inputs para falar os dados): ",
        opcao)

    if escolha == "civil":

        # Dados simulados do arduino
        historicoNvlAgua = [200, 100, 115, 170, 240, 166, 187]
        historicoUmidade = [80, 60, 75, 90, 57, 66, 99]
        historicoTemperatura = [20, 27, 35, 20, 17, 12, 11]

        # Cálculo e exibição das médias
        mediaNvlAgua = media(historicoNvlAgua, "o nível da água foi", " centímetros")
        pode = forcaOpcao("Pode continuar?",continuar)

        mediaUmidade = media(historicoUmidade, "a porcentagem da umidade foi", "%")
        pode = forcaOpcao("Pode continuar?", continuar)

        mediaTemperatura = media(historicoTemperatura, "a temperatura foi", "°C")
        pode = forcaOpcao("Pode continuar?", continuar)

        # alerta de acordo com a media da agua
        print("ALERTA NÍVEL DA ÁGUA\n")
        alertaNvlAgua = alertaMediaAgua(mediaNvlAgua)

        # alerta de acordo com a umidade diaria
        print("ALERTA CHUVA\n")
        alertaUmidade = alertaChuva(historicoUmidade)

        # alerta de acordo com a media de temperatura
        print("ALERTA TEMPERATURA\n")
        alertaTemperatura = alertaMediaTerperatura(mediaTemperatura)

        print("\n")
        print(f"Obrigado pela sua atenção {nome}, muito bom saber que a pessoas de {idade} interressadas no AquaGuard")
        print(f"Sempre que você quiser saber mais sobre os dados do seu cep {cep}, só acessar o AquaGuard")

        pode = forcaOpcao(f"Podemos mandar mensagem no telefone cadastrado {telefone}?", continuar)
        mensagemFinal(pode)
        # gráfico
        grafico = gerarGrafico(diasDaSemana, historicoNvlAgua, historicoUmidade, historicoTemperatura)

    # cadastro funcionário público
    else:
        senhaDeEntrada = ['1234']
        senhaParaEntrada = forcaOpcao("Se você for mesmo um funcionário público digite a senha para entrada (1234): ",
                                      senhaDeEntrada)

        # Arrays para armazenar dados inseridos pelo funcionário público
        historicoNvlAgua = []
        historicoUmidade = []
        historicoTemperatura = []

        # Coleta e cálculo das médias dos dados inseridos
        mediaNvlAgua = calcularMedia("Qual era o nivel da água no", historicoNvlAgua, "o nível da água foi",
                                     " centímetros")
        mediaUmidade = calcularMedia("Qual era a porcentagem da umidade no", historicoUmidade,
                                     "a porcentagem da umidade foi", "%")
        mediaTemperatura = calcularMedia("qual era a temperatura no", historicoTemperatura, "a temperatura foi", "°C")

        # alerta de acordo com a media da agua
        print("ALERTA NÍVEL DA ÁGUA\n")
        alertaNvlAgua = alertaMediaAgua(mediaNvlAgua)

        # alerta de acordo com a umidade diaria
        print("ALERTA CHUVA\n")
        alertaUmidade = alertaChuva(historicoUmidade)

        # alerta de acordo com a media de temperatura
        print("ALERTA TEMPERATURA\n")
        alertaTemperatura = alertaMediaTerperatura(mediaTemperatura)

        print("\n")
        print(
            f"Obrigado pela incrementação de dados {nome}, muito bom saber que a pessoas de {idade} estão trabalhando no AquaGuard e a favor do bem da população")
        pode = forcaOpcao(f"Podemos mandar mensagem no telefone cadastrado {telefone}?", continuar)
        mensagemFinal(pode)
        grafico = gerarGrafico(diasDaSemana, historicoNvlAgua, historicoUmidade, historicoTemperatura)

