import speech_recognition as sr
import time
import os
import pynput
from pynput.keyboard import Key, Controller
import webbrowser
import random
import pyttsx3
import SpotifySecrets
from SpotifySecrets import sp, uname
import json
from CustomSet import CustomSet


##Key Variables--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

keyboard = Controller()

mic = sr.Microphone()
r = sr.Recognizer()
engine = pyttsx3.init()
cs = CustomSet()

stopCommand = "Stop Alfred"
startCommand = "Alfred"

##Saying Lists-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##Wallpapers

KickitList = ("kick it", "play it", "a kit", "it is", "ticket")
BoogieList = ("it is time to boogie", "it's time to boogie", "time to boogie", "take me to boogie wonderland", "let's grove tonight", "it's boogie time", "it is time to buggy")
DogeList = ("doge")
NormalList = ("back to normal", "bring it back to normal")
GamingList = ("it is gaming time", "it's gaming time", "time to game", "it is game time", "is gaming time")
NightTimeList = ("it's night time", "it is night time")
AFKList = ("i am going afk", "i'm going afk")
CheemsList = ("cheems")
Chillhop = ("play lo-fi", "lo-fi")

for i in KickitList:
    cs.add(i, "k", "spotify:playlist:1psDNZgQfBiIgReq8CfPmv")

for i in BoogieList:
    cs.add(i, "b")

## Shortcut Locations---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
LeagueOfLegends = r"C:\Users\zekev\Desktop\SC\Games\Multiplayer\League of Legends.lnk"
BorderLands = r"com.epicgames.launcher://apps/Turkey?action=launch&silent=true"
GrandTheftAuto5 = r"com.epicgames.launcher://apps/9d2d0eb64d5c44529cece33fe2a46482?action=launch&silent=true"
HyperLightDrifter = r"com.epicgames.launcher://apps/Parakeet?action=launch&silent=true"
Bloons = r"E:\Steam Games\steamapps\common\BloonsTD6\BloonsTD6.exe"
MGS5 = r"E:\Steam Games\steamapps\common\MGS_TPP\mgsvtpp.exe"
Smite = r"E:\Steam Games\steamapps\common\SMITE\Binaries\Win64\Smite.exe"
MirrorsEdge = r"E:\Steam Games\steamapps\common\mirrors edge\Binaries\MirrorsEdge.exe"
LostInVivo = r"E:\Steam Games\steamapps\common\Lost in Vivo\LIV.exe"
Minecraft = r"E:\App Instalations\Minecraft\MinecraftLauncher.exe"
DolphinEmulator = r"E:\Downloads\Emulators\Nintendo\Dolphin-x64\Dolphin.exe"
EpicGamesLauncher = r"E:\App Instalations\Epic Games\Launcher\Engine\Binaries\Win64\EpicGamesLauncher.exe"
Barony = r"com.epicgames.launcher://apps/c98c4cd6d83a4524b4b22f13af95a104?action=launch&silent=true"
ReminantFromTheAshes = r"com.epicgames.launcher://apps/b4a0d2d15acb4db894a599b810297543?action=launch&silent=true"
StreamLabsOBS = r"E:\App Instalations\Streamlabs OBS\Streamlabs OBS.exe"
unity = r"E:\App Instalations\Unity\Unity Hub\Unity Hub.exe"

ShortCutDictionary = {
    "launch league of legends": LeagueOfLegends, 
    "launch borderlands": BorderLands,
    "launch gta v" : GrandTheftAuto5,
    "launch hyper light drifter" : HyperLightDrifter,
    "launch bloons td 6" : Bloons,
    "launch metal gear solid 5" : MGS5,
    "launch smite" : Smite,
    "launch mirrors edge" : MirrorsEdge,
    "launch lost in vivo" : LostInVivo,
    "launch minecraft" : Minecraft,
    "launch dolphin" : DolphinEmulator,
    "launch epic games launcher" : EpicGamesLauncher,
    "launch streamlabs obs" : StreamLabsOBS,
    "launch unity" : unity,
    "launch remnant ashes" : ReminantFromTheAshes
    }

ListOfGames = ["league", "bordlands", "gta 5", "hyper light drifter", "bloons td 6", "MGS5", "smite", "mirrors edge", "lost in vivo", "MC", "dolphin emulator", "20XX", "Crashlands",
"Gnog", "Quake", "Barony", "Reminant Ashes", "no games, do something productive", "do something productive", "should you really be playing games rn", "no games"]

##Actions---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def tts(said):
    engine.say(said)
    engine.runAndWait()



def lookUp(said):
    url = "https://www.google.com/search?client=firefox-b-1-d&q="
    webbrowser.register("firefox", None, 
    webbrowser.BackgroundBrowser(r"C:\Program Files\Mozilla Firefox\firefox.exe"))
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

def ShortCutsExecution(location):
    os.startfile(location)

def SpotifyCommands(said):
    ##Enviroment Variables
    l = sp.current_user_playing_track()
    artist = l["item"]["artists"][0]["name"]
    track = l["item"]["name"]
    uri = l["item"]["uri"]
    uria = [uri]
    likePlaylist = "spotify:playlist:223ZsEQOnOcUP8avR4xd2Z"

    ##Playlists
    if said == "gaming playlist":
        sp.start_playback(context_uri="spotify:playlist:0aEYvdj5ITz2TVYGpg9xx4")
    elif said == "like":
        #print("liked")
        sp.user_playlist_add_tracks(tracks=uria, playlist_id=likePlaylist, user=uname)
        tts("Liking song")

    ##Controls
    elif said == "before":
        sp.previous_track()
    elif said == "skip":
        sp.next_track()
        tts("Skipping Song")
    elif said[:6] == "volume":
        i = int(said[7:])
        sp.volume(volume_percent=i)
    elif said == "shuffle on":
        sp.shuffle(state=True)
        tts("Shuffle On")
    elif said == "shuffle off":
        sp.shuffle(state=False)
        tts("Shuffle Off")
    elif said == "phone":
        sp.transfer_playback(device_id="SM-G970U")

    ##Info
    elif said == "song" or said == "what song is playing":
        if artist != "":
            tts("Currently playing " + track + " by " + artist)
            print("Currently playing " + artist + " - " + track)
        else:
            tts("Currently playing " + track)
            print("Currently playing " + track)







## Audio Transcription---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def audioCap(microphone, recognizer):
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

##Redirection---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def WhatSaid(said):
    ##ShortCuts
    if said[0 : 6] == "launch":
        try:
            ShortCutsExecution(ShortCutDictionary[said])
            tts("launching" + said[7:])
        except:
            print(said[7:] + " can not be found.")
            tts(said[7:] + " can not be found.")
    
    ##Google
    
    elif said[0 : 7] == "look up":
        tts("Looking up " + said[8:])
        lookUp(said[8:])
    
    ##What Should I Play
    elif said == "what game should i play":
        random.shuffle(ListOfGames)
        tts("You should play" + ListOfGames[0])
        print("You should play " + ListOfGames[0])
    
    ##What Can Alfred Do
    elif said == "what can you do":
        print("I can:\n1).Change your wallpapers \n2).Google anything you want \n3).Launch any application you want \n4).Recommend games to play \n5).Control your spotify account.")
        tts("I can: 1)Change your wallpapers 2)Google anything you want 3)Launch any application you want 4)Recommend games to play 5).Control your spotify account")
    
    ## Wallpapers
    elif BoogieList.count(said) == 1:
        tts("Awww yeaaaaaa lets grove tonight")
        WallpaperKeyBind("b")
        sp.start_playback(context_uri="spotify:playlist:5jsuFtC4d3i3hnFs51RT5n")
    
    elif DogeList.count(said) == 1:
        tts("Doge")
        WallpaperKeyBind("d")
    
    elif NormalList.count(said) == 1:
        tts("Lets bring it back")
        WallpaperKeyBind("n")
    
    elif GamingList.count(said) == 1:
        tts("Its gaming time")
        WallpaperKeyBind("g")
        sp.start_playback(context_uri="spotify:playlist:0aEYvdj5ITz2TVYGpg9xx4")
    
    elif NightTimeList.count(said) == 1:
        tts("Night time")
        WallpaperKeyBind("w")
    
    elif CheemsList.count(said) == 1:
        tts("Cheems")
        WallpaperKeyBind("c")
    
    elif AFKList.count(said) == 1:
        tts("Will it hit the corner")
        WallpaperKeyBind("a")
        keyboard.press("-")
        keyboard.release("-")
    
    elif KickitList.count(said) == 1:
        WallpaperKeyBind("k")
        sp.start_playback(context_uri="spotify:playlist:1psDNZgQfBiIgReq8CfPmv")
    
    elif Chillhop.count(said) == 1:
        WallpaperKeyBind("l")
        sp.start_playback(context_uri="spotify:playlist:16BzUqICTjNk5r05n3W8Rk")

    ##Media Control
    elif said == "stop":
        keyboard.press(Key.media_play_pause)
    elif said == "play":
        keyboard.press(Key.media_play_pause)
    elif said == "skip" or said == "next":
        keyboard.press(Key.media_next)
    elif said == "volume up":
        keyboard.press(Key.media_volume_up)
    elif said == "volume down":
        keyboard.press(Key.media_volume_down)

    ##Spotify
    elif said[:7] == "spotify":
        SpotifyCommands(said[8:])

    else:
        print(said)
        return
        


##Audio Record---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def loopRecord(recog):
    try:
        if recog.lower() == startCommand.lower():
            print("Speak: ")
            #tts("yes")
            commandSetup = audioCap(mic, r)
            command = commandSetup["transcription"]
            #print(command)
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