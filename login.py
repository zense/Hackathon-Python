from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import speech_recognition as s
import pyttsx3
import string


class Bot():
    def speech_recog_uname(self):
        try:
            with s.Microphone() as source:
                voice_msg = self.hear.listen(source)
                info = self.hear.recognize_google(voice_msg,language='en-in').lower()
                if 'dollar' in info:
                    info=info.replace('dollar','$')
                if ' ' in info:
                    info=info.replace(' ','')
                if "at the rate" in info:
                    info=info.replace("at the rate","@")
                return(info)
        except:
            return("Couldn't hear you try again")
    def speech_recog_pwd(self):
        try:
            with s.Microphone() as source:
                voice_msg1 = self.hear.listen(source)
                info1 = self.hear.recognize_google(voice_msg,language='en-in')
                if 'dollar' in info1:
                    info1=info1.replace('dollar','$')
                if ' ' in info:
                    info1=info1.replace(' ','')
                return(info1)
        except:
            return("Couldn't hear you")
    
    def __init__(self):
        self.engine=pyttsx3.init()
        self.engine.say("What is your Username")
        self.engine.runAndWait()
        self.hear=s.Recognizer()
        #The below lines are for username and password for speech recognition
        #self.username = Bot.speech_recog_uname(self)
        #print(self.username)
        #self.password = Bot.speech_recog_pwd(self)
        #print(self.password)
        self.username=input()
        self.engine.say("What is your password")
        self.engine.runAndWait()
        self.password=input()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        Bot.rediffmail(self)
    
    def working_in_mail(self):
        try:
            with s.Microphone() as source:
                command = self.hear.listen(source)
                info2 = self.hear.recognize_google(command,language='en-in').lower()
                return(info2)
        except:
            self.engine.say("Couldn't hear you")
    
    def mailfunction(self):
        self.engine.say("To send an email say send")
        self.engine.runAndWait()
        func=Bot.working_in_mail(self)
        #func='send'
        if 'send' in func:
            s=self.driver.find_element_by_xpath('//*[@id="boxscroll"]/li[1]/a')
            s.click()
            self.engine.say("To whom do you want to send the mail")
            self.engine.runAndWait()
            email_dict = {
                'surya': 'suryavamsikalaga@gmail.com'
            }
            name=email_dict[Bot.speech_recog_uname(self)]
            a=self.driver.find_element_by_xpath('//*[@id="TO_IDcmp2"]')
            a.click()
            name = 'suryavamsikalaga@gmail.com'
            a.send_keys(name)
            #self.engine.say("What is the subject of this mail")
            #self.engine.runAndWait()
            #sub1=self.driver.find_elements_by_xpath('//*[@id="rd_compose_cmp2"]/ul/li[4]/input')
            #sub1.click()
            #sub=Bot.working_in_mail(self) 
            #sub1.send_keys(sub)
            self.engine.say("Please tell your body of the mail")
            self.engine.runAndWait()
            msg=Bot.working_in_mail(self)
            msg1=self.driver.find_element_by_xpath('/html')
            msg1.click()
            msg1.send_keys(msg)
            sent=self.driver.find_element_by_xpath('//*[@id="rd_compose_cmp2"]/div[1]/a[1]')
            sent.click()
            yes=self.driver.find_element_by_xpath('//*[@id="jqi_state0_buttonYes"]')
            yes.click()

    def rediffmail(self):
        self.driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
        user_name = self.driver.find_element_by_xpath('//*[@id="login1"]')
        user_name.click()
        user_name.send_keys(self.username)
        pwd = self.driver.find_element_by_xpath('//*[@id="password"]')
        pwd.click()
        pwd.send_keys(self.password)

        login = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input[2]')
        login.click()
        try:
            skip = self.driver.find_element_by_xpath('/html/body/div/div[3]/div/form/div[7]/a')
            skip.click()
        except:
            pass
        Bot.mailfunction(self)
    


bot = Bot()

