import speech_recognition as sr
import time
import os
import pynput
from pynput.keyboard import Key, Controller
import webbrowser
import random



#Key Variables-----------------------------------------------------------------------------------------------------

keyboard = Controller()

mic = sr.Microphone() #variable used to access your mic
r = sr.Recognizer() #variable used to access the speech recognition software


stopCommand = "Stop Alfred"
startCommand = "Alfred"


#Shortcut Locations--------------------------------------------------------------------------------------------
LeagueOfLegends = r"C:\Example\Of\A\File\Location\Of\An\.exe\file"

#Keybind Sayings-----------------------------------------------------------------------------------------------
ListOfSayingsForKeyBind = ["the list of sayings which can be associated with keybinds", "use commas to distingush different strings"]

ShortCutDictionary = {
    "What you say to access and use the variable after the colon": LeagueOfLegends 
    }

ListOfThings = ["the list of things you want to be pulled randomly"]

#Actions-------------------------------------------------------------------------------------------------------

def lookUp(said):
    url = "https://www.google.com/search?client=firefox-b-1-d&q="
    webbrowser.register("firefox", None, 
    webbrowser.BackgroundBrowser(r"C:\Program Files\Mozilla Firefox\firefox.exe")) #This is where you put the file location of firefox browser, idk how to it with other browser srry
    webbrowser.get("firefox").open(url + said)

def KeyBind(keyword): #Ouputs the keybind of Left Control, Left Alt, Left Shift, and custom key that can be changed by different input of KeyBind.
    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.alt_l)
    keyboard.press(Key.shift_l)
    keyboard.press(keyword)
    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.alt_l)
    keyboard.release(Key.shift_l)
    keyboard.release(keyword)

def ShortCutsExecution(location): #Tool used to launch the .exe variables stated early in the code.
    os.startfile(location)


#Audio Transcription--------------------------------------------------------------------------------------------

def audioCap(microphone, recognizer): #Definition which allows what is said through your mic to transcribed into a string on python
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
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

#Redirection------------------------------------------------------------------------------------------------------

def WhatSaid(said):
    #ShortCuts
    if said[0 : 6] == "launch": #After keyword launch is said, the key for the .exe file in the dictionary must be said in order to execute that specific .exe file
        ShortCutsExecution(ShortCutDictionary[said])
    
    ##Google
    
    elif said[0 : 7] == "look up": #After loop up is said everything after will be searched
        print("Looking up " + said[8:])
        lookUp(said[8:])
    
    #Pick something random
    elif said == "pick one thing in this list": #Uses previous list stated and picks one item in the list
        random.shuffle(ListOfThings)
        print("I picked " + ListOfThings[0])

    #What Can alfred do
    elif said == "what can you do":
        print("I can:\n1).Change your wallpapers \n2).Google anything you want \n3).Launch any application you want \n4).Recommend games to play")


    ## Wallpapers
    elif ListOfSayingsForKeyBind.count(said) == 1:
        KeyBind("b") #Key pressed with keybind definition
    else:
        print(said[0:14])
        return
        


#Audio Record----------------------------------------------------------------------------------------------------

def loopRecord(recog): #Definition where the startcommand must be said in order to access all the other definitions within this code
    try:
        if recog.lower() == startCommand.lower():
            print("speak")
            commandSetup = audioCap(mic, r)
            command = commandSetup["transcription"]
            print(command.lower())
            WhatSaid(command.lower())
            loopRecord(1)
        elif recog.lower() == stopCommand.lower():
            return
        else:
            loopRecord(1)
    except:
        print("Command")
        setup = audioCap(mic, r)
        recog = setup["transcription"]
        print(recog)
        loopRecord(recog)

loopRecord(1)
print("finished")