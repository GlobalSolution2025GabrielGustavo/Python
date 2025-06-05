#Gabriel Akira Borges - RM: 565191
#Gustavo Francisco Santos - RM: 561820
#Sala: 1ESPJ

# Projeto AquaGuard - Proteção contra enchentes e desastres hídricos

import matplotlib.pyplot as plt
import numpy as np
import sys

# variaveis globais
diasDaSemana = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
anoAtual = 2025
continuar = ['sim', 'não']

# Função para forçar o usuário a escolher uma opção válida de uma lista
def forcaOpcao(stg, listaOpcao):
    exibirOpcoes = '\n'.join((listaOpcao))
    opcao = input(f"{stg}\n{exibirOpcoes}\n")
    while not opcao in listaOpcao:
        print(f"❌ Opa! Opção inválida. Por favor, escolha entre: {exibirOpcoes}\n")
        opcao = input(f"{stg}\n")
    return opcao

# Função para garantir que o usuário digite uma string (não numérica)
def garanteString(stg):
    string = input(stg)
    while string.isnumeric():
        print("🔢 Inválido! Isso parece um número. Por favor, digite um texto. Tente novamente.")
        string = input(stg)
    return string

def garanteSeIsnumeric(stg):
    num = input(stg)
    while not num.isnumeric():
        print("🚫 Entrada inválida! Por favor, digite apenas números. Tente novamente.")
        num = input(stg)
    return num

# Função para garantir que o usuário digite um número com quantidade de dígitos específica
def garanteNumero(stg,qtd):
    # 1. Verifica se a entrada é numérica
    entrada = garanteSeIsnumeric(stg)

    # 2. Verifica se a entrada tem a quantidade de caracteres esperada
    while not len(entrada) == qtd:
            print(f"📏 Entrada inválida! O número deve ter exatamente {qtd} dígitos. Tente novamente.")
            entrada = garanteSeIsnumeric(stg)

     # Se chegou até aqui, a entrada é numérica E tem a quantidade correta de caracteres
    return int(entrada) # Converte para int e retorna o valor

# Função para calcular a média de valores inseridos pelo usuário para cada dia da semana
def calcularMedia(stg, array, stg1, medida):
    i = 0
    soma = 0
    print(f"\n--- 💧 Dados diários de {stg1} ---")
    while i < 7:
        informacao = int(garanteSeIsnumeric(f"🗓️ {stg} {i + 1}° dia da semana: "))
        array.append(informacao)
        i += 1

    print("\n")

    for i in range(len(diasDaSemana)):
        print(f"{diasDaSemana[i]} {stg1} {array[i]} {medida}")
        soma += array[i]
    media = soma / len(array)
    print(f"\n📈 A média semanal {stg1} foi {int(media)} {medida}!")

    return media


# Função para calcular a média de um array e exibir os valores
def media(array, stg1, medida):
    soma = 0
    print(f"\n--- 📊 Dados semanais de {stg1} ---")
    for i in range(len(array)):
        print(f"{diasDaSemana[i]} {stg1} {array[i]} {medida}")
        soma += array[i]
    medias = soma / len(array)
    print(f"\n📈 A média semanal {stg1} foi {int(medias)} {medida}!")
    return medias

# Função para alertar sobre o nível médio da água
def alertaMediaAgua(mediaNvlAgua):
    print("\n--- 🚨 ALERTA: NÍVEL DA ÁGUA ---")
    if mediaNvlAgua > 200:
        print("🌊💧 PERIGO!!! O nível da água está MUITO ALTO! Risco de enchente iminente! Fique seguro(a)! 🚨")
    elif mediaNvlAgua > 130:
        print("⚠️ Cuidado! O nível da água está meio alto. Monitore a situação com atenção. 📈")
    else:
        print("✅ Fique tranquilo(a)! O nível da água está baixo. Tudo sob controle. 👍")

# Função para alertar sobre a possibilidade de chuva com base na umidade
def alertaChuva(historicoUmidade):
    print("\n--- 🌧️ ALERTA: POSSIBILIDADE DE CHUVA ---")
    for i in range(len(historicoUmidade)):
        if historicoUmidade[i] > 70 and historicoUmidade[i] < 85:
            print(f"🌦️ {diasDaSemana[i]}: A umidade está em {historicoUmidade[i]}%, poderá chover. Leve um guarda-chuva! ☔")
        elif historicoUmidade[i] > 85:
            print(f"⛈️ {diasDaSemana[i]}: Índices ALTÍSSIMOS de umidade ({historicoUmidade[i]}%). CUIDADO ao sair de casa! Risco de temporais! ⚡")
        else:
            print(f"☀️ {diasDaSemana[i]}: Umidade normal ({historicoUmidade[i]}%). Céu limpo e sem riscos de chuva. Aproveite! 😎")

# Função para alertar sobre a média de temperatura
def alertaMediaTerperatura(mediaTemperatura):
    print("\n--- 🌡️ ALERTA: TEMPERATURA ---")
    if mediaTemperatura > 30:
        print("🥵 Está MUITO QUENTE! Hidrate-se e evite o sol. ☀️")
    elif mediaTemperatura > 25:
        print("🔥 Está calor! Beba bastante água. 💧")
    elif mediaTemperatura > 21:
        print("Temperatura normal e agradável. Perfeito para atividades ao ar livre! 😊")
    elif mediaTemperatura > 15:
        print("🥶 Frio! Vista um casaco e se agasalhe. 🧣")
    else:
        print("🧊 Muito frio! Brrr... Mantenha-se aquecido(a)! 🧤")

#Validar Senha
def validarSenha(stg, senhaDeEntrada, tentativasMaximas):
    tentativas = 0  # Inicializa o contador de tentativas dentro da função
    while tentativas < tentativasMaximas:
        senha = input(stg)  # Pede a senha ao usuário

        if senha == senhaDeEntrada:
            print("🔑 Senha correta! Acesso concedido. Bem-vindo(a) de volta! ✨")
            return True  # Senha correta, sai da função e o código continua
        else:
            tentativas += 1  # Incrementa o número de tentativas
            print(f"❌ Senha incorreta! Você tem mais {tentativasMaximas - tentativas} tentativa(s). Tente novamente.")

    print("\n🚫 Número máximo de tentativas excedido. Encerrando o programa por segurança. Até mais! 👋")
    sys.exit()

# Função para gerar gráfico dos dados semanais
def gerarGrafico(diasDaSemana,historicoNvlAgua,historicoUmidade,historicoTemperatura):
    dias = np.arange(len(diasDaSemana))
    plt.figure(figsize=(10, 6))
    plt.plot(dias, historicoNvlAgua, marker='o', linestyle='-', color='blue', label='Nível da Água (cm) 🌊')
    plt.plot(dias, historicoUmidade, marker='o', linestyle='--', color='green', label='Umidade (%) 💧')
    plt.plot(dias, historicoTemperatura, marker='o', linestyle=':', color='red', label='Temperatura (°C) 🌡️')
    plt.xticks(dias, diasDaSemana)
    plt.xlabel('Dias da Semana')
    plt.ylabel('Valores')
    plt.title('Dados Semanais do AquaGuard')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    print("Obrigado por usar o AquaGuard! Tenha uma boa semana e fique seguro(a)! 👋🛡️")

# Função para exibir mensagem final ao usuário
def mensagemFinal(pode):
    if pode == 'sim':
        print(f"👍 Ok, caso haja futuros incidentes em sua região, mandaremos uma mensagem. Muito obrigado, {nome}! Estamos juntos na prevenção! 🤝")
    else:
        print(f"👋 Tudo bem, {nome}! Se precisar, acesse o AquaGuard e mude suas opções. Até mais! 😊")

# Início do programa - Boas vindas
print("🌊 Bem-vindo(a) ao AquaGuard! Seu escudo contra enchentes e desastres hídricos! 🛡️")
comecar = forcaOpcao("Olá! Gostaríamos de te convidar para um pré-cadastro rápido e gratuito. Podemos começar?", continuar)
if comecar == 'não':
    print("👋 Tudo bem! Entendemos. Tenha uma boa semana e fique seguro(a)! AquaGuard está sempre por aqui. 💧")
    # continua codigo
else:

    # cadastro do usuário
    nome = garanteString("📝 Digite seu nome : ")
    anoDeNascimento = garanteNumero("🎂 Digite seu ano de nascimento (AAAA): ",4)
    idade = anoAtual - anoDeNascimento
    cep = garanteNumero("📍 Digite seu CEP (8 dígitos): ",8)
    telefone = garanteNumero("📱 Digite seu telefone com DDD (ex: 5511999999999 - 13 dígitos): ",13)
    cargo = garanteString("💼 Qual seu cargo ou profissão? ")

    print("\n")
    print("Obrigado por preencher os dados 🧑‍💻😁👍")
    print(f"Seja bem vindo {nome} ao AquaGuard🧊🧊🧊!!!")
    print("Aqui você poderá ver sobre o nível da aguá e umidade em cada dia da semana e sua média, alem da temperatura diaria da semana 🌡️🌡")

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
        input("\nPressione Enter para continuar...")

        mediaUmidade = media(historicoUmidade, "a porcentagem da umidade foi", "%")
        input("\nPressione Enter para continuar...")

        mediaTemperatura = media(historicoTemperatura, "a temperatura foi", "°C")
        input("\nPressione Enter para continuar...")

        # alerta de acordo com a media da agua
        alertaNvlAgua = alertaMediaAgua(mediaNvlAgua)

        # alerta de acordo com a umidade diaria
        alertaUmidade = alertaChuva(historicoUmidade)

        # alerta de acordo com a media de temperatura
        alertaTemperatura = alertaMediaTerperatura(mediaTemperatura)

        print("\n")
        print(f"✨ Obrigado pela sua atenção, {nome}! É ótimo saber que pessoas com {idade} anos estão interessadas no AquaGuard. 💙")
        print(f"🏠 Sempre que quiser saber mais sobre os dados do seu CEP {cep}, é só acessar o AquaGuard!")

        pode = forcaOpcao(f"Podemos mandar mensagem no telefone cadastrado {telefone}?", continuar)
        mensagemFinal(pode)
        # gráfico
        grafico = gerarGrafico(diasDaSemana, historicoNvlAgua, historicoUmidade, historicoTemperatura)

    # cadastro funcionário público
    else:
        senhaDeEntrada = '1234'
        senhaParaEntrada = validarSenha("Se você for mesmo um funcionário público digite a senha para entrada (1234): ",senhaDeEntrada,3)

        # Arrays para armazenar dados inseridos pelo funcionário público
        historicoNvlAgua = []
        historicoUmidade = []
        historicoTemperatura = []

        # Coleta e cálculo das médias dos dados inseridos
        mediaNvlAgua = calcularMedia("Qual era o nivel da água no", historicoNvlAgua, "o nível da água foi"," centímetros")

        mediaUmidade = calcularMedia("Qual era a porcentagem da umidade no", historicoUmidade,"a porcentagem da umidade foi", "%")

        mediaTemperatura = calcularMedia("qual era a temperatura no", historicoTemperatura, "a temperatura foi", "°C")

        # alerta de acordo com a media da agua
        alertaNvlAgua = alertaMediaAgua(mediaNvlAgua)
        input("\nPressione Enter para continuar...")

        # alerta de acordo com a umidade diaria
        alertaUmidade = alertaChuva(historicoUmidade)
        input("\nPressione Enter para continuar...")

        # alerta de acordo com a media de temperatura
        alertaTemperatura = alertaMediaTerperatura(mediaTemperatura)
        input("\nPressione Enter para continuar...")
        print("\n")
        print(f"Obrigado pela incrementação de dados {nome}, muito bom saber que a pessoas de {idade} estão trabalhando no AquaGuard e a favor do bem da população")

        pode = forcaOpcao(f"Podemos mandar mensagem no telefone cadastrado {telefone}?", continuar)
        mensagemFinal(pode)
        grafico = gerarGrafico(diasDaSemana, historicoNvlAgua, historicoUmidade, historicoTemperatura)

