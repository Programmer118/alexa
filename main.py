import speech_recognition as sr
import pyttsx3
from pyttsx3 import engine
# import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from time import sleep
import os
import random
from tcl.Lib.django.db.backends.base import client

lis = ['sleep','stop','exit','quit','close']

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold=2
            r.energy_threshold=250
            r.dynamic_energy_threshold=150
            voice = r.listen(source)
            command = r.recognize_google(voice,language='en-in')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
            return command
            
            
    except Exception:
        return 'plz say again'
    except KeyboardInterrupt:
        exit('Process completed\n\tLogout')
    


def run_alexa():
    command = take_command()
    print(command)
    
    l=[True if i in command else False for i in lis]
    
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        # pywhatkit.playonyt(song)
    
    elif "what\'s up" in command or 'how are you' in command :
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            talk(random.choice(stMsgs))
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    
    elif 'who the heck is'  in command or 'who is' in command:
        person = command.replace('who the heck is', '').replace('who is','')
        command = command.lower()
    
        try:
                try:
                    res = client.query(command)
                    results = next(res.results).text
                    talk('WOLFRAM-ALPHA says - ')
                    talk(results)
                    print(results)
                    
                except:
                    results = wikipedia.summary(command, sentences=2)
                    talk('Got it.')
                    talk('WIKIPEDIA says - ')
                    talk(results)
                    print(results)
        except:
                webbrowser.open('www.google.com')
        
    
    elif 'date' in command:
        talk('sorry, I have a headache')
    
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    
    elif True in l:
        exit()
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    
    elif 'open' in command:
        web = command.replace(' ','').replace('open','')
        talk(f'Oppening {web}')
        webbrowser.open(f'www.{web}.com')
    
    else:
        pass
    


while True:
    run_alexa()