# from os import system #this is a core python package
import os
import random #you want to randomly generate a file name for the audio file


#make sure to have python 3 interpreter ctrl+shift+P 
#pip3 install speechrecognition
#this is google's library performing speech recog API
import speech_recognition as sr

#python time() and datetime() methods for current
import time
import datetime


# pip3 instal pyaudio
# installs required pyaudio which is 
# needed to use the microphone
import pyaudio

# import webbrowser package 
import webbrowser


# pip3 install gTTS : use google text to speech interface; whatever we pass in as text, it will create an audio file to speak
from gtts import gTTS

# pip3 install playsound : make sure to also use another package called 'playsound.' If we don't use this, itll open up your defauly sound/audio player to respond... and we don't want that.
import playsound

# pip3 install pyobjc : this has app kit that playsound depends on. PyObjC is a bridge between Python and Objective-C. 

# initialize recognizer
# responsible for recognizing speech 
r = sr.Recognizer()


#create function to record audio
def record_audio(ask=False): #setting optional ask argument to False
    with sr.Microphone() as source:
        #create if statement for ask argument
        if ask:
            print(ask)
        # create audio variable and set to recognizer object and then use listen() method. Pass in source which is our microphone
        audio = r.listen(source, phrase_time_limit=4) 

        # create variable for voice_data and initialize 
        voice_data = ''
        # create try block with 2 exceptions
        try:
            #create variable for voice data; whatever we say, we want to put that into a variable. Use recognize_google and pass in our audio variable
            voice_data = r.recognize_google(audio)
        # create unknownValueError exception for when it doesn't understand what user is saying
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        # create request error exception if something is wrong/if server isn't working
        except sr.RequestError:
            print("Sorry, my speech service is in maintenance. Be right back.")
        # return voice_data 
        return voice_data

def friday(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

# now let's start coding the response
# create function respond with voice_data inside
def respond(voice_data):
    # if "what is your name" is heard in voice_data google_audio recording:
    if "what is your name" in voice_data:
        friday("My name is Alexis")
    elif "what time is it" in voice_data:
        friday("Time: ", time.ctime())
    elif "what day is it" in voice_data:
        friday(datetime.datetime.now())
    elif 'search' in voice_data:
        friday("What do you want to search for?")
        search = record_audio("Please say what you want to search for: ")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        friday("Here is what I found for " + search)
    elif 'find location' in voice_data:
        location = record_audio("What is the location?: ")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        friday("Here is the location of " + location)
    elif 'find place' in voice_data:
        location = record_audio("What is the location?: ")
        url = "https://google.nl/maps/search/" + location + "/&amp;"
        webbrowser.get().open(url)
        friday("Here is the location of " + location)
    # elif "exit" or "thank you that is all" in voice_data:
       # exit()
        


time.sleep(1) #waits however many seconds we want
friday('How can I help you...')
#now, we are creating a while loop to continuously have computer listen to what I am saying
while 1:
    voice_data = record_audio() 
    respond(voice_data)
# from here, you can perform print(voice_data) to double check that your audio is being heard


# test one two three