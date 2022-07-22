from pytube import YouTube
from model._uses_.mathplus import *
import os

def download(url):
    try:
        os.system('cls' if os.name=='nt' else 'clear')
        video = YouTube(url)

        dl = ""
        while dl not in ["h", "l", "i"]:
            dl = input("Download higher resolution (h), lower resolution (l) or get by itag (i) : ")

            if dl not in ["h", "l", "i"]:
                print("Please chose a valid option between : h, l, i")

        itag = 0
        if dl == "i": 
            itag = input("What's the itag (you can use h for help) : ")
            if itag == "help" or itag == "h":
                for stream in video.streams:
                    print(" ", stream)
                itag = input("\nWhat's the itag (you can use h for help) : ")
            itag = try_int(itag)

        def on_download_progress(stream, chunk, bytes_remaining):

            os.system('cls' if os.name=='nt' else 'clear')

            print("TITRE :", video.title)
            print("VEWS :", video.views)
            print("AUTHOR :", video.author)
            print("THUMBNAIL :", video.thumbnail_url)
            pourcentage = round(100-((bytes_remaining/stream.filesize)*100))

            points = "".join(["." for _ in range(100-pourcentage)])
            hashtag = "".join(["#" for _ in range(pourcentage)])

            print(f"Downloaded : [{hashtag}{points}] {pourcentage}%")

        video.register_on_progress_callback(on_download_progress)

        if dl == "h":
            stream = video.streams.get_highest_resolution()
            print("Downloading...")
            stream.download()
        elif dl == "l":
            stream = video.streams.get_lowest_resolution()
            print("Downloading...")
            stream.download()
        elif dl == "i" and itag != 0:
            stream = video.streams.get_by_itag(str(itag))
            print("Downloading...")
            stream.download()
        
        print("Download as well !")

    except:
        print("incorrect URL")