import pyttsx3
import speech_recognition as sr
import datetime
import os

mya = pyttsx3.init('sapi5')

voices = mya.getProperty('voices')
mya.setProperty('voices' , voices[0].id)



def speak(audio):
    mya.say(audio)
    print(audio)
    mya.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("lisening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
        
    try:
        print("recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}")
    except Exception as e:
        speak("Say that again please")
        return None
    return query    

def wish():
    hour = int(datetime.datetime.now().hour)   
    
    if hour >=8 and hour <= 12:
        speak("good morning sir")
        
    elif hour >= 12 and hour <= 18:
         speak("good afternon sir")
    else:
        speak("good evening sir")  
    speak("i am Edith please tell me what can i do for you")    
if __name__ == '__main__': 
    wish() 
    while True:
        
        
        query=takecommand().lower()
        
        
        
        if "open google" in query:
            path = "C:\\Users\\Electrobt\\Desktop\\poorni\\prepared\\22.jpg"
            os.system("start cmd")
           
             
                
        else:
            speak("say something")
           
            
           
           
           