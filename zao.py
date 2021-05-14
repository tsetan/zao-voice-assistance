import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import win32api
import wikipedia
import webbrowser
import os
import PyInstaller
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Hanupa Tundup. Please tell me how may I help you , I can assist you with web browser , date and time , playing music ,telling jokes, wikipedia searches , opening social media and sending e mails ")

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
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query=query.replace("'wikipedia"," ")
            result   = wikipedia.summary(query,sentences=2)
            speak('According to Wikipedia...')
            print(result)
            speak(result)

        elif 'open youtube'in query:
            webbrowser.open("youtube.com")

        elif "how are you" in query:
            speak('I am good , how are you ')
        
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.in")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'play music' in query:
            music_dir="C:\\Users\\tseta\\OneDrive\\Desktop\\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            
        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")


        elif 'quit' in query or 'exit' in query:
            speak("Thanks for giving me your time")
            quit()

        else:
            speak("sorry please say it again")

