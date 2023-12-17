from cx_Freeze import setup, Executable
  
executables = [
        Executable(script = "main.py", base = "Win32GUI" )
]
# ne pas mettre "base = ..." si le programme n'est pas en mode graphique, comme c'est le cas pour chiffrement.py.
  
buildOptions = dict( 
        includes = ["kivy.app","kivy.uix.gridlayout","kivy.uix.label","kivy.uix.textinput","kivy.uix.button","kivy.uix.widget","speech_recognition","pyttsx3"]
        
)
  
setup(
    name = "3e Degre",
    version = "1.0",
    description = "Ce programme renvoie la solution d'un polynome de 3e degre",
    author = "Mouhamed",
    options = dict(build_exe = buildOptions),
    executables = executables
)