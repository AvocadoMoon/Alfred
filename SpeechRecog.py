import speech_recognition as sr
import time
import os
import pynput
from pynput.keyboard import Key, Controller
import keyboard as kb
import webbrowser
import random
import pyttsx3
import SpotifySecrets
from SpotifySecrets import sp, uname
import json
from pydub import AudioSegment
from pydub.playback import play
import winsound
from Commands import cs


##Key Variables--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

keyboard = Controller()

mic = sr.Microphone()
r = sr.Recognizer()
engine = pyttsx3.init()


r.energy_threshold = 2000
r.pause_threshold = 1

stopCommand = "Stop Alfred"
startCommand = "Alfred"

webBroswerLocation = r""

##Actions---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def tts(said):
    engine.say(said)
    engine.runAndWait()


def lookUp(said):
    url = "https://www.google.com/search?client=firefox-b-1-d&q="
    webbrowser.register("firefox", None, 
    webbrowser.BackgroundBrowser(webBroswerLocation))
    webbrowser.get("firefox").open(url + said)

def WallpaperKeyBind(keyword):
    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.alt_l)
    keyboard.press(Key.shift_l)
    keyboard.press(keyword)
    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.alt_l)
    keyboard.release(Key.shift_l)
    keyboard.release(keyword)
## Audio Transcription---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def audioCap(microphone, recognizer, ts=False):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        if ts:
            print("Speak: ")
            tts("Speak")
        audio = recognizer.listen(source)
    response = {"success": True, "error": None, "transcription": None}
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"
    return response

##Redirection---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def WhatSaid(said):
    ##Enviroment Variables
    l = sp.current_user_playing_track()
    if l:
        artist = l["item"]["artists"][0]["name"]
        track = l["item"]["name"]
        uri = l["item"]["uri"]
        uria = [uri]
    likePlaylist = "spotify:playlist:223ZsEQOnOcUP8avR4xd2Z"

    ##Google
    if "look up" in said:
        index = said.find("look up")
        tts("Looking up " + said[(index + 8):])
        lookUp(said[(index + 8):])
    
    ##What Can Alfred Do
    elif said == "what can you do":
        print("I can:\n1).Change your wallpapers \n2).Google anything you want \n3).Launch any application you want \n4).Recommend games to play \n5).Control your spotify account.")
        tts("I can: 1)Change your wallpapers 2)Google anything you want 3)Launch any application you want 4)Recommend games to play 5).Control your spotify account")
    
    ## Wallpapers/ Launch Application/ Media Controls
    elif cs.get(said):
        j = cs.get(said)
        if j.tts:
            tts(j.tts)
        if j.command:
            eval(j.command)
        if j.playlist:
            sp.start_playback(context_uri=j.playlist)
        if j.keybind:
            keyboard.press(j.keybind)
            keyboard.release(j.keybind)

    ##Spotify
    elif "volume" in said:
        try:
            index = said.find("volume")
            i = int(said[(index + 7):])
        except:
            return
    ##Info
    elif "what song is playing" in said or "song" in said:
        try:
            if artist != "":
                tts("Currently playing " + track + " by " + artist)
                print("Currently playing " + artist + " - " + track)
            else:
                tts("Currently playing " + track)
                print("Currently playing " + track)
        except:
            return
    ## Type
    elif said[:4] == "type":
        tts("typing" + said[5:])
        for i in said[5:]:
            keyboard.press(i)
            keyboard.release(i)

    else:
        print(said)
        return
        


##Audio Record---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#upgrade record setup with async, couroutine
#check for alfred is couroutine, getting full line of text is not


#Voice activated
def loopRecord():
    recog = "None"
    while recog.lower() != stopCommand.lower():
        if recog.lower() == startCommand.lower() or kb.is_pressed("`+shift"):
            winsound.Beep(500, 200)
            winsound.Beep(1000, 200)
            commandSetup = audioCap(mic, r, True)
            recog = commandSetup["transcription"]
            if not(recog):
                recog = "None"
            WhatSaid(recog.lower())
        else:
            setup = audioCap(mic, r)
            recog = setup["transcription"]
            if not(recog):
                recog = "None"
            print(recog)

# #Keybind Only
# def loopRecord():
#     recog = "None"
#     while recog.lower() != stopCommand.lower():
#         if kb.is_pressed("`+shift"):
#             winsound.Beep(500, 200)
#             winsound.Beep(1000, 200)
#             commandSetup = audioCap(mic, r, True)
#             recog = commandSetup["transcription"]
#             if not(recog):
#                 recog = "None"
#             WhatSaid(recog.lower())
#         time.sleep(1)

if __name__ == "__main__":
    assert(cs.get("launch league"))
    assert(cs.get("kick it"))
    assert(cs.get("play"))
    assert(cs.get("shuffle on"))
    assert(cs.get("gaming playlist"))


loopRecord()
tts("Booting Down")
play(AudioSegment.from_wav(r"E:\Downloads\Programing\Other Applications\Speech\Microsoft Windows XP Shutdown Sound.wav"))
print("finished")