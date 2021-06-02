client_id= "b01aad9baf284ea184b28665045d5f57"
client_secret = "261f5685e8714092bc482ad3107b83bc"

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os
import spotipy.util as util
from json.decoder import JSONDecodeError
rurl = "https://www.google.us/"
scope = """playlist-read-private, ugc-image-upload, user-read-playback-state, streaming, playlist-read-collaborative, user-modify-playback-state, user-read-private, user-read-playback-position, user-read-currently-playing, user-read-recently-played, playlist-modify-public, playlist-modify-private """
capath = r"E:\Downloads\Programing\Other Applications\YoutubeToSpotify\.cache-Zeke"
uname = "3j2rte6v16bsg091aueomvnbl"



sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=client_id, client_secret=client_secret ,redirect_uri=rurl,scope=scope, show_dialog=True, username= uname)

sp = spotipy.Spotify(auth_manager=sp_oauth)

#l = sp.current_user_playing_track()

#print(json.dumps(l, sort_keys=True, indent=4))
#print()
#artist = l["item"]["artists"][0]["name"]
#track = l["item"]["name"]
#uri = l["item"]["uri"]
#uria = [uri]
#print(uri)
#likePlaylist = "spotify:playlist:223ZsEQOnOcUP8avR4xd2Z"
#sp.user_playlist_add_tracks(user=uname, tracks=uria, playlist_id=likePlaylist)