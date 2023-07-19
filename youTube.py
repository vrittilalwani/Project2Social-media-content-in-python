'''from pytube import YouTube

# Input url output audio Function
def audio_from_youtube(url):

    # object
    yt = YouTube(url)

    aud = yt.streams.filter(only_audio=True).first()

    # download that audio
    aud.download()

video_url=input("Enter youtube url ")
audio_from_youtube(video_url)
'''
from pytube import YouTube
def downloadSong(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")
link = input("Enter the YouTube video URL: ")
downloadSong(link)
