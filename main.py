import speech_recognition as sr  # Import the speech recognition library
import webbrowser  # Import the webbrowser module for opening websites
import pyttsx3
import os   # Import the text-to-speech conversion library
# Define a function to list all music files in a specified folder

import requests

import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')
import gradio as gr
# from keys import newsapi,weatherapi
def get_weather(city):
      # Change to your city
    api_key = os.getenv('weatherapi')  # Make sure to set your API key in the environment
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        # Extract relevant information
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        # Format the weather report
        weather_report = (
            f"The current temperature in {city} is {temperature}°C, "
            f"feels like {feels_like}°C with {weather_description}. "
            f"The humidity is {humidity}% and the wind speed is {wind_speed} m/s."
        )
        
        speak(weather_report)  # Use your existing speak function
    else:
        speak("Sorry, I couldn't fetch the weather information.")

def speak(text):
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    engine.say(text)  # Make the engine say the text
    engine.runAndWait()  # Block while processing all the commands in the queue

def clean_text(text):
    return text.replace('*', '')  # Remove asterisks from the text

def AIprocess(c):
    API_KEY = os.getenv('GEMINI_API_KEY')

    genai.configure(
        api_key=API_KEY
    )

    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat(history=[])

    response_limit = 1  # Set a limit for the number of responses
    response_count = 0

    while response_count < response_limit:
        user_input = c
        if user_input.lower() == "exit":
            print("thanks for using jarvis")
            speak("thanks for using jarvis")
            break
        try:
            response = chat.send_message(user_input)
            print('\n')
            x = response.text
            
            # Clean the response text to remove asterisks
            cleaned_response = clean_text(x)
            
            print(cleaned_response)  # Print the cleaned response
            speak(cleaned_response)  # Ensure the assistant speaks the cleaned response
            
            response_count += 1  # Increment the response counter
        except genai.generation_types.StopCandidateException as e:
            print(f"Model stopped early. Reason: {e.candidate.finish_reason}")
            break  # Break the loop if the model stops early
    return cleaned_response

def processCommand(c):
    c = c.lower()  # Convert the command to lowercase once

    if c.startswith("open google"):
        webbrowser.open("https://www.google.com")
    elif c.startswith("open youtube"):
        webbrowser.open("https://www.youtube.com")
    elif c.startswith("open wikipedia"):
        webbrowser.open("https://www.wikipedia.org")
    elif c.startswith("open stackoverflow"):
        webbrowser.open("https://www.stackoverflow.com")
    elif c.startswith("open github"):
        webbrowser.open("https://www.github.com")
    elif c.startswith("open google maps"):
        webbrowser.open("https://www.google.com/maps")
    elif c.startswith("open google images"):
        webbrowser.open("https://www.google.com/images")
    elif c.startswith("open google news"):
        webbrowser.open("https://www.google.com/news")
    elif c.startswith("open google drive"):
        webbrowser.open("https://www.google.com/drive")
    elif c.startswith("open google calendar"):
        webbrowser.open("https://www.google.com/calendar")
    elif c.startswith("open google classroom"):
        webbrowser.open("https://www.google.com/classroom")
    elif c.startswith("open netflix"):
        webbrowser.open("https://www.netflix.com")
    elif c.startswith("open amazon"):
        webbrowser.open("https://www.amazon.com")
    elif c.startswith("open wwe"):
        webbrowser.open("https://www.wwe.com")
    elif c.startswith("open youtube music"):
        webbrowser.open("https://www.youtube.com/feed/music")
    elif c.startswith("open youtube movies"):
        webbrowser.open("https://www.youtube.com/feed/movies")
    elif c.startswith("open youtube sports"):
        webbrowser.open("https://www.youtube.com/feed/sports")
    elif c.startswith("open vs code"):
        webbrowser.open("https://code.local")
    elif c.startswith("open replit"):
        webbrowser.open("https://replit.com")
    elif c.startswith("open google docs"):
        webbrowser.open("https://docs.google.com")
    elif c.startswith("open google sheets"):
        webbrowser.open("https://docs.google.com/spreadsheets")
    elif c.startswith("open google slides"):
        webbrowser.open("https://docs.google.com/presentation")
    elif c.startswith("open google photos"):
        webbrowser.open("https://photos.google.com")
    elif c.startswith("open brave"):
        webbrowser.open("https://brave.com")
    elif c.startswith("open brave search"):
        webbrowser.open("https://search.brave.com")
    elif c.startswith("open whatsapp"):
        webbrowser.open("https://web.whatsapp.com")
    elif c.startswith("open microsoft edge"):
        webbrowser.open("https://www.microsoft.com/en-us/edge")
    elif c.startswith("open microsoft word"):
        webbrowser.open("https://www.microsoft.com/en-us/microsoft-365/word")
    elif c.startswith("open microsoft excel"):
        webbrowser.open("https://www.microsoft.com/en-us/microsoft-365/excel")
    elif c.startswith("open microsoft powerpoint"):
        webbrowser.open("https://www.microsoft.com/en-us/microsoft-365/powerpoint")
    elif c.startswith("open microsoft outlook"):
        webbrowser.open("https://www.microsoft.com/en-us/microsoft-365/outlook")
    elif c.startswith("open microsoft teams"):
        webbrowser.open("https://www.microsoft.com/en-us/microsoft-365/teams")
    elif c.startswith("open microsoft office"):
        webbrowser.open("https://www.microsoft.com/en-us/microsoft-365/microsoft-office")
    elif c.startswith("open microsoft azure"):
        webbrowser.open("https://azure.microsoft.com")
    elif c.startswith("open aws"):
        webbrowser.open("https://aws.amazon.com")
    elif c.startswith("open facebook"):
        webbrowser.open("https://www.facebook.com")
    elif c.startswith("open twitter"):
        webbrowser.open("https://www.twitter.com")
    elif c.startswith("open instagram"):
        webbrowser.open("https://www.instagram.com")
    elif c.startswith("open linkedin"):
        webbrowser.open("https://www.linkedin.com")
    elif c.startswith("open pinterest"):
        webbrowser.open("https://www.pinterest.com")
    elif c.startswith("open snapchat"):
        webbrowser.open("https://www.snapchat.com")
    elif c.startswith("open tiktok"):
        webbrowser.open("https://www.tiktok.com")
    elif c.startswith("open reddit"):
        webbrowser.open("https://www.reddit.com")
    elif c.startswith("open tumblr"):
        webbrowser.open("https://www.tumblr.com")
    elif c.startswith("open flickr"):
        webbrowser.open("https://www.flickr.com")
    elif c.startswith("open cnn"):
        webbrowser.open("https://www.cnn.com")
    elif c.startswith("open bbc news"):
        webbrowser.open("https://www.bbc.com/news")
    elif c.startswith("open new york times"):
        webbrowser.open("https://www.nytimes.com")
    elif c.startswith("open the guardian"):
        webbrowser.open("https://www.theguardian.com")
    elif c.startswith("open fox news"):
        webbrowser.open("https://www.foxnews.com")
    elif c.startswith("open nbc news"):
        webbrowser.open("https://www.nbcnews.com")
    elif c.startswith("open al jazeera"):
        webbrowser.open("https://www.aljazeera.com")
    elif c.startswith("open reuters"):
        webbrowser.open("https://www.reuters.com")
    elif c.startswith("open cnbc"):
        webbrowser.open("https://www.cnbc.com")
    elif c.startswith("open washington post"):
        webbrowser.open("https://www.washingtonpost.com")
    elif c.startswith("open khan academy"):
        webbrowser.open("https://www.khanacademy.org")
    elif c.startswith("open coursera"):
        webbrowser.open("https://www.coursera.org")
    elif c.startswith("open edx"):
        webbrowser.open("https://www.edx.org")
    elif c.startswith("open udemy"):
        webbrowser.open("https://www.udemy.com")
    elif c.startswith("open chatgpt"):
        webbrowser.open("https://chat.openai.com")
    elif c.startswith("open flipkart"):
        webbrowser.open("https://www.flipkart.com")



    ##Adding Music
    elif c.startswith("play alone"):
        webbrowser.open("https://www.youtube.com/watch?v=1p3vcRhsYGo")
    elif c.startswith("play perfect"):
        webbrowser.open("https://www.youtube.com/watch?v=2Vv-BfVoq4g")
    elif c.startswith("play darkside"):
        webbrowser.open("https://www.youtube.com/watch?v=M-P4QBt-FWw")
    elif c.startswith("play sing me to sleep"):
        webbrowser.open("https://www.youtube.com/watch?v=2i2khp_npdE")
    elif c.startswith("play on my way"):
        webbrowser.open("https://www.youtube.com/watch?v=dhYOPzcsbGM")
    elif c.startswith("play the spectre"):
        webbrowser.open("https://www.youtube.com/watch?v=wJnBTPUQS5A")
    elif c.startswith("play all falls down"):
        webbrowser.open("https://www.youtube.com/watch?v=6RLLOEzdxsM")
    elif c.startswith("play diamond heart"):
        webbrowser.open("https://www.youtube.com/watch?v=KWehlr9H4gM")
    

    
  
        



    #Adding news
      
    elif "news" in c.lower():
        newsapi = os.getenv('newsapi')
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        data=r.json()
        for i in range(5):
            print(data['articles'][i]['title'])
            speak(data['articles'][i]['title'])

    #Adding weather
    # elif "weather" in c.lower():
    #     weatherapi = os.getenv('weatherapi')
    #     r=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid={weatherapi}")
    #     data=r.json()
    #     print(data)
    #     speak(data['weather'][0]['description'])
    elif "weather " in c.lower():
        speak("Which city's weather do you want to know? ")
        with sr.Microphone() as source:
            audio = r.listen(source)
        city = r.recognize_google(audio)
        output = get_weather(city)
        print(output)
        speak(output)

    else:
        output= AIprocess(c)
        print(output)
        speak(output)



if __name__ == "__main__":
    print("initializing jarvis....")  # Print initialization message
    speak("initializing jarvis....")  # Use the speak function to say initialization message

    while True:
        # Initialize the speech recognizer
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:  # Use the default microphone as the audio source
                print("Listening...")  # Prompt the user to say something
                audio = r.listen(source,timeout=2,phrase_time_limit=2)  # Listen for the first phrase and extract it into audio data
        # Attempt to recognize speech using Google's speech recognition
            print("Recognizing...")
            word=r.recognize_google(audio)
            print(word)

            if "exit" in word:
                break
            
            
            if ( "jarvis" in word.lower()):
                print("yes sir")
                speak("how can i help you sir")
                while True:
                    with sr.Microphone() as source:  # Use the default microphone as the audio source
                        print("Jarvis Active...")  # Prompt the user to say something
                        audio = r.listen(source)
                        c=r.recognize_google(audio)
                        
                        processCommand(c)
              
        except Exception as e:
            print("Error;{0}".format(e))



