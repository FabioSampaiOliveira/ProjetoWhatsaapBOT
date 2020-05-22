from selenium import webdriver
from time import sleep


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
        self.grupos_ou_pessoas = ["André Balao"]
        self.Bot_Msg = "Olá, sou o bot whatsapp! Para receber ajuda digite: help"

    def Abre_Conversa(self):
        """ Abre a conversa com um contato especifico """
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo_ou_pessoa}']")
            sleep(2)
            campo_grupo.click()

    def Envia_Msg(self, Bot_Msg):
        """ Envia uma mensagem para a conversa aberta """
        sleep(2)
        # Seleciona acaixa de mensagem
        chat_box = self.driver.find_element_by_class_name('_1Plpp')
        # Digita a mensagem
        chat_box.send_keys(Bot_Msg)
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


if __name__ == '__main__':
    bot = WhatsaapBot()  # Inicia o objeto zapbot
    bot.Abre_Conversa()  # Passando o numero ou o nome do contato
    bot.Envia_Msg()
    msg = ""  # Criando a variável msg
    while msg != "/quit":
        sleep(1)
        msg = bot.Ultima_Msg()  # A cada loop recebe a ultima mensagem da conversa
        if msg == "help":  # Retorna uma mensagem de ajuda
            bot.Envia_Msg()
            """Bot: Esse é um texto com os comandos válidos:
                help (para ajuda)
                quit (para sair)
                """

        elif msg == "quit":  # Encerra o programa
            bot.Envia_Msg("Bye bye!")