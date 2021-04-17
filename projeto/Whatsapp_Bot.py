from selenium import webdriver
import time


class Whatsapp_Bot:

    def __init__(self, grupos, messages):
        self.grupos =[grupos]
        self.message = messages
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'Scripts\chromedriver.exe')

    def EnviarMensagens(self):
        #<span dir="auto" title="TESTE" class="_35k-1 _1adfa _3-8er">TESTE</span>
        #<div tabindex="-1" class="_1JAUF _2x4bz">
        #<span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            grupo.click()
            time.sleep(3)
            chat_box = self.driver.find_element_by_class_name('_2A8P4')
            chat_box.click()
            time.sleep(3)
                #chat_box.send_keys(repr(self.message)) ---> funciona
            mensagem = repr(self.message).replace("'","")
            chat_box.send_keys(mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            botao_enviar.click()
            time.sleep(5)
