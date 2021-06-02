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
from CustomSet import CustomSet
from pydub import AudioSegment
from pydub.playback import play
import winsound
import asyncio


##Key Variables--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

keyboard = Controller()

mic = sr.Microphone()
r = sr.Recognizer()
engine = pyttsx3.init()

cs = CustomSet()

r.energy_threshold = 2000
r.pause_threshold = 1

stopCommand = "Stop Alfred"
startCommand = "Alfred"
startCommandlen = len(startCommand)

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


##Saying Lists-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##Wallpapers

KickitList = ("kick it", "play it", "a kit", "it is", "ticket", "cake it", "turn it up", "turn it all the way up")
BoogieList = ("it is time to boogie", "it's time to boogie", "time to boogie", "take me to boogie wonderland", "let's grove tonight", "it's boogie time", "it is time to buggy")
DogeList = ("doge")
NormalList = ("back to normal", "bring it back to normal")
GamingList = ("it is gaming time", "it's gaming time", "time to game", "it is game time", "is gaming time")
NightTimeList = ("it's night time", "it is night time")
AFKList = ("i am going afk", "i'm going afk")
CheemsList = ("cheems")
Chillhop = ("play lo-fi", "lo-fi")
christmas = ("christmas", "it is christmas time", "it's christmas", "santa", "its snowing")

#sp.start_playback(context_uri="spotify:playlist:5jsuFtC4d3i3hnFs51RT5n")

for i in KickitList:
    cs.add(i, """WallpaperKeyBind("k")""", "spotify:playlist:1psDNZgQfBiIgReq8CfPmv", "Kicking it")

for i in BoogieList:
    cs.add(i, """WallpaperKeyBind("b")""", "spotify:playlist:5jsuFtC4d3i3hnFs51RT5n", "Awww yeaaaaaa lets grove tonight")

for i in DogeList:
    cs.add(i, """WallpaperKeyBind("d")""", None, "Doge")

for i in NormalList:
    cs.add(i, """WallpaperKeyBind("n")""", None, "Let's bring it back to normal")

for i in GamingList:
    cs.add(i, """WallpaperKeyBind("g")""", "spotify:playlist:0aEYvdj5ITz2TVYGpg9xx4", "It's gaming time")

for i in NightTimeList:
    cs.add(i, """WallpaperKeyBind("w")""", None, "Night time")

for i in CheemsList:
    cs.add(i, """WallpaperKeyBind("c")""", None, "Chems")

for i in AFKList:
    cs.add(i, """WallpaperKeyBind("a")""", None, "Will it hit the corner", "-")

for i in Chillhop:
    cs.add(i, """WallpaperKeyBind("l")""", "spotify:playlist:16BzUqICTjNk5r05n3W8Rk", "playing lofi")

for i in christmas:
    cs.add(i, """WallpaperKeyBind("s")""", "spotify:playlist:05aFClJd2oxuUDsHpuWgpp", "oh baby its cold outside")

## Media Controls---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ListOfMediaControls = [
    [["pause", "play", "stop"], Key.media_play_pause], 
    [["skip", "next"], Key.media_next], 
    [["volume up"], Key.media_volume_up], 
    [["volume down"], Key.media_volume_down]
    ]

for i in ListOfMediaControls:
    for k in i[0]:
        cs.add(k, None, None, None, i[1])

ListOfSpotifyCommands = [
    [["shuffle on", "shuffle", "spotify shuffle", "spotify shuffle on"], "sp.shuffle(state=True)", "shuffle on"], 
    [["shuffle off", "spotify shuffle off"], "sp.shuffle(state=False)", "shuffle off"],
    [["switch to phone", "spotify phone"], """sp.transfer_playback(device_id="SM-G970U")""", "switching spotify to phone"], 
    [["replay", "before", "spotify before", "replay song"], "sp.previous_track()", None], 
    [["spotify skip", "spotify next", "spotify next song", "spotify skip this song"], "sp.next_track()", None], 
    [["like this song", "like the song", "like", "like song"], "sp.user_playlist_add_tracks(tracks=uria, playlist_id=likePlaylist, user=uname)", "Liking Song"]
    ]

for i in ListOfSpotifyCommands:
    for k in i[0]:
        cs.add(k, i[1], None, i[2])

ListOfPlaylists = [[["gaming playlist"], "spotify:playlist:0aEYvdj5ITz2TVYGpg9xx4"]]

for i in ListOfPlaylists:
    for k in i[0]:
        cs.add(k, None, i[1])


## Shortcut Locations---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
LeagueOfLegends = """ "{}" """.format(r"E:\App Instalations\Riot Games\League of Legends\LeagueClient.exe")
GrandTheftAuto5 = """ "com.epicgames.launcher://apps/9d2d0eb64d5c44529cece33fe2a46482?action=launch&silent=true" """
HyperLightDrifter = """ "com.epicgames.launcher://apps/Parakeet?action=launch&silent=true" """
Bloons = """ "E:\Steam Games\steamapps\common\BloonsTD6\BloonsTD6.exe" """
MGS5 = """ "E:\Steam Games\steamapps\common\MGS_TPP\mgsvtpp.exe" """
Smite = """ "E:\Steam Games\steamapps\common\SMITE\Binaries\Win64\Smite.exe" """
LostInVivo = """ "E:\Steam Games\steamapps\common\Lost in Vivo\LIV.exe" """
Minecraft = """ "E:\App Instalations\Minecraft\MinecraftLauncher.exe" """
DolphinEmulator = """ "{}" """.format(r"E:\\Downloads\\Emulators\\Nintendo\\Dolphin-x64\\Dolphin.exe")
EpicGamesLauncher = """ "E:\App Instalations\Epic Games\Launcher\Engine\Binaries\Win64\EpicGamesLauncher.exe" """
Barony = """ "com.epicgames.launcher://apps/c98c4cd6d83a4524b4b22f13af95a104?action=launch&silent=true" """
ReminantFromTheAshes = """ "com.epicgames.launcher://apps/b4a0d2d15acb4db894a599b810297543?action=launch&silent=true" """
StreamLabsOBS = """ "E:\App Instalations\Streamlabs OBS\Streamlabs OBS.exe" """
Qube = """ "com.epicgames.launcher://apps/Auk?action=launch&silent=true" """
Celeste = """ "com.epicgames.launcher://apps/Salt?action=launch&silent=true" """

ListOfGames = [
[["launch league of legends", "launch league"], LeagueOfLegends], 
[["launch gta v", "launch gta"], GrandTheftAuto5], 
[["launch hyper light drifter", "launch light drifter"], HyperLightDrifter], 
[["launch bloons", "launch bloons td", "launch bloons td 5"], Bloons],
[["launch metal gear solid 5", "launch MGS", "launch metal gear", "launch metal gear solid"], MGS5], 
[["launch smite"], Smite],  
[["launch lost in vivo"], LostInVivo], 
[["launch minecraft"], Minecraft], 
[["launch dolphin", "launch dolphin emulator"], DolphinEmulator],
[["launch epic games launcher"], EpicGamesLauncher], 
[["launch streamlabs obs"], StreamLabsOBS], 
[["launch remnant ashes", "launch remnant", "launch remnant from the ashes"], ReminantFromTheAshes],
[["launch cube", "launch cube 2"], Qube],
[["launch celeste"], Celeste]
]

for i in ListOfGames:
    for k in i[0]:
        cs.add(key=k, command="os.startfile({})".format(i[1]), tts="launching " + k[7:])
    






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


# Voice activated
# def loopRecord():
#     recog = "None"
#     while recog.lower() != stopCommand.lower():
#         if recog.lower() == startCommand.lower() or kb.is_pressed("`+shift"):
#             winsound.Beep(500, 200)
#             winsound.Beep(1000, 200)
#             commandSetup = audioCap(mic, r, True)
#             recog = commandSetup["transcription"]
#             if not(recog):
#                 recog = "None"
#             WhatSaid(recog.lower())
#         else:
#             setup = audioCap(mic, r)
#             recog = setup["transcription"]
#             if not(recog):
#                 recog = "None"
#             print(recog)

#Keybind Only
def loopRecord():
    recog = "None"
    while recog.lower() != stopCommand.lower():
        if kb.is_pressed("`+shift"):
            winsound.Beep(500, 200)
            winsound.Beep(1000, 200)
            commandSetup = audioCap(mic, r, True)
            recog = commandSetup["transcription"]
            if not(recog):
                recog = "None"
            WhatSaid(recog.lower())
        time.sleep(1)

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