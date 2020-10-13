def friday(audio_string):
    tts = gTTS(text=audio_string, lang='en') 
    r = random.randint(1, 10000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

    
def mood_chat(user_response):
    if "test this response" in user_response:
        return friday("test 1, 2, 3. Don't worry. It works")
        