from selenium import webdriver
from time import sleep
from datetime import datetime
from datetime import date


class WhatsaapBot:

    def __init__(self):
        options = webdriver.ChromeOptions()
        # Configurando a pasta profile, para mantermos os dados da seção
        options.add_argument('lang=pt-br')
        # Inicializa o webdriver
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=options)
        # Abre o whatsappweb
        self.driver.get("https://web.whatsapp.com/")
        # Aguarda alguns segundos para validação manual do QrCode
        self.driver.implicitly_wait(10)
        self.grupos_ou_pessoas = ["ZapBOT"]

    def Abre_Conversa(self):
        """ Abre a conversa com um contato especifico """
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo_ou_pessoa}']")
            sleep(2)
            campo_grupo.click()

    def Envia_Msg(self, msg):
        """ Envia uma mensagem para a conversa aberta """
        sleep(2)
        # Seleciona acaixa de mensagem
        chat_box = self.driver.find_element_by_class_name('_1Plpp')
        # Digita a mensagem
        chat_box.send_keys(msg)
        sleep(1)
        # Seleciona botão enviar
        botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        # Envia msg
        botao_enviar.click()
        sleep(2)

    def Ultima_Msg(self):
        """ Captura a ultima mensagem da conversa """
        post = self.driver.find_elements_by_class_name("_3_7SH")
        ultimo = len(post) - 1
        # O texto da ultima mensagem
        texto = post[ultimo].find_element_by_css_selector("span.selectable-text").text
        return texto


bot = WhatsaapBot()  # Inicia o objeto zapbot
bot.Abre_Conversa()  # Passando o numero ou o nome do contato
# bot.Envia_Msg()
msg = ""  # Criando a variável msg

dias = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-Feira', 'Sexta-feira', 'Sábado', 'Domingo']

espetinho = [('ESPETO DE CARNE - R$:8,00', 8.00), ('ESPETO DE CARNE (com creme de alho) - R$:9,50', 9.50),
             ('ESPETO DE PICAHNHA - R$:15,00', 15.00), ('ESPETO DE CUPIM - R$:13,00', 13.00),
             ('ESPETO DE CALABRESA DEFUMADA - R$7,00', 7.00), ('ESPETO DE FRANGO - R$:8,00', 8.00),
             ('ESPETO DE COXINHA DE FRANGO - R$:9,50', 9.50), ('ESPETO DE CORAÇÃO - R$:8,00', 8.00),
             ('ESPETO DE KAFTA - R$:10,00', 10.00), ('ESPETO DE TOSCANA R$:9,00', 9.00),
             ('MEDALHÃO DE CARNE - R$:13,50', 13.50), ('MEDALHÃO DE FRANGO - R$:11,50', 11.50)]

acompanhamento = [('PÃO DE ALHO - R$:6,00', 6.00), ('BATATA FRITA (P) - R$:8,00', 8.00),
                  ('BATATA FRITA (M) - R$:14,00', 14.00), ('BATATA FRITA (G) - R$:24,00', 24.00),
                  ('QUEIJO ASSADO c/MELAÇO OU s/MELAÇO - R$:8,00', 8.00)]

bebidas = [('COCA-COLA 350ml (lata) - R$:5,00', 5.00), ('COCA-COLA (1 litro) - R$:9,00', 9.00),
           ('GUARANÁ 269ml (lata) - R$:3,00', 3.00), ('GUARANÁ 350ml (lata) - R$:3,50', 3.50),
           ('GUARANÁ (1 litro) - R$:9,00', 9.00), ('ÁGUA 300ml (sem gás) - R$:3,00', 3.00),
           ('ÁGUA 300ml (com gás) - R$:4,00', 4.00), ('DEVASSA PURO MALTE 350ml (lata) - R$:5,00', 5.00),
           ('HEINEKEN (long neck) - R$:9,00', 9.00)]

combos = [('COMBO 1 - R$:28,00', 28.00), ('COMBO 2 - R$:22,00', 22.00), ('COMBO 3 - R$:35,00', 33.00),
          ('COMBO 4 - R$:22,00', 22.00), ('COMBO 5 - R$:22,00', 22.00), ('COMBO 6 - R$:35,00', 35.00),
          ('COMBO 7 - R$:35,00', 35.00)]

promoção_do_dia = ['COMBO 1 - R$:28,00\n(Batata Frita (P) + 1 Espeto de Picanha + Pão de Alho + 1 Guaraná 269ml (lata)',
                   'COMBO 2 - R$:17,00\n(1 Espeto de Picanha + Batata Frita (P) + 1 Guaraná 269ml (lata))',
                   'COMBO 3 - R$:28,00\n(File Acebolado + Batata Frita (M) + 1 Guaraná 269ml (lata))',
                   'COMBO 4 - R$:17,00\n(1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata)',
                   'COMBO 5 - R$:17,00\n(1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Guaraná 269ml (lata))',
                   'COMBO 6 - R$:30,00\n(Carne do Sol Acebolada + Batata Frita (M) + 1 Guaraná 269ml (lata))',
                   'COMBO 7 - R$:30,00\n(1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata))']

lista_itens_factura = []
lista_precos_factura = []
cont_esp = 0
data = date.today()
indice_da_semana = data.weekday()
dia_da_semana = dias[indice_da_semana]


def car_esp():
    bot.Envia_Msg("** ESPETINHOS **")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("[1]- ESPETO DE CARNE - R$:8,00")
    bot.Envia_Msg("[2]- ESPETO DE CARNE (com creme de alho) - R$:9,50")
    bot.Envia_Msg("[3]- ESPETO DE PICAHNHA - R$:15,00")
    bot.Envia_Msg("[4]- ESPETO DE CUPIM - R$:13,00")
    bot.Envia_Msg("[5]- ESPETO DE CALABRESA DEFUMADA - R$:7,00")
    bot.Envia_Msg("[6]- ESPETO DE FRANGO - R$:8,00
    bot.Envia_Msg("[7]- ESPETO DE COXINHA DE FRANGO - R$:9,50")
    bot.Envia_Msg("[8]- ESPETO DE CORAÇÃO - R$:8,00")
    bot.Envia_Msg("[9]- ESPETO DE KAFTA - R$:10,00")
    bot.Envia_Msg("[10]- ESPETO DE TOSCANA - R$:9,00")
    bot.Envia_Msg("[11]- MEDALHÃO DE CARNE - R$:13,50")
    bot.Envia_Msg("[12]- MEDALHÃO DE FRANGO - R$:11,50")
    bot.Envia_Msg("** --------------------------- **")


def car_acom():
    bot.Envia_Msg("** ACOMPANHAMENTOS **")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("1]- PÃO DE ALHO - R$:6,00")
    bot.Envia_Msg("[2]- BATATA FRITA (P) - R$:8,00")
    bot.Envia_Msg("[3]- BATATA FRITA (M) - R$:14,00")
    bot.Envia_Msg("[4]- BATATA FRITA (G) - R$:24,00")
    bot.Envia_Msg("[5]- QUEIJO ASSADO c/MELAÇO OU s/MELAÇO R$:8,00")
    bot.Envia_Msg("** --------------------------- **")


def car_bebida():
    bot.Envia_Msg("** BEBIDAS **")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("[1]- COCA-COLA 350ml (lata) - R$:5,00")
    bot.Envia_Msg("[2]- COCA-COLA (1 litro) - R$:9,00")
    bot.Envia_Msg("[3]- GUARANÁ 269ml (lata) - R$:3,00")
    bot.Envia_Msg("[4]- GUARANÁ 350ml (lata) - R$:3,50")
    bot.Envia_Msg("[5]- GUARANÁ (1 litro) - R$:9,00")
    bot.Envia_Msg("[6]- ÁGUA 300ml (sem gás) - R$:3,00")
    bot.Envia_Msg("[7]- ÁGUA 300ml (com gás) - R$:4,00")
    bot.Envia_Msg("[8]- DEVASSA PURO MALTE 350ml (lata) - R$:5,00")
    bot.Envia_Msg("[9]- HEINEKEN (long neck) - R$:9,00")
    bot.Envia_Msg("** --------------------------- **")


def car_combo():
    bot.Envia_Msg("** COMBOS **")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg(f"O COMBO {promoção_do_dia[indice_da_semana].split()[1]} ESTÁ EM PROMOÇÃO!!")
    bot.Envia_Msg(f"Está custando {promoção_do_dia[indice_da_semana].split()[3]}")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("[1]- COMBO 1 - R$:28,00")
    bot.Envia_Msg("(Batata Frita (P) + 1 Espeto de Picanha + Pão de Alho + 1 Guaraná 269ml (lata))")
    bot.Envia_Msg("[2]- COMBO 2 - R$:22,00")
    bot.Envia_Msg("(1 Espeto de Picanha + Batata Frita (P) + 1 Guaraná 269ml (lata))")
    bot.Envia_Msg("[3]- COMBO 3 - R$:33,00")
    bot.Envia_Msg("(File Acebolado + Batata Frita (M) + 1 Guaraná 269ml (lata))")
    bot.Envia_Msg("[4]- COMBO 4 - R$:22,00")
    bot.Envia_Msg("(1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata))")
    bot.Envia_Msg("[5]- COMBO 5 - R$:22,00")
    bot.Envia_Msg("(1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Guaraná 269ml (lata))")
    bot.Envia_Msg("[6]- COMBO 6 - R$:35,00")
    bot.Envia_Msg("(Carne do Sol Acebolada + Batata Frita (M) + 1 Guaraná 269ml (lata))")
    bot.Envia_Msg("[7]- COMBO 7 - R$:35,00")
    bot.Envia_Msg(
        "(1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata))")
    bot.Envia_Msg("** --------------------------- **")


def conta():
    global lista_itens_factura
    global lista_precos_factura

    bot.Envia_Msg("** |---------------------------| **")

| bot.Envia_Msg("** SUA CONTA **")
| bot.Envia_Msg("** |---------------------------| **")
preco_final = 0

for i in range(0, len(lista_itens_factura)):
    bot.Envia_Msg(f"{lista_itens_factura[i]}"")
    preco_final += lista_precos_factura[i]
    bot.Envia_Msg("** |---------------------------| **")
    bot.Envia_Msg(f"|Total a pagar: R$ {preco_final:.2f}|")
    bot.Envia_Msg("** |---------------------------| **")
    bot.Envia_Msg("Digite o endereço para a entrega.")


def verificar_tipo_pedido(valor='0', limite=1):
    while not valor.isdigit():
        bot.Envia_Msg("Digite um número inteiro por-favor")
        valor = input(': ')
    valor = int(valor)

    if valor > limite or valor <= 0:
        bot.Envia_Msg("A opção que você digitou não é válida! Por-favor tente novamente")
        return verificar_tipo_pedido(input(': '), limite)
    return valor


def verificar_quant_pedida(valor='0'):
    while not valor.isdigit():
        bot.Envia_Msg("'Digite um número inteiro por-favor")
        valor = input(': ')
    valor = int(valor)

    if valor <= 0:
        bot.Envia_Msg("A opção que você digitou não é válida! Por-favor tente novamente")
        return verificar_tipo_pedido(input(': '))
    return valor


def efetuar_pedidos():
    global lista_itens_factura
    global lista_precos_factura
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("** SUAS OPÇÕES: **")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("[1]- ESPETINHOS")
    bot.Envia_Msg("[2]- ACOMPANHAMENTO")
    bot.Envia_Msg("[3]- BEBIDAS")
    bot.Envia_Msg("[4]- COMBOS")
    bot.Envia_Msg("[5]- CANCERLAR PEDIDO")
    bot.Envia_Msg("[6]- EFETUAR PEDIDO")
    bot.Envia_Msg("** --------------------------- **")

    op_pedido = input('Digite a opção: ').strip()[0]

    if op_pedido == '1':
        quant_esp = verificar_quant_pedida(input('Quantos você deseja? '))
        while quant_esp > 0:
            car_esp()
            sabor = verificar_tipo_pedido(input(f'Dígite o sabor do Espetinho: '), 12)
            quant = verificar_quant_pedida(input(f'Quantos {espetinho[sabor - 1][0]} você deseja: '))
            while quant > quant_esp:
                print(f'Infelizmente você pediu uma quantidade inferior a essa!'
                      f'\nDigite uma quantidade que vai de 1 até {quant_esp}')
                quant = verificar_quant_pedida(input(f'Quantos {espetinho[sabor - 1][0]} você deseja: '))
            quant_esp -= quant
            lista_itens_factura.append(espetinho[sabor - 1][0])
            lista_precos_factura.append(espetinho[sabor - 1][1] * quant)
    elif op_pedido == '2':
        quant_acom = verificar_quant_pedida(input('Quantos você deseja? '))
        while quant_acom > 0:
            car_acom()
            op_acom = verificar_tipo_pedido(input(f'Dígite o Acompanhamento: '), 5)
            quant = verificar_quant_pedida(input(f'Quantos {acompanhamento[op_acom - 1][0]} você deseja: '))
            while quant > quant_acom:
                print(f'Infelizmente você pediu uma quantidade inferior a essa!'
                      f'\nDigite uma quantidade que vai de 1 até {quant_acom}')
                quant = verificar_quant_pedida(input(f'Quantos {acompanhamento[op_acom - 1][0]} você deseja: '))
            quant_acom -= quant
            lista_itens_factura.append(acompanhamento[op_acom - 1][0])
            lista_precos_factura.append(acompanhamento[op_acom - 1][1] * quant)
    elif op_pedido == '3':
        quant_bebi = int(input('Quantos você deseja? '))
        while quant_bebi > 0:
            car_bebida()
            op_bebi = verificar_tipo_pedido(input(f'Dígite a Bebida: '), 9)
            quant = verificar_quant_pedida(input(f'Quantos {bebidas[op_bebi - 1][0]} você deseja: '))
            while quant > quant_bebi:
                print(f'Infelizmente você pediu uma quantidade inferior a essa!'
                      f'\nDigite uma quantidade que vai de 1 até {quant_bebi}')
                quant = verificar_quant_pedida(input(f'Quantas {bebidas[op_bebi - 1][0]} você deseja: '))
            quant_bebi -= quant
            lista_itens_factura.append(bebidas[op_bebi - 1][0])
            lista_precos_factura.append(bebidas[op_bebi - 1][1] * quant)
    elif op_pedido == '4':
        quant_combo = verificar_quant_pedida(input('Quantos você deseja? '))
        while quant_combo > 0:
            car_combo()
            op_combo = verificar_tipo_pedido(input(f'Dígite o Combo: '), 7)
            quant = verificar_quant_pedida(input(f'Quantos {combos[op_combo - 1][0]} você deseja: '))
            while quant > quant_combo:
                print(f'Infelizmente você pediu uma quantidade inferior a essa!'
                      f'\nDigite uma quantidade que vai de 1 até {quant_combo}')
                quant = verificar_quant_pedida(input(f'Quantas {combos[op_combo - 1][0]} você deseja: '))
            quant_combo -= quant
            lista_itens_factura.append(combos[op_combo - 1][0])

            if indice_da_semana == op_combo - 1:
                print(
                    f'O combo {op_combo}: {combos[op_combo - 1][0]} está custando R$ {combos[op_combo - 1][1] - 5}\nPorque está em promoção')
                lista_precos_factura.append((combos[op_combo - 1][1] - 5) * quant)
            else:
                lista_precos_factura.append(combos[op_combo - 1][1] * quant)
    elif op_pedido == '5':
        lista_itens_factura.clear()
        lista_precos_factura.clear()
    elif op_pedido == '6':
        return False
    return True


def op_pedi():
    flag = efetuar_pedidos()
    while True:
        flag = efetuar_pedidos()

        if flag == False:
            bot.Envia_Msg("** --------------------------- **")
            bot.Envia_Msg("Seu pedido foi realizado com sucesso!")
            bot.Envia_Msg("** --------------------------- **")
            conta()
            break
    exit()


def vol_car():
    bot.Envia_Msg("[1]- IR PARA O CARDÁPIO")
    bot.Envia_Msg("[2]- FAZER SEU PEDIDO")
    bot.Envia_Msg("[3]- VOLTAR AO MENU INICIAL")
    bot.Envia_Msg("** --------------------------- **")
    voltar = input('Dígite sua opção: ').strip()[0]
    if voltar != '1' and voltar != '2' and voltar != '3':
        bot.Envia_Msg("** --------------------------- **")
        bot.Envia_Msg("Não entendi.")
        bot.Envia_Msg("Dígite uma das opções:")
        bot.Envia_Msg("** --------------------------- **")
        bot.Envia_Msg("[1]- IR PARA O CARDÁPIO")
        bot.Envia_Msg("[2]- FAZER SEU PEDIDO")
        bot.Envia_Msg("[3]- VOLTAR AO MENU PRINCIPAL")
        bot.Envia_Msg("** --------------------------- **")
        voltar = input('Dígite uma das opção: ').strip()[0]
    if voltar == '1':
        cardapio()
    elif voltar == '2':
        efetuar_pedidos()
    elif voltar == '3':
        main()


def menu_principal():
    bot.Envia_Msg("** --------------------------- **")


Dígite
uma
das
opções:
bot.Envia_Msg("** --------------------------- **")
bot.Envia_Msg("[1]- PROMOÇÕES DO DIA")
bot.Envia_Msg("[2]- CARDÁPIO")
bot.Envia_Msg("[3]- FAZER SEU PEDIDO")
bot.Envia_Msg("[4]- FINALIZAR ATENDIMENTO")
bot.Envia_Msg("** --------------------------- **")


def promocao_do_dia():
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg(f"PROMOÇÃO DO DIA ({dia_da_semana})")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg(f"{promoção_do_dia[indice_da_semana]}"")
    bot.Envia_Msg("** --------------------------- **")
    vol_car()


def cardapio():
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("** CARDÁPIO **")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("[1]- ESPETINHOS")
    bot.Envia_Msg("[2]- ACOMPANHAMENTO")
    bot.Envia_Msg("[3]- BEBIDAS")
    bot.Envia_Msg("[4]- COMBOS")
    bot.Envia_Msg("[5]- VOLTAR AO MENU INICIAL")
    bot.Envia_Msg("** --------------------------- **")

    car = input('Dígite sua Opção: ')
    bot.Envia_Msg("** --------------------------- **")

    while car != '1' and car != '2' and car != '3' and car != '4' and car != '5':
        bot.Envia_Msg("** --------------------------- **")
        bot.Envia_Msg("Não entendi")
        bot.Envia_Msg("Dígite uma das opções")
        bot.Envia_Msg("** --------------------------- **")
        bot.Envia_Msg("[1]- ESPETINHOS")
        bot.Envia_Msg("[2]- ACOMPANHAMENTO")
        bot.Envia_Msg("[3]- BEBIDAS")
        bot.Envia_Msg("[4]- COMBOS")
        bot.Envia_Msg("[5]- VOLTAR AO MENU INICIAL")
        bot.Envia_Msg("** --------------------------- **")

        car = input('Dígite sua Opção: ').strip()[0]

    if car == '1':
        car_esp()
        vol_car()
    elif car == '2':
        car_acom()
        vol_car()
    elif car == '3':
        car_bebida()
        vol_car()
    elif car == '4':
        car_combo()
        vol_car()
    elif car == '5':
        main()


def pedido():
    bot.Envia_Msg("** --------------------------- **")
    pronto = input('Pronto para fazer seu pedido [S/N]: ').upper().strip()[0]

    if pronto != 'S' and pronto != 'N':
        bot.Envia_Msg("Não entendi")
        bot.Envia_Msg("Dígite [S] para SIM | [N] para NÃO ")
        pronto = str(input('Pronto para fazer seu pedido [S/N]: ')).upper().strip()[0]
    elif pronto == 'S':
        op_pedi()
        bot.Envia_Msg("** --------------------------- **")
        bot.Envia_Msg("Deseja fazer mais um pedido?")
        bot.Envia_Msg("Dígite [S] para SIM e [N] para NÃO")
        bot.Envia_Msg("** --------------------------- **")
    else:
        menu_principal()


def main():
    menu_principal()
    op1 = input('Digite a opção: ').strip()[0]
    if op1 != '1' and op1 != '2' and op1 != '3' and op1 != '4':
        bot.Envia_Msg("** --------------------------- **")
        bot.Envia_Msg("Não entendi a opção dígitada.)
        menu_principal()
        op1 = input('Digite a opção: ').strip()[0]
        if op1 == '1':
            promocao_do_dia()
        elif op1 == '2':
            cardapio()
        elif op1 == '3':
            pedido()
        elif op1 == '4':
            return False
    return True


if __name__ == '__main__':
    hora = datetime.today().hour
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("** ESTAÇÃO DO ESPETINHO **")
    bot.Envia_Msg("** --------------------------- **")
    sleep(0.5)

    if hora < 12:
        bot.Envia_Msg("Olá Bom Dia!")
    elif hora < 18:
        bot.Envia_Msg("Olá Boa Tarde!")
    else:
        bot.Envia_Msg("Olá Boa Noite!")
        "
    bot.Envia_Msg("Seja Bem-vindo!")
    bot.Envia_Msg("Sou sua atendente virtual!")
    bot.Envia_Msg("eu me chamo Ana.")
    bot.Envia_Msg("irei passar agora suas opções")
    sleep(1)
    while True:
        flag = main()

        if flag == False:
            break
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("** Obrigado, volte sempre.**")
    bot.Envia_Msg("** --------------------------- **")
