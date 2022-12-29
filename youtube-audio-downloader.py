from pytube import YouTube
import os

url = input("Enter youtube video link: ")
video = YouTube(url)

print("Downloading... " + video.title)
out_path = video.streams.filter(only_audio=True).first().download()
new_name = os.path.splitext(out_path)
os.rename(out_path, new_name[0]+".mp3")
print("Done!")