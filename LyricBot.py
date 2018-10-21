import requests
import json
import string
import webbrowser
import pyautogui
import time

def get_lyrics(id):
    api = requests.get("https://thatsyourjam.com/lyrics?id="+str(id)).json()
    artist = api['artist_query']
    song = api['song_query']
    tr = str.maketrans("", "", string.punctuation)
    lyrics = api['lyrics'].lower()
    lyrics = set(lyrics.translate(tr).split())
    print("Starting "+api['song']+" by "+api['artist']+" ID: "+str(id))
    fill(artist,song,lyrics)
    print("Finished "+api['song']+" by "+api['artist']+" ID: "+str(id))

def fill(artist,song,lyrics):
    webbrowser.open("https://thatsyourjam.com/?artist="+artist+"&song="+song)
    time.sleep(5) #adjust based on how long the webpage takes to load
    for lyric in lyrics:    
        pyautogui.typewrite(lyric)
        pyautogui.press('space')
        #time.sleep(0.5)
    pyautogui.keyDown('command')
    pyautogui.press('w')
    pyautogui.keyUp('command')
    time.sleep(1)

def main():
    for i in range(1,34820):
        get_lyrics(i)

if __name__ == '__main__':
    main()