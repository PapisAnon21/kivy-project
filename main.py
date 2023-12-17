# appliction say and read
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
#from kivy.properties import ListProperty
from kivy.uix.widget import Widget
import speech_recognition as sr
import pyttsx3
parleur = pyttsx3.init()
reconnaitre = sr.Recognizer()
# dans le init on mettrea tous nos widgets
# d'autre part on mettra nos fonctions
# Gridlayout est la disposition de nis widget en grille
class LoginScreen(GridLayout):  #<div class="banniere">

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 4
        parleur = Button(text='Dire votre texte' , size_hint = (.3,.2), pos_hint ={'x':0, 'top':1})
        parleur.bind(on_press = self.ecoute)
        self.add_widget(parleur)
        self.text_transcris = TextInput(multiline=True, text = '' , use_bubble = True)
        self.add_widget(self.text_transcris)
        self.add_widget(Label(text = '_____________________________________'))
        self.add_widget(Label(text = '______________________________________'))
        Lecteur = Button(text = 'Lire le Texte')
        Lecteur.bind(on_press = self.lire)
        self.add_widget(Lecteur)
        self.texte_a_lire = TextInput(multiline = True  , text = '' , use_bubble = True)
        self.add_widget(self.texte_a_lire)
        self.add_widget(Label(text = 'Developpeur :'))
        self.add_widget(Label(text = 'Mouhamed Dieng --- Startup: Club Des Amis Codeurs'))

        #self.add_widget(Label(text='password'))
        #self.password = TextInput(password=True, multiline=False)
        #self.add_widget(self.password)
        #self.mon = Label(text = '')
        #bouton = Button(text = 'appuyer')
        #bouton.bind(on_press = self.f)
        #self.add_widget(bouton)

    def ecoute(self,deglou): 

        with sr.Microphone() as son:
        	audio = reconnaitre.listen(son)
        	try:
        		texte = reconnaitre.recognize_google(audio , language ="fr-FR")
        		self.text_transcris.text = texte
        		print(texte)
        	except:
        		self.text_transcris.text = 'Veillez reesayer svp'
        		print("veuu")
    def lire(self , liral):
    	if len(self.texte_a_lire.text) != 0:
    		lire = self.texte_a_lire.text
    		parleur.say(lire)
    		parleur.runAndWait()


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()

# construction d'un systeme de connexion sans efffet