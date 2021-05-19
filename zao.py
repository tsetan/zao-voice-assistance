import pyttsx3 #convert text to speech
import speech_recognition as sr #convert speech to text
import datetime #date and time
import win32api # have to import with pyttsx3 if on windows 
import wikipedia # wikipedia searches 
import webbrowser #browser
import os #operating system
import pyjokes #python jokes


engine = pyttsx3.init('sapi5') # init function to get an engine instance for the speech synthesis
#sapi5 is Microsoft speech application platform interface we will be using this for text to speech function.
voices = engine.getProperty('voices')  # 0 for male , 1 for female
engine.setProperty('voice', voices[0].id) # setting voice


def speak(audio): #function called speak()
    engine.say(audio) # text po zer nok speak() na de kan bo
    engine.runAndWait() # run and wait method, it processes the voice commands.


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    print("I am zago . Please tell me how may I help you , I can assist you with Web browser \nTime \nPlaying music \nTelling jokes \nWikipedia searches \nOpening social media ")
    speak("I am zago . Please tell me how may I help you , I can assist you with web browser , date and time , playing music ,telling jokes, wikipedia searches , opening social media ")

def takeCommand():  #It takes microphone input from the user and returns string output
    ''' takeCommand() function,  awill return a string output by taking microphone input from the user.
    Before defining the takeCommand() function, we need to install a module called speechRecognition'''
    r = sr.Recognizer()  #helps to recognize the audio
    with sr.Microphone() as source: #using microphone as source
        print("Listening...")
        r.pause_threshold = 1   # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source) # functions from speech recognisation

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query



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


