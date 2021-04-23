from Whatsapp_Bot import Whatsapp_Bot


escolher_contato = input("Digite um contato\n")
digite_messagem = input("Digite uma mensagem\n")

bot = Whatsapp_Bot(escolher_contato, digite_messagem)
bot.EnviarMensagens()