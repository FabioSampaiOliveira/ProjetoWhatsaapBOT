from selenium import webdriver
from time import sleep
from datetime import datetime

class WhatsappBot:
    def __init__(self):
        hora = datetime.today().hour
        self.mensagem1 = "* ESTAÇÃO DO ESPETINHO *"
        if hora < 12:
            self.mensagem2 = "Olá Bom Dia!"
        elif hora < 18:
            self.mensagem2 = "Olá Boa Tarde!"
        else:
            self.mensagem2 = "Olá Boa Noite!"
        self.mensagem3 ="Seja Bem-vindo!"
        self.mensagem4 = "me chamo * Ana *!"
        self.mensagem5 = "Sou sua atendente virtual!!"
        self.mensagem6 = "irei passar agora suas opções:"
        self.grupos_ou_pessoas = ["ZapBOT"]                                      # Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')                                       # coloca em português Brasil
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=options)   #local onde vc colocou seu chromedriver.exe

    def EnviarMensagens(self):
        def send():                                                                 #aqui é a função de enviar a mensagem
            sleep(1,5)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            botao_enviar.click()

        self.driver.get('https://web.whatsapp.com')
        sleep(10)
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo_ou_pessoa}']")  #aqui é para quem ele vai mandar
            sleep(2)
            campo_grupo.click()
            chat_box = self.driver.find_element_by_class_name('_1Plpp')     #aqui é onde vc dígita sua mensagem
            chat_box.click()                                                #aqui ele vai clicar no chat box
            chat_box.send_keys(self.mensagem1)
            send()
            chat_box.send_keys(self.mensagem2)
            send()
            chat_box.send_keys(self.mensagem3)
            send()
            chat_box.send_keys(self.mensagem4)
            send()
            chat_box.send_keys(self.mensagem5)
            send()
            chat_box.send_keys(self.mensagem6)
            send()
            sleep(10)
            self.driver.quit()                          # fecha a página



bot = WhatsappBot()
bot.EnviarMensagens()


#<div class="_3_7SH _3DFk6" role="text">span mas já é um começo                 # aqui é onde a mensagem recebida chega (irei usar no futuro)
