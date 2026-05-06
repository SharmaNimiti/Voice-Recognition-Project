import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import sys
import smtplib
from ecapture import ecapture as ec
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Pre-defined user voiceprints (for demonstration purposes)
user_voiceprints = {
    "user1": "hello",
    "user2": "kese ho"
}

# Function for voice-based authentication
def voice_authentication():
    with sr.Microphone() as source:
        print("Speak your passphrase for authentication:")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen for audio input
        
        try:
            print("Recognizing...")
            passphrase = recognizer.recognize_google(audio)  # Use Google Web Speech API for recognition
            if passphrase in user_voiceprints.values():
                for user, voiceprint in user_voiceprints.items():
                    if voiceprint == passphrase:
                        print("Authentication successful. Welcome,", user)
                        return True
            else:
                print("Authentication failed. Please try again.")
                return False
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return False
        except sr.RequestError as e:
            print("Could not request results from Google Web Speech API; {0}".format(e))
            return False

# Function to perform an action after successful authentication
def perform_action():
    print("Authenticated action performed.")

# Main function
def main():
    authenticated = False
    while not authenticated:
        authenticated = voice_authentication()
    perform_action()

# Call the main function
main()

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

    speak("I am Nimiti. Please tell me how may I help you")       

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
    server.login('your-email', ' your-password')
    server.sendmail('email', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        elif " the wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")       

        elif 'open' in query:
            webbrowser.open("https://usci.karnavatiuniversity.edu.in/")    

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0  ,"robo camera","img.jpg")


        elif 'email to pallavi' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pallavi.diligence@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry mam. I am not able to send this email")


        elif ('band ho jao','quit','exit'):
            speak('Haji sir bye sir')
            sys.exit()