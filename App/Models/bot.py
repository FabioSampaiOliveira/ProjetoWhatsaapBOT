from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pickle

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
        self.driver.implicitly_wait(2)
        while self.driver.find_elements_by_xpath("//canvas"):pass

    def Abre_Conversa(self, contato):
        self.driver.find_element_by_class_name("_2S1VP").send_keys(contato)
        sleep(2)
        self.driver.find_element_by_xpath("//span[@title = '{}']".format(contato)).click()

    def Envia_Msg(self, msg):
        #Envia uma mensagem para a conversa aberta
        chat_box = self.driver.find_element_by_class_name('_1Plpp')
        for linha in msg.split("\n"):
            chat_box.send_keys(linha)
            chat_box.send_keys(Keys.SHIFT + Keys.ENTER)
        #envia mensagem
        self.driver.find_element_by_xpath("//span[@data-icon='send']").click()
        #chat_box.send_keys(Keys.ENTER)
        
    def sair(self):
        self.driver.quit

    def Ultima_Msg(self, mensagem=""):
        #Captura a ultima mensagem da conversa
        if mensagem != "":
            self.Envia_Msg(mensagem)
        post = self.driver.find_elements_by_class_name("_3_7SH")
        # O texto da ultima mensagem
        texto = post[-1].find_element_by_css_selector("span.selectable-text").text
        return texto
    
    def capturaTelefone(self):
        self.driver.find_element_by_xpath("//div[@class='_5SiUq']").click()
        sleep(0.5)
        telefone = self.driver.find_element_by_xpath("//span[contains(text(),'+')]").text
        self.driver.find_element_by_xpath("//span[@data-icon='x']").click()
        return telefone
    
    def watch(self):
        conversasDisponiveis = self.driver.find_elements_by_xpath("//div[@class='_3j7s9']//span[@class='OUeyt']/ancestor::div[@class='_3j7s9']")
        while not conversasDisponiveis:
            conversasDisponiveis = self.driver.find_elements_by_xpath("//div[@class='_3j7s9']//span[@class='OUeyt']/ancestor::div[@class='_3j7s9']")

        conversasDisponiveis[0].click()
    
