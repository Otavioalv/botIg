from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from tkinter import *

import random

class InstagramBot:
    def __init__(self, username:str, password:str):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        
    def login(self):
        driver = self.driver
        driver.get('https://instagram.com')
        
        sleep(5)
        
        username_element = driver.find_element(By.NAME, 'username');
        username_element.clear()
        sleep(2)
        username_element.send_keys(self.username)
        sleep(2)
        
        password_element = driver.find_element(By.NAME, 'password')
        password_element.clear()
        sleep(2)
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        sleep(10)
        
    def find_profile(self, username):
        driver = self.driver
        url = 'https://www.instagram.com/' + username + "/followers/"
        driver.get(url)
        sleep(5)
    
    def find_video_rell(self, url):
        driver = self.driver
        sleep(6)
        driver.get(url)
        sleep(15)
        
    def button_follower(self):
        driver = self.driver
        try:
            # Espera até que o elemento <a> com href '/amazon/followers/' esteja presente
            button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/amazon/followers/')]"))
            )
            # driver.execute_script('arguments[0].click();', button)
            button.click();
            sleep(5)
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_comments(self, comments_array, amount_comments):
        for _ in range(amount_comments):
            comment = comments_array[random.randint(0, len(comments_array) - 1)]
            self.add_comment(comment)
            sleep(random.uniform(1, 2))
        

    def add_comment(self, comment):
        driver = self.driver
        try:
            sleep(random.uniform(5, 7))
            while True: 
                try: 
                    text_area = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='Adicione um comentário...']"))
                    )
                    print(text_area)
                    
                    sleep(random.uniform(5, 7))
                    text_area.send_keys(comment)
                    sleep(random.uniform(2, 3))
                    break
                except Exception as e: 
                    print(f"Houve um erro, ao tentar encontrar campo de comentario, tentando novamente...")
                    sleep(random.uniform(1, 2))
            
            while True: 
                try:
                    sleep(3)
                    publish_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Publicar') and @role='button']"))
                    )
                    
                    # < div class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37" role="button" tabindex="0">Publicar</div>
                    # publish_button = WebDriverWait(driver, 10).until(
                    #     EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'x1i10hfl') and contains(@class, 'xjqpnuy') and contains(@class, 'xa49m3k') and contains(@class, 'xqeqjp1') and contains(@class, 'x2hbi6w') and contains(@class, 'xdl72j9') and contains(@class, 'x2lah0s') and contains(@class, 'xe8uvvx') and contains(@class, 'xdj266r') and contains(@class, 'x11i5rnm') and contains(@class, 'xat24cr') and contains(@class, 'x1mh8g0r') and contains(@class, 'x2lwn1j') and contains(@class, 'xeuugli') and contains(@class, 'x1hl2dhg') and contains(@class, 'xggy1nq') and contains(@class, 'x1ja2u2z') and contains(@class, 'x1t137rt') and contains(@class, 'x1q0g3np') and contains(@class, 'x1lku1pv') and contains(@class, 'x1a2a7pz') and contains(@class, 'x6s0dn4') and contains(@class, 'xjyslct') and contains(@class, 'x1ejq31n') and contains(@class, 'xd10rxx') and contains(@class, 'x1sy0etr') and contains(@class, 'x17r0tee') and contains(@class, 'x9f619') and contains(@class, 'x1ypdohk') and contains(@class, 'x1f6kntn') and contains(@class, 'xwhw2v2') and contains(@class, 'xl56j7k') and contains(@class, 'x17ydfre') and contains(@class, 'x2b8uid') and contains(@class, 'xlyipyv') and contains(@class, 'x87ps6o') and contains(@class, 'x14atkfc') and contains(@class, 'xcdnw81') and contains(@class, 'x1i0vuye') and contains(@class, 'xjbqb8w') and contains(@class, 'xm3z3ea') and contains(@class, 'x1x8b98j') and contains(@class, 'x131883w') and contains(@class, 'x16mih1h') and contains(@class, 'x972fbf') and contains(@class, 'xcfux6l') and contains(@class, 'x1qhh985') and contains(@class, 'xm0m39n') and contains(@class, 'xt0psk2') and contains(@class, 'xt7dq6l') and contains(@class, 'xexx8yu') and contains(@class, 'x4uap5') and contains(@class, 'x18d9i69') and contains(@class, 'xkhd6sd') and contains(@class, 'x1n2onr6') and contains(@class, 'x1n5bzlp') and contains(@class, 'x173jzuc') and contains(@class, 'x1yc6y37') and @role='button' and @tabindex='0']")
                    # )
                    
                    publish_button.click()
                    break
                except Exception as e:
                    print(f"Eror ao encontrar botao de enviar comentario, tentando novamente")
                    sleep(2)
        
            sleep(5)
        except Exception as e:
            print(f"An error occoured: {e}")
    def follow_all(self):
        driver = self.driver
        
        try:
            button_list = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, '_acan') and contains(@class, '_acap') and contains(@class, '_acas') and contains(@class, '_aj1-') and contains(@class, '_ap30')]"))
            )

            seguidor = 0
            teste = 0

            while teste < 10:
                for element in button_list:
                    try:
                        driver.execute_script('arguments[0].click();', element)
                        # Aguarda um tempo aleatório entre 5 e 10 segundos
                        sleep(random.uniform(5, 10))
                        seguidor += 1
                        print(f"Seguidor número: {seguidor}")
                    except Exception as e:
                        print(f"Não foi possível seguir a pessoa: {e}")
                teste += 1
                # Atualiza a lista de botões após cada iteração
                button_list = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, '_acan') and contains(@class, '_acap') and contains(@class, '_acas') and contains(@class, '_aj1-') and contains(@class, '_ap30')]"))
                )
        except Exception as e:
            print(f"An error occurred: {e}")



class Application:
    def __init__(self, master=None):
        print("Certifique-se de que os parametros estão corretos para o bom funcionamento do BOT!!!")
            
        self.fontePadrao = ("Arial", "10")
        
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()
        
        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()
        
        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 20
        self.sextoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Bot Instagram")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.usernameLabel = Label(self.segundoContainer,text="username", font=self.fontePadrao)
        self.usernameLabel.pack(side=LEFT)

        self.username = Entry(self.segundoContainer)
        self.username["width"] = 30
        self.username["font"] = self.fontePadrao
        self.username.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha.pack(side=LEFT)
        
        
        self.linkReelLabel = Label(self.quartoContainer,text="link rell", font=self.fontePadrao)
        self.linkReelLabel.pack(side=LEFT)

        self.linkReel = Entry(self.quartoContainer)
        self.linkReel["width"] = 30
        self.linkReel["font"] = self.fontePadrao
        self.linkReel.pack(side=LEFT)
        
        
        self.amountCommentLabel = Label(self.quintoContainer,text="quantidade de comentarios", font=self.fontePadrao)
        self.amountCommentLabel.pack(side=LEFT)

        self.amountComment = Entry(self.quintoContainer)
        self.amountComment["width"] = 30
        self.amountComment["font"] = self.fontePadrao
        self.amountComment.pack(side=LEFT)


        self.iniciar = Button(self.sextoContainer)
        self.iniciar["text"] = "iniciar"
        self.iniciar["font"] = ("Calibri", "8")
        self.iniciar["width"] = 12
        self.iniciar["command"] = self.startBot
        self.iniciar.pack()

        self.mensagem = Label(self.sextoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        
    def startBot(self):
        print("BOT INICIADO");
        sleep(2)
        username = self.username.get()
        pawssword = self.senha.get()
        url_rell = self.linkReel.get()
        amount_comments = int(self.amountComment.get())
        
        comentarios = [
            "Amei essa peça!", "Super estiloso!", "Usaria muito!", "Perfeito para o verão!", 
            "Esse look é tudo!", "Maravilhoso! ", "Essa cor é incrível! ", "Ficou lindo em você!", 
            "Preciso de um desses!", "Chique demais!", "Simplesmente lindo! ", "Esse estilo é demais!", 
            "Elegante e moderno!", "Adorei o design!", "Ficou perfeito! ", "Combina com tudo! ", 
            "Essa estampa é linda!", "Muito fashion!", "Quero um igual! ", "Esse look é um arraso!", 
            "Puro glamour!", "Muito fofo!", "Essa peça é única! ", "Amei o tecido!", "Es1tiloso e confortável! "
        ]
        
        Bot = InstagramBot(username, pawssword);
        Bot.login();
        Bot.find_video_rell(url_rell)
        Bot.add_comment("comentario");
        Bot.add_comments(comentarios, amount_comments)
        print("BOT FINALIZADO");

    def print_teste(self):
        print(self.username.get())
        print(self.senha.get())
        print(self.linkReel.get())
        print(self.amountComment.get())
    
    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"


# username = "skyfall6582"
# pawssword = "1510@Sky"
# user_profile = "felps11"
# url_rell = "https://www.instagram.com/reel/C2SG7oBuy6O/?igsh=MXZsdDFhazJkaWJmcw%3D%3D"
# comentarios = [
#     "Amei essa peça!", "Super estiloso!", "Usaria muito!", "Perfeito para o verão!", 
#     "Esse look é tudo!", "Maravilhoso! ", "Essa cor é incrível! ", "Ficou lindo em você!", 
#     "Preciso de um desses!", "Chique demais!", "Simplesmente lindo! ", "Esse estilo é demais!", 
#     "Elegante e moderno!", "Adorei o design!", "Ficou perfeito! ", "Combina com tudo! ", 
#     "Essa estampa é linda!", "Muito fashion!", "Quero um igual! ", "Esse look é um arraso!", 
#     "Puro glamour!", "Muito fofo!", "Essa peça é única! ", "Amei o tecido!", "Es1tiloso e confortável! "
# ]



if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()
    
    
    # Bot = InstagramBot(username, pawssword);
    # Bot.login();
    # Bot.find_video_rell(url_rell)
    # Bot.add_comment("comentario");
    # Bot.add_comments(comentarios, 100)

    # Bot.find_profile(user_profile)
    # Bot.button_follower()
    # Bot.follow_all()


    print("Bot finalizado com sucesso")
        
        
        
    