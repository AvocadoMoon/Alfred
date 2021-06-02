from CustomSet import CustomSet
from pynput.keyboard import Key, Controller

cs = CustomSet()

##Wallpapers

##Sayings for specific wallpapers
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

##Putting Wallpapers In Custom Hash Table
for i in KickitList:
    cs.add(key_word=i, command="""WallpaperKeyBind("k")""", playlist="spotify:playlist:1psDNZgQfBiIgReq8CfPmv", tts="Kicking it")

for i in BoogieList:
    cs.add(key_word=i, command="""WallpaperKeyBind("b")""", playlist="spotify:playlist:5jsuFtC4d3i3hnFs51RT5n", tts="Awww yeaaaaaa lets grove tonight")

for i in DogeList:
    cs.add(key_word=i, command="""WallpaperKeyBind("d")""", tts= "Doge")

for i in NormalList:
    cs.add(key_word=i, command="""WallpaperKeyBind("n")""", tts="Let's bring it back to normal")

for i in GamingList:
    cs.add(key_word=i, command="""WallpaperKeyBind("g")""", playlist="spotify:playlist:0aEYvdj5ITz2TVYGpg9xx4", tts="It's gaming time")

for i in NightTimeList:
    cs.add(key_word=i, command="""WallpaperKeyBind("w")""", tts= "Night time")

for i in CheemsList:
    cs.add(key_word=i, command="""WallpaperKeyBind("c")""", tts="Chems")

for i in AFKList:
    cs.add(key_word=i, command="""WallpaperKeyBind("a")""", tts= "Will it hit the corner", keybind="-")

for i in Chillhop:
    cs.add(key_word=i, command="""WallpaperKeyBind("l")""", playlist="spotify:playlist:16BzUqICTjNk5r05n3W8Rk", tts="playing lofi")

for i in christmas:
    cs.add(key_word=i, command="""WallpaperKeyBind("s")""", playlist="spotify:playlist:05aFClJd2oxuUDsHpuWgpp", tts="oh baby its cold outside")


## Media Controls---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ListOfMediaControls = [
    [["pause", "play", "stop"], Key.media_play_pause], 
    [["skip", "next"], Key.media_next], 
    [["volume up"], Key.media_volume_up], 
    [["volume down"], Key.media_volume_down]
    ]

for i in ListOfMediaControls:
    for k in i[0]:
        cs.add(key_word=k, keybind= i[1])

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
        cs.add(key_word=k, command=i[1], tts=i[2])

ListOfPlaylists = [
    [["gaming playlist"], "spotify:playlist:0aEYvdj5ITz2TVYGpg9xx4"]
    ]

for i in ListOfPlaylists:
    for k in i[0]:
        cs.add(key_word=k, playlist=i[1])

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