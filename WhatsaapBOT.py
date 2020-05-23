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


def cardapio():
    bot.Envia_Msg("** CARDÁPIO **")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("[1]- ESPETINHOS")
    bot.Envia_Msg("[2]- ACOMPANHAMENTO")
    bot.Envia_Msg("[3]- BEBIDAS")
    bot.Envia_Msg("[4]- COMBOS")
    bot.Envia_Msg("[5]- VOLTAR AO MENU INICIAL")
    bot.Envia_Msg("** --------------------------- **")


def promocao_do_dia():
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg(f"PROMOÇÃO DO DIA ({dia_da_semana})")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg(f"{promoção_do_dia[indice_da_semana]}")
    bot.Envia_Msg("** --------------------------- **")


if __name__ == '__main__':
    bot = WhatsaapBot()  # Inicia o objeto zapbot
    bot.Abre_Conversa()  # Passando o numero ou o nome do contato
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("Dígite uma das opções:")
    bot.Envia_Msg("** --------------------------- **")
    bot.Envia_Msg("[1]- PROMOÇÕES DO DIA")
    bot.Envia_Msg("[2]- CARDÁPIO")
    # bot.Envia_Msg("[3]- FAZER SEU PEDIDO")
    bot.Envia_Msg("[4]- FINALIZAR ATENDIMENTO")
    bot.Envia_Msg("** --------------------------- **")
    msg = ""  # Criando a variável msg
    dias = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-Feira', 'Sexta-feira', 'Sábado', 'Domingo']
    data = date.today()
    indice_da_semana = data.weekday()
    dia_da_semana = dias[indice_da_semana]
    while msg != "4":
        sleep(1)
        msg = bot.Ultima_Msg()  # A cada loop recebe a ultima mensagem da conversa
        if msg == "1":  # Retorna uma mensagem de ajuda
            promocao_do_dia()
        if msg == "2":
            cardapio()

        elif msg == "4":  # Encerra o programa
            bot.Envia_Msg("Bye bye!")







