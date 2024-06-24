import random
import sys
import webbrowser

import speech_recognition as sr
import pyttsx3
import openai
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys




# Initialize Text-to-Speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)
# Function to speak out the response
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# voice to text


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 2
        audio = r.listen(source,timeout=5,phrase_time_limit=5)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language= 'en-in')
            print(f"user said: {query}")

        except Exception as e:
            speak("Say that again please...")
            return "none"
        return query


# wish function

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>= 0 and hour<= 12:
       speak("good morning")
    elif hour> 12 and hour< 18:
       speak("good afternoon")
    else:
       speak("good evening")
    speak("i am cooper sir. please tell me how can i help you?")



if __name__ == "__main__":
  wish()
  # while True:
  if 1:
      query= takecommand().lower()

      #logic for task
      if "open notepad" in query:
         npath = "C:\\Windows\\System32\\notepad.exe"
         os.startfile(npath)

      elif "open chrome" in query:
          apath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
          os.startfile(apath)

      elif "open telegram" in query:
          cpath = "C:\\Users\\vansh\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
          os.startfile(cpath)

      elif "open command prompt" in query:
          os.system("start cmd")

      elif "open camera" in query:
          cap = cv2.VideoCapture(0)
          while True:
              ret, img = cap.read()
              cv2.imshow('webcam', img)
              k = cv2.waitKey(50)
              if k==27:
                  break;
          cap.release()
          cv2.destroyAllWindows()

      elif "play music" in query:
          music_dir="C:\\Users\\vansh\\Music"
          songs = os.listdir(music_dir)
          rd = random.choice(songs)
          for song in songs:
              if song.endswith('.mp3'):
                 os.startfile(os.path.join(music_dir, song))

      elif "ip address" in query:
          ip= get('https://api.ipify.org').text
          speak(f"Your IP address is {ip}")

      elif "wikipedia" in query:
          speak("searching wikipedia....")
          query = query.replace("wikipedia","")
          results = wikipedia.summary(query, sentences=3)
          speak("according to wikipedia")
          speak(results)
          #print(results)

      elif "open youtube" in query:
          url = "https://www.youtube.com"
          chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
          webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
          webbrowser.get('chrome').open(url)

      elif "open chess" in query:
          url = "https://www.chess.com"
          chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
          webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
          webbrowser.get('chrome').open(url)

      elif "open ai" in query:
          url = "https://chat.openai.com"
          chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
          webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
          webbrowser.get('chrome').open(url)

      elif "open insta" in query:
          url = "https://www.instagram.com"
          chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
          webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
          webbrowser.get('chrome').open(url)

      elif "open google" in query:
          url = "https://www.google.com"
          chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
          webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
          webbrowser.get('chrome').open(url)


  def listen():
      recognizer = sr.Recognizer()
      with sr.Microphone() as source:
          recognizer.adjust_for_ambient_noise(source)
          print("Listening...")
          audio = recognizer.listen(source)
      try:
          print("Recognizing...")
          user_input = recognizer.recognize_google(audio)
          print("You said:", user_input)
          return user_input
      except sr.UnknownValueError:
          speak("Sorry, I couldn't understand what you said.")
          return ""
      except sr.RequestError as e:
          speak("Sorry, I encountered an error while processing your request. Please try again later.")
          return ""


  if __name__ == "__main__":
      speak("What would you like to do? You can tell me a command or say 'exit' to quit the program.")

      while True:
          user_input = listen()
          if user_input.lower() == "exit":
              speak("Exiting the program.Have a Great Day Sir!")
              break
          elif user_input:
              speak("You said: " + user_input)





