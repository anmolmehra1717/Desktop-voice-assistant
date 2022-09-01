import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Sir Today is our  final project assesment day")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir")

    speak("please speak your command")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('anmolmehra4400@gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    #ask:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
            
        # 1st
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        #  2nd
        elif 'open google' in query:
            webbrowser.open("https://google.com/")
        # 3
        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/")
        # 4   
        elif 'play music' in query or 'open music' in query or 'open spotify' in query:
            webbrowser.open("https://www.spotify.com/")
        # 5
        elif 'open news' in query or 'show me some news' in query or 'tell me news' in query:
            webbrowser.open("https://1qkr8.csb.app/")
        # 6
        elif ' hows the stock market today' in query or 'stock market news' in query:
            speak("Lets find out  hows the stock market doing today")
            webbrowser.open("https://www.moneycontrol.com/stocksmarketsindia/")
        # 7
        elif 'open games' in query or 'play games' in query or 'i want to play a game' in query:
            webbrowser.open("https://shellshock.io//")
        # 8
        elif 'open my latest project' in query:
            speak("i am your latest project sir !")
        # 9
        elif 'open my university portal' in query:
            webbrowser.open("https://uims.cuchd.in/uims/")
        # 10
        elif 'open blackboard' in query:
            webbrowser.open("https://cuchd.blackboard.com/ultra/course")
        #11
        elif 'open food order website' in query or 'i want to order food' in query or 'i am hungry' in query:
            webbrowser.open("https://www.swiggy.com/")
        #12
        elif 'show me the best meme' in query or 'show me trending meme' in query or 'memes' in query or 'trending meme' in query:
            webbrowser.open("https://www.youtube.com/watch?v=V2jD7L6HfoQ")
        #13
        elif 'coding tool' in query or 'i want to code' in query:
            webbrowser.open("https://www.onlinegdb.com/online_c_compiler")
            
        #14
        elif 'who are you' in query:
                speak("Hi there, my name is jarvis. i am a voice based artificial intelligence voice assistant. I can help you in many ways. What do you want me to do now")
                
          # 15
        elif 'tell me a joke' in query:
            speak("wanna hear a joke ? YOU ")

            # 16
        elif 'who created you' in query:
            speak("i was created by mister Kanav & mister Anmol")
            webbrowser.open("https://www.instagram.com/wtfanmoll")
            webbrowser.open("https://www.instagram.com/kanavpaba")

            #17
        elif 'book a flight' in query:
            webbrowser.open("https://www.makemytrip.com/flights/")

            #18
        elif 'ipl points table' in query:
            webbrowser.open("https://www.google.com/search?q=ipl+points+table&oq=ipl+points+table&aqs=edge.0.0i131i433i512l4j0i131i433j0i433i512j0i131i433j0i131i433i512.5117j0j4&sourceid=chrome&ie=UTF-8#sie=lg;/g/11p5qpzt6t;5;/m/03b_lm1;st;fp;1;;")
            
             
             #n
        elif 'take some rest' in query:
            speak("Thankyou for giving me rest ! See you soon")
            
            break