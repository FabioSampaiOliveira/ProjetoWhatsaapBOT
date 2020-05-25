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
        self.grupos_ou_pessoas = ["Eufranio Python"]

    def Abre_Conversa(self, contato):
        caixa_de_pesquisa = self.driver.find_element_by_class_name("_2S1VP")
        caixa_de_pesquisa.send_keys(contato)
        sleep(2)
        contato = self.driver.find_element_by_xpath("//span[@title = '{}']".format(contato))
        contato.click()

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

    def sair(self):
        self.driver.quit

    def Ultima_Msg(self, mensagem=""):
        """ Captura a ultima mensagem da conversa """
        if mensagem != "":
            self.Envia_Msg(mensagem)
        post = self.driver.find_elements_by_class_name("_3_7SH")
        ultimo = len(post) - 1
        # O texto da ultima mensagem
        texto = post[ultimo].find_element_by_css_selector("span.selectable-text").text
        return texto


dias = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-Feira', 'Sexta-feira', 'Sábado', 'Domingo']

espetinho = [('ESPETO DE CARNE - R$: 8,00', 8.00), ('ESPETO DE CARNE (com creme de alho) - R$: 9,50', 9.50),
             ('ESPETO DE PICAHNHA - R$: 15,00', 15.00), ('ESPETO DE CUPIM - R$: 13,00', 13.00),
             ('ESPETO DE CALABRESA DEFUMADA - R$: 7,00', 7.00), ('ESPETO DE FRANGO - R$: 8,00', 8.00),
             ('ESPETO DE COXINHA DE FRANGO - R$: 9,50', 9.50), ('ESPETO DE CORAÇÃO - R$: 8,00', 8.00),
             ('ESPETO DE KAFTA - R$: 10,00', 10.00), ('ESPETO DE TOSCANA R$: 9,00', 9.00),
             ('MEDALHÃO DE CARNE - R$: 13,50', 13.50), ('MEDALHÃO DE FRANGO - R$: 11,50', 11.50)]

acompanhamento = [('PÃO DE ALHO - R$: 6,00', 6.00), ('BATATA FRITA (P) - R$: 8,00', 8.00),
                  ('BATATA FRITA (M) - R$: 14,00', 14.00), ('BATATA FRITA (G) - R$: 24,00', 24.00),
                  ('QUEIJO ASSADO c/MELAÇO OU s/MELAÇO - R$: 8,00', 8.00)]

bebidas = [('COCA-COLA 350ml (lata) - R$: 5,00', 5.00), ('COCA-COLA (1 litro) - R$: 9,00', 9.00),
           ('GUARANÁ 269ml (lata) - R$: 3,00', 3.00), ('GUARANÁ 350ml (lata) - R$: 3,50', 3.50),
           ('GUARANÁ (1 litro) - R$: 9,00', 9.00), ('ÁGUA 300ml (sem gás) - R$: 3,00', 3.00),
           ('ÁGUA 300ml (com gás) - R$: 4,00', 4.00), ('DEVASSA PURO MALTE 350ml (lata) - R$: 5,00', 5.00),
           ('HEINEKEN (long neck) - R$: 9,00', 9.00)]

combos = [('COMBO 1 - R$: 28,00', 28.00), ('COMBO 2 - R$: 22,00', 22.00), ('COMBO 3 - R$: 35,00', 33.00),
          ('COMBO 4 - R$: 22,00', 22.00), ('COMBO 5 - R$: 22,00', 22.00), ('COMBO 6 - R$: 35,00', 35.00),
          ('COMBO 7 - R$: 35,00', 35.00)]

combos1 = ['COMBO 1 - R$: 23,00', 'COMBO 2 - R$: 17,00', 'COMBO 3 - R$: 30,00',
          'COMBO 4 - R$: 17,00', 'COMBO 5 - R$: 17,00', 'COMBO 6 - R$: 30,00',
          'COMBO 7 - R$: 30,00']

promoção_do_dia = [
    'COMBO 1 - R$: 28,00 (Batata Frita (P) + 1 Espeto de Picanha + Pão de Alho + 1 Guaraná 269ml (lata)',
    'COMBO 2 - R$: 17,00 (1 Espeto de Picanha + Batata Frita (P) + 1 Guaraná 269ml (lata))',
    'COMBO 3 - R$: 28,00 (File Acebolado + Batata Frita (M) + 1 Guaraná 269ml (lata))',
    'COMBO 4 - R$: 17,00 (1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata)',
    'COMBO 5 - R$: 17,00 (1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Guaraná 269ml (lata))',
    'COMBO 6 - R$: 30,00 (Carne do Sol Acebolada + Batata Frita (M) + 1 Guaraná 269ml (lata))',
    'COMBO 7 - R$: 30,00 (1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata))']

data = date.today()
indice_da_semana = data.weekday()
dia_da_semana = dias[indice_da_semana]
lista_itens_factura = []
lista_precos_factura = []
cont_esp = 0


def Continuar():
    bot.Envia_Msg("""*SUAS OPÇÕES:*
    *[1]*- CONTINUAR COMPRANDO
    *[2]*- CANCELAR PEDIDO
    *[3]*- FINALIZAR PEDIDO
    *|---------------------------|*""")
    msg = ""  # Criando a variável msg
    while True:
        msg = bot.Ultima_Msg()
        if msg == "1":
            efetuar_pedidos()
        if msg == "2":
            lista_itens_factura.clear()
            lista_precos_factura.clear()
        elif msg == "3":
            bot.Envia_Msg("*Seu pedido foi realizado com sucesso!*")
            conta()
            break
    exit()



def vol_car():
    bot.Envia_Msg("""*SUAS OPÇÕES:*
    *[1]*- IR PARA O CARDÁPIO
    *[2]*- FAZER O PEDIDO
    *[3]*- VOLTAR AO MENU INICIAL
    *|---------------------------|*""")
    msg = ""  # Criando a variável msg
    while msg != "3":
        msg = bot.Ultima_Msg()  # A cada loop recebe a ultima mensagem da conversa
        if msg == "1":
            cardapio()
        if msg == "2":
            op_pedi()
        elif msg == "3":
            Menu_Ini()


def car_esp():
    bot.Envia_Msg("""*ESPETINHOS*
    *|---------------------------|*
    *[1]*- ESPETO DE CARNE - R$: 8,00
    *[2]*- ESPETO DE CARNE (com creme de alho) - R$: 9,50
    *[3]*- ESPETO DE PICANHA - R$: 15,00
    *[4]*- ESPETO DE CUPIM - R$: 13,00
    *[5]*- ESPETO DE CALABRESA DEFUMADA - R$: 7,00
    *[6]*- ESPETO DE FRANGO - R$: 8,00
    *[7]*- ESPETO DE COXINHA DE FRANGO - R$: 9,50
    *[8]*- ESPETO DE CORAÇÃO - R$: 8,00
    *[9]*- ESPETO DE KAFTA - R$: 10,00
    *[10]*- ESPETO DE TOSCANA - R$: 9,00
    *[11]*- MEDALHÃO DE CARNE - R$: 13,50
    *[12]*- MEDALHÃO DE FRANGO - R$: 11,50
    *|---------------------------|*""")


def car_acom():
    bot.Envia_Msg("""*ACOMPANHAMENTOS*
    *|---------------------------|*
    *[1]*- PÃO DE ALHO - R$: 6,00
    *[2]*- BATATA FRITA (P) - R$: 8,00
    *[3]*- BATATA FRITA (M) - R$: 14,00
    *[4]*- BATATA FRITA (G) - R$: 24,00
    *[5]*- QUEIJO ASSADO c/MELAÇO OU s/MELAÇO R$: 8,00
    *|---------------------------|*""")


def car_bebida():
    bot.Envia_Msg("""*BEBIDAS*
    *|---------------------------|*
    *[1]*- COCA-COLA 350ml (lata) - R$: 5,00
    *[2]*- COCA-COLA (1 litro) - R$: 9,00
    *[3]*- GUARANÁ 269ml (lata) - R$: 3,00
    *[4]*- GUARANÁ 350ml (lata) - R$: 3,50
    *[5]*- GUARANÁ (1 litro) - R$: 9,00
    *[6]*- ÁGUA 300ml (sem gás) - R$: 3,00
    *[7]*- ÁGUA 300ml (com gás) - R$: 4,00
    *[8]*- DEVASSA PURO MALTE 350ml (lata) - R$: 5,00
    *[9]*- HEINEKEN (long neck) - R$: 9,00
    *|---------------------------|*""")


def car_combo():
    if indice_da_semana == 0:
        comb1 = "*R$: 23,00*"
    else:
        comb1 = "R$: 28,00"
    if indice_da_semana == 1:
        comb2 = "*R$: 17,00*"
    else:
        comb2 = "R$: 22,00"
    if indice_da_semana == 2:
        comb3 = "*R$: 28,00*"
    else:
        comb3 = "R$: 33,00"
    if indice_da_semana == 3:
        comb4 = "*R$: 17,00*"
    else:
        comb4 = "R$: 22,00"
    if indice_da_semana == 4:
        comb5 = "*R$: 17,00*"
    else:
        comb5 = "R$: 22,00"
    if indice_da_semana == 5:
        comb6 = "*R$: 30,00*"
    else:
        comb6 = "R$: 35,00"
    if indice_da_semana == 6:
        comb7 = "*R$: 30,00*"
    else:
        comb7 = "R$: 35,00"

    bot.Envia_Msg(f"""*COMBOS*
    *|---------------------------|*

    *[1]*- COMBO 1 - R$: {comb1}
    (Batata Frita (P) + 1 Espeto de Picanha + Pão de Alho + 1 Guaraná 269ml (lata))

    *[2]*- COMBO 2 - R$: {comb2}
    (1 Espeto de Picanha + Batata Frita (P) + 1 Guaraná 269ml (lata))

    *[3]*- COMBO 3 - {comb3}
    (File Acebolado + Batata Frita (M) + 1 Guaraná 269ml (lata))

    *[4]*- COMBO 4 - {comb4}
    (1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata))

    *[5]*- COMBO 5 - {comb5}
    (1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Guaraná 269ml (lata))

    *[6]*- COMBO 6 - {comb6}
    (Carne do Sol Acebolada + Batata Frita (M) + 1 Guaraná 269ml (lata))

    *[7]*- COMBO 7 - {comb7}
    (1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata))
    *|---------------------------|*""")


def car_esp1():
    bot.Envia_Msg("""*ESPETINHOS*
    *|---------------------------|*
    ESPETO DE CARNE - R$: 8,00
    ESPETO DE CARNE (com creme de alho) - R$: 9,50
    ESPETO DE PICANHA - R$: 15,00
    ESPETO DE CUPIM - R$: 13,00
    ESPETO DE CALABRESA DEFUMADA - R$: 7,00
    ESPETO DE FRANGO - R$: 8,00
    ESPETO DE COXINHA DE FRANGO - R$: 9,50
    ESPETO DE CORAÇÃO - R$: 8,00
    ESPETO DE KAFTA - R$: 10,00
    ESPETO DE TOSCANA - R$: 9,00
    MEDALHÃO DE CARNE - R$: 13,50
    MEDALHÃO DE FRANGO - R$: 11,50
    *|---------------------------|*""")
    vol_car()


def car_acom1():
    bot.Envia_Msg("""*ACOMPANHAMENTOS*
    *|---------------------------|*
    PÃO DE ALHO - R$: 6,00
    BATATA FRITA (P) - R$: 8,00
    BATATA FRITA (M) - R$: 14,00
    BATATA FRITA (G) - R$: 24,00
    QUEIJO ASSADO c/MELAÇO OU s/MELAÇO R$: 8,00
    *|---------------------------|*""")
    vol_car()


def car_bebida1():
    bot.Envia_Msg("""*BEBIDAS*
    *|---------------------------|*
    COCA-COLA 350ml (lata) - R$: 5,00
    COCA-COLA (1 litro) - R$: 9,00
    GUARANÁ 269ml (lata) - R$: 3,00
    GUARANÁ 350ml (lata) - R$: 3,50
    GUARANÁ (1 litro) - R$: 9,00
    ÁGUA 300ml (sem gás) - R$: 3,00
    ÁGUA 300ml (com gás) - R$: 4,00
    DEVASSA PURO MALTE 350ml (lata) - R$: 5,00
    HEINEKEN (long neck) - R$: 9,00
    *|---------------------------|*""")
    vol_car()


def car_combo1():
    if indice_da_semana == 0:
        comb1 = "*R$: 23,00*"
    else:
        comb1 = "R$: 28,00"
    if indice_da_semana == 1:
        comb2 = "*R$: 17,00*"
    else:
        comb2 = "R$: 22,00"
    if indice_da_semana == 2:
        comb3 = "*R$: 28,00*"
    else:
        comb3 = "R$: 33,00"
    if indice_da_semana == 3:
        comb4 = "*R$: 17,00*"
    else:
        comb4 = "R$: 22,00"
    if indice_da_semana == 4:
        comb5 = "*R$: 17,00*"
    else:
        comb5 = "R$: 22,00"
    if indice_da_semana == 5:
        comb6 = "*R$: 30,00*"
    else:
        comb6 = "R$: 35,00"
    if indice_da_semana == 6:
        comb7 = "*R$: 30,00*"
    else:
        comb7 = "R$: 35,00"

    bot.Envia_Msg(f"""*COMBOS*
    *|---------------------------|*
    *O COMBO {promoção_do_dia[indice_da_semana].split()[1]} ESTÁ EM PROMOÇÃO!!
    *|---------------------------|*
    COMBO 1 - R$: {comb1}
    (Batata Frita (P) + 1 Espeto de Picanha + Pão de Alho + 1 Guaraná 269ml (lata))
    COMBO 2 - R$: {comb2}
    (1 Espeto de Picanha + Batata Frita (P) + 1 Guaraná 269ml (lata))
    COMBO 3 - {comb3}
    (File Acebolado + Batata Frita (M) + 1 Guaraná 269ml (lata))
    COMBO 4 - {comb4}
    (1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata))
    COMBO 5 - {comb5}
    (1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Guaraná 269ml (lata))
    COMBO 6 - {comb6}
    (Carne do Sol Acebolada + Batata Frita (M) + 1 Guaraná 269ml (lata))
    COMBO 7 - {comb7}
    (1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata))
    *|---------------------------|*""")
    vol_car()


def cardapio():
    bot.Envia_Msg("""*CARDÁPIO:*
    *|---------------------------|*
    *[1]*- ESPETINHOS
    *[2]*- ACOMPANHAMENTO
    *[3]*- BEBIDAS
    *[4]*- COMBOS
    *[5]*- VOLTAR AO MENU INICIAL
    *|---------------------------|*""")
    msg = ""  # Criando a variável msg
    while msg != "5":
        sleep(1)
        msg = bot.Ultima_Msg()  # A cada loop recebe a ultima mensagem da conversa
        if msg == "1":
            car_esp1()
        if msg == "2":
            car_acom1()
        if msg == "3":
            car_bebida1()
        if msg == "4":
            car_combo1()
        elif msg == "5":
            Menu_Ini()


def conta():
    global lista_itens_factura
    global lista_precos_factura

    bot.Envia_Msg("""*SUA CONTA*              
    *|---------------------------|*""")
    preco_final = 0

    for i in range(0, len(lista_itens_factura)):
        bot.Envia_Msg(f'{lista_itens_factura[i]}')
        preco_final += lista_precos_factura[i]
    bot.Envia_Msg(f"""*|---------------------------|*
    *Total a pagar: R$ {preco_final:.2f}*
    *|---------------------------|*
    *Digite o endereço para a entrega.*""")


def verificar_numero_inteiro():
    numero_sendo_testado = ""

    while not numero_sendo_testado.isdigit():
        numero_sendo_testado = bot.Ultima_Msg()
    return numero_sendo_testado


def verificar_tipo_pedido(numero_sendo_testado='0', limite=1):
    while not numero_sendo_testado.isdigit():
        numero_sendo_testado = bot.Ultima_Msg()
    numero_sendo_testado = int(numero_sendo_testado)

    if numero_sendo_testado > limite:
        bot.Envia_Msg("A opção que você digitou não é válida! Por-favor tente novamente")
        return verificar_tipo_pedido(verificar_numero_inteiro(), limite)
    return numero_sendo_testado


def efetuar_pedidos():
    global lista_itens_factura
    global lista_precos_factura

    bot.Envia_Msg("""*SUAS OPÇÕES:*
    *|---------------------------|*
    *[1]*- ESPETINHOS
    *[2]*- ACOMPANHAMENTO
    *[3]*- BEBIDAS
    *[4]*- COMBOS
    *|---------------------------|*""")

    op_pedido = ""
    while op_pedido != '6':
        op_pedido = verificar_numero_inteiro()

        if op_pedido == '1':
            bot.Envia_Msg("*Quantos você deseja?*")
            quant_esp = int(verificar_numero_inteiro())
            while quant_esp > 0:
                car_esp()
                sabor = verificar_tipo_pedido(verificar_numero_inteiro(), 12)
                bot.Envia_Msg(f"*Quantos {espetinho[sabor - 1][0]} você deseja:*")
                quant = int(verificar_numero_inteiro())

                while quant > quant_esp:
                    bot.Envia_Msg(f"""*Infelizmente você pediu uma quantidade inferior a essa!
                    Digite uma quantidade que vai de 1 até {quant_esp}*""")
                    bot.Envia_Msg(f"*Quantos {espetinho[sabor - 1][0]} você deseja:*")
                    quant = int(verificar_numero_inteiro())
                quant_esp -= quant
                lista_itens_factura.append(espetinho[sabor - 1][0])
                lista_precos_factura.append(espetinho[sabor - 1][1] * quant)
            Continuar()
        elif op_pedido == '2':
            bot.Envia_Msg("*Quantos você deseja?*")
            quant_acom = int(verificar_numero_inteiro())
            while quant_acom > 0:
                car_acom()
                op_acom = verificar_tipo_pedido(verificar_numero_inteiro(), 5)
                bot.Envia_Msg(f"*Quantos {acompanhamento[op_acom - 1][0]} você deseja:*")
                quant = int(verificar_numero_inteiro())

                while quant > quant_acom:
                    bot.Envia_Msg(f"""*Infelizmente você pediu uma quantidade inferior a essa!
                    Digite uma quantidade que vai de 1 até {quant_acom}*""")
                    bot.Envia_Msg(f"*Quantos {acompanhamento[op_acom - 1][0]} você deseja:*")
                    quant = int(verificar_numero_inteiro())
                quant_acom -= quant
                lista_itens_factura.append(acompanhamento[op_acom - 1][0])
                lista_precos_factura.append(acompanhamento[op_acom - 1][1] * quant)
            Continuar()
        elif op_pedido == '3':
            bot.Envia_Msg("*Quantas você deseja?*")
            quant_bebi = int(verificar_numero_inteiro())
            while quant_bebi > 0:
                car_bebida()
                op_bebi = verificar_tipo_pedido(verificar_numero_inteiro(), 9)
                bot.Envia_Msg(f"*Quantos {bebidas[op_bebi - 1][0]} você deseja:*")
                quant = int(verificar_numero_inteiro())

                while quant > quant_bebi:
                    bot.Envia_Msg(f"""*Infelizmente você pediu uma quantidade inferior a essa!
                    Digite uma quantidade que vai de 1 até {quant_bebi}*""")
                    bot.Envia_Msg(f"*Quantos {bebidas[op_bebi - 1][0]} você deseja:*")
                    quant = int(verificar_numero_inteiro())
                quant_bebi -= quant
                lista_itens_factura.append(bebidas[op_bebi - 1][0])
                lista_precos_factura.append(bebidas[op_bebi - 1][1] * quant)
            Continuar()
        elif op_pedido == '4':
            bot.Envia_Msg("*Quantos você deseja?*")
            quant_combo = int(verificar_numero_inteiro())
            while quant_combo > 0:
                car_combo()
                op_combo = verificar_tipo_pedido(verificar_numero_inteiro(), 7)
                bot.Envia_Msg(f"*Quantos {combos[op_combo - 1][0]} você deseja:*")
                quant = int(verificar_numero_inteiro())

                while quant > quant_combo:
                    bot.Envia_Msg(f"""*Infelizmente você pediu uma quantidade inferior a essa!
                    Digite uma quantidade que vai de 1 até {quant_combo}*""")
                    bot.Envia_Msg(f"*Quantos {combos[op_combo - 1][0]} você deseja:*")
                    quant = int(verificar_numero_inteiro())
                quant_combo -= quant
                if indice_da_semana == op_combo - 1:
                    bot.Envia_Msg(f"""*O combo {op_combo}: {combos[op_combo - 1][0]} 
                    está custando R$ {combos[op_combo - 1][1] - 5}  
                    Porque está em promoção*""")
                    lista_itens_factura.append(combos1[op_combo - 1])
                    lista_precos_factura.append((combos[op_combo - 1][1] - 5) * quant)
                else:
                    lista_itens_factura.append(combos[op_combo - 1][0])
                    lista_precos_factura.append(combos[op_combo - 1][1] * quant)
            Continuar()
#-------------------------------------------------------------------------------------
            #elif op_pedido == '5':
        #    lista_itens_factura.clear()
        #    lista_precos_factura.clear()
        #elif op_pedido == '6':
        #    return False
        #return True


#def op_pedi():
#    flag = efetuar_pedidos()
#    while True:
#        flag = efetuar_pedidos()
#
#        if flag == False:
#            bot.Envia_Msg("*Seu pedido foi realizado com sucesso!*")
#            conta()
#            break
#    exit()
#-------------------------------------------------------------------------------------

def promocao_do_dia():
    bot.Envia_Msg(f"""*PROMOÇÃO DO DIA ({dia_da_semana})
    {promoção_do_dia[indice_da_semana]}*""")
    vol_car()


def Menu_Ini():
    bot.Envia_Msg("""*SUAS OPÇÕES:*
    *|---------------------------|*
    *[1]*- PROMOÇÕES DO DIA
    *[2]*- CARDÁPIO
    *[3]*- FAZER PEDIDO
    *[4]*- FINALIZAR ATENDIMENTO
    *|---------------------------|*""")
    msg = ""  # Criando a variável msg
    while msg != "4":
        sleep(1)
        msg = bot.Ultima_Msg()  # A cada loop recebe a ultima mensagem da conversa
        if msg == "1":  # Retorna uma mensagem de ajuda
            promocao_do_dia()
        if msg == "2":
            cardapio()
        if msg == "3":
            efetuar_pedidos()
        elif msg == "4":  # Encerra o programa
            bot.Envia_Msg("*Obrigado, volte sempre.*")
            break
    bot.sair()


if __name__ == '__main__':
    bot = WhatsaapBot()  # Inicia o objeto zapbot
    bot.Abre_Conversa("ZapBOT")  # Passando o numero ou o nome do contato
    hora = datetime.today().hour
    Saudação = ""
    if hora < 12:
        Saudação = "Olá Bom Dia!"
    elif hora < 18:
        Saudação = "Olá Boa Tarde!"
    else:
        Saudação = "Olá Boa Noite!"
    bot.Envia_Msg(f"""*ESTAÇÃO DO ESPETINHO*
    {Saudação}, Seja Bem-vindo!""")
    Menu_Ini()