import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb 
import os
import random


Friday = pyttsx3.init() # Initialize the pyttsx3 engine
voices = Friday.getProperty('voices') # Get the available voices
Friday.setProperty('voice', voices[1].id) # voices[0]: male, voices[1]:female

commands = {
    'help' : ['help', '?', 'what can you do', 'what are your capabilities'],
    'exit_commands': ['exit', 'quit', 'bye', 'goodbye', 'see you later', 'that\'s it for now', 'stop', 'end'],
    'google': ['google', 'search for', 'search'],
    'youtube': ['yt', 'youtube', 'youtube search', 'search on youtube', 'search youtube for' ,'search on youtube for'],
    'video': ['open video', 'play video'],
    'time': ['time', 'what time is it', 'what time', 'tell me the time'],
    'weather': ['weather', 'weather report', 'weather forecast']
}


def speak(audio):
    print('F.R.I.D.A.Y: ', audio)
    Friday.say(audio)
    Friday.runAndWait() # Wait for the speech to finish

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p") #I for 12 hour format, M for minutes, p for AM/PM
    speak(Time)

def welcome():
    global name 
    name = input("Enter your name: ")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning " + name + ".")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon " + name + ".")
    else:
        speak("Good Evening " + name + ".")
    speak("How can I help you?")

def command():
    c = sr.Recognizer() # Initialize the recognizer help to recognize the speech
    with sr.Microphone() as source: # Use the microphone as the source
        c.pause_threshold = 2
        c.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = c.listen(source) # Listen to the audio
        try:
            query = c.recognize_google(audio, language='en') # Recognize the speech using Google Web Speech API
            print(name +" said: ", query)
        except sr.UnknownValueError:
            r = random.randint(0, 1)
            print("I cant hear you clearly. Please say again") if r == 0 else print("Sorry, I can't interpret what you said. Please repeat.")
            query = str(input("Your order is: "))
    return query

def command_type():
    query = input("You: ")
    return query        

if __name__ == "__main__":
    speak("Initializing Friday...")
    time()
    welcome()
    while True:
            query = command_type().lower()

            if query in commands['exit_commands']:
                r = random.randint(0, 1)
                if r == 0:
                    speak("Friday will miss you!")
                else:
                    speak(f"See you later, {name}!")
                quit()

            elif query in commands['help']:
                speak("I can Google Search, Youtube Search, Show what time is it, Tell the weather ")
                speak("That's for now. I'll learn more later on when further development is done.")

            elif query in commands['google']:
                speak("What should I search for?")
                search = command_type().lower()
                url = f"https://www.google.com/search?q={search}"
                wb.get().open(url)
                speak(f"Here is your {search} on Google")

            elif query in commands['youtube']:
                speak("What should I search for?")
                search = command_type().lower()
                url = f"https://www.youtube.com/search?q={search}"
                wb.get().open(url)
                speak(f"Here is your {search} on Youtube")

            elif query in commands['video']: 
                video_path = r"F:\Download\conheo.mp4"
                os.startfile(video_path)
                speak("Opening video...")    

            elif query in commands['time']:
                time()
            
            elif query in commands['weather']:
                speak("What city's weather should I check?")
                city = command_type().lower()
                url = f"https://www.google.com/search?q=weather+{city}"
                wb.get().open(url)
                speak(f"Here is the weather info: {city}")

            else:
                speak("Sorry I didn't understand that")
            



