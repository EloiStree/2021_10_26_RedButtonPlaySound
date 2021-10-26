import keyboard  # using module keyboard
import os
import pathlib
from playsound import playsound

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('1'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
			#from playsound import playsound
			#playsound('audio.mp3')
            #file = "audio.mp3"
            #os.system("mpg123 " + file)
            str=os.path.dirname(os.path.abspath(__file__))+"\\audio.wav"
            #str="T"+pathlib.Path(__file__).parent.resolve()+'/audio.mp3'
            
            print(str)
            playsound(str)
			
            print('playing sound using  playsound')
            #break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break