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



dias = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-Feira', 'Sexta-feira', 'Sábado', 'Domingo']
promoção_do_dia = [
        'COMBO 1 - R$:28,00 (Batata Frita (P) + 1 Espeto de Picanha + Pão de Alho + 1 Guaraná 269ml (lata)',
        'COMBO 2 - R$:17,00 (1 Espeto de Picanha + Batata Frita (P) + 1 Guaraná 269ml (lata))',
        'COMBO 3 - R$:28,00 (File Acebolado + Batata Frita (M) + 1 Guaraná 269ml (lata))',
        'COMBO 4 - R$:17,00 (1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata)',
        'COMBO 5 - R$:17,00 (1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Guaraná 269ml (lata))',
        'COMBO 6 - R$:30,00 (Carne do Sol Acebolada + Batata Frita (M) + 1 Guaraná 269ml (lata))',
        'COMBO 7 - R$:30,00 (1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata))']


data = date.today()
indice_da_semana = data.weekday()
dia_da_semana = dias[indice_da_semana]


def vol_car():
    bot.Envia_Msg("[1]- IR PARA O CARDÁPIO")
    #bot.Envia_Msg("[2]- FAZER SEU PEDIDO")
    bot.Envia_Msg("[3]- VOLTAR AO MENU INICIAL")
    bot.Envia_Msg("** --------------------------- **")
    msg = ""  # Criando a variável msg
    while msg != "3":
        sleep(1)
        msg = bot.Ultima_Msg()  # A cada loop recebe a ultima mensagem da conversa
        if msg == "1":
            cardapio()
        if msg == "2":
            bot.Envia_Msg("falta fazer")
        elif msg == "3":
            Menu_Ini()


def car_esp():
    bot.Envia_Msg("** ESPETINHOS **")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("[1]- ESPETO DE CARNE - R$:8,00")
    bot.Envia_Msg("[2]- ESPETO DE CARNE (com creme de alho) - R$:9,50")
    bot.Envia_Msg("[3]- ESPETO DE PICANHA - R$:15,00")
    bot.Envia_Msg("[4]- ESPETO DE CUPIM - R$:13,00")
    bot.Envia_Msg("[5]- ESPETO DE CALABRESA DEFUMADA - R$:7,00")
    bot.Envia_Msg("[6]- ESPETO DE FRANGO - R$:8,00")
    bot.Envia_Msg("[7]- ESPETO DE COXINHA DE FRANGO - R$:9,50")
    bot.Envia_Msg("[8]- ESPETO DE CORAÇÃO - R$:8,00")
    bot.Envia_Msg("[9]- ESPETO DE KAFTA - R$:10,00")
    bot.Envia_Msg("[10]- ESPETO DE TOSCANA - R$:9,00")
    bot.Envia_Msg("[11]- MEDALHÃO DE CARNE - R$:13,50")
    bot.Envia_Msg("[12]- MEDALHÃO DE FRANGO - R$:11,50")
    bot.Envia_Msg("** --------------------------- **")
    vol_car()

def car_acom():
    bot.Envia_Msg("** ACOMPANHAMENTOS **")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("[1]- PÃO DE ALHO - R$:6,00")
    bot.Envia_Msg("[2]- BATATA FRITA (P) - R$:8,00")
    bot.Envia_Msg("[3]- BATATA FRITA (M) - R$:14,00")
    bot.Envia_Msg("[4]- BATATA FRITA (G) - R$:24,00")
    bot.Envia_Msg("[5]- QUEIJO ASSADO c/MELAÇO OU s/MELAÇO R$:8,00")
    bot.Envia_Msg("** --------------------------- **")
    vol_car()

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
    vol_car()

def car_combo():
    bot.Envia_Msg("** COMBOS **")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg(f"O COMBO {promoção_do_dia [indice_da_semana].split()[1]} ESTÁ EM PROMOÇÃO!!")
    bot.Envia_Msg(f"Está custando {promoção_do_dia [indice_da_semana].split()[3]}")
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
    bot.Envia_Msg("(1 Pão de Alho + 1 Espeto de Carne + 1 Espeto de Frango + 1 Espeto de Calabresa Defumada + 1 Guaraná 269ml (lata))")
    bot.Envia_Msg("** --------------------------- **")
    vol_car()

def cardapio():
    bot.Envia_Msg("** CARDÁPIO **")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("[1]- ESPETINHOS")
    bot.Envia_Msg("[2]- ACOMPANHAMENTO")
    bot.Envia_Msg("[3]- BEBIDAS")
    bot.Envia_Msg("[4]- COMBOS")
    bot.Envia_Msg("[5]- VOLTAR AO MENU INICIAL")
    bot.Envia_Msg("** --------------------------- **")
    msg = ""  # Criando a variável msg
    while msg != "5":
        sleep(1)
        msg = bot.Ultima_Msg()  # A cada loop recebe a ultima mensagem da conversa
        if msg == "1":
            car_esp()
        if msg == "2":
            car_acom()
        if msg == "3":
            car_bebida()
        if msg == "4":
            car_combo()
        elif msg == "5":
            Menu_Ini()


def promocao_do_dia():
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg(f"PROMOÇÃO DO DIA ({dia_da_semana})")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg(f"{promoção_do_dia[indice_da_semana]}")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("Dígite o número da opção desejada:")
    vol_car()

def Menu_Ini():
    bot.Envia_Msg("Dígite o número da opção desejada:")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("[1]- PROMOÇÕES DO DIA")
    bot.Envia_Msg("[2]- CARDÁPIO")
    # bot.Envia_Msg("[3]- FAZER SEU PEDIDO")
    bot.Envia_Msg("[4]- FINALIZAR ATENDIMENTO")
    bot.Envia_Msg("** --------------------------- **")
    msg = ""  # Criando a variável msg
    while msg != "4":
        sleep(1)
        msg = bot.Ultima_Msg()  # A cada loop recebe a ultima mensagem da conversa
        if msg == "1":  # Retorna uma mensagem de ajuda
            promocao_do_dia()
        if msg == "2":
            cardapio()

        elif msg == "4":  # Encerra o programa
            bot.Envia_Msg("Obrigado, volte sempre.")
            break



if __name__ == '__main__':
    bot = WhatsaapBot()  # Inicia o objeto zapbot
    bot.Abre_Conversa()  # Passando o numero ou o nome do contato
    hora = datetime.today().hour
    bot.Envia_Msg("** ESTAÇÃO DO ESPETINHO **")
    if hora < 12:
        bot.Envia_Msg("Olá Bom Dia!")
    elif hora < 18:
        bot.Envia_Msg("Olá Boa Tarde!")
    else:
        bot.Envia_Msg("Olá Boa Noite!")
    bot.Envia_Msg("Seja Bem-vindo!")
    bot.Envia_Msg("irei passar agora suas opções")
    Menu_Ini()






