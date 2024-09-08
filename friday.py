import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb 
import os


Friday = pyttsx3.init() # Initialize the pyttsx3 engine
voices = Friday.getProperty('voices') # Get the available voices
Friday.setProperty('voice', voices[0].id) # Set the voice to the second voice in the list voices[0], voices[1]


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
            print("I cant hear you clearly.")
            query = str(input("Your order is: "))
    return query
        

if __name__ == "__main__":
    welcome()
    while True:
            query = command().lower()

            if "what can you do" in query:
                speak("I can Google Search, Youtube Search, Show what time is it.")
                speak("I'll learn more.")

            elif "google" in query:
                speak("What should I search for?")
                search = command().lower()
                url = f"https://www.google.com/search?q={search}"
                wb.get().open(url)
                speak(f"Here is your {search} on Google")

            elif "youtube" in query:
                speak("What should I search for?")
                search = command().lower()
                url = f"https://www.youtube.com/search?q={search}"
                wb.get().open(url)
                speak(f"Here is your {search} on Youtube")

            elif "open video" in query: 
                video_path = r"F:\Download\conheo.mp4"
                os.startfile(video_path)
                speak("Opening video...")
            
            elif "quit" in query or "exit" in query:
                speak("Friday will miss you !")
                quit()

            elif "time" in query:
                time()

            else:
                speak("I cant do that.")
            



