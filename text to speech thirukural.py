from gtts import gTTS   # we have to import this module for google text to translate 
import os   #Python OS module provides the facility to establish the interaction between the user and the operating system

#a=open('thirukural.txt')
#text=a.read()

text='கேடில் விழுச்செல்வம் கல்வி யொருவற்கு மாடல்ல மற்றை யவை' #text to be translated
language='ta' # mentioning the language
obj=gTTS(text= text,lang=language,slow=False)  # mentioning the parameters

obj.save('thirukural.mp3')  #to save the mp3 file
os.system('thirukural.mp3')  #os.system() is used to execute a command.