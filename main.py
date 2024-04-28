from pytube import Playlist
from pytube import YouTube
import datetime
import sys
import time
import os




def progress_func(stream, chunk, bytes_remaining):
    live = stream.filesize - bytes_remaining
    finished = int(50 * live / stream.filesize)

    sys.stdout.write(
        "\r[{}{}] {} MB / {} MB".format('=' * finished, ' ' * (50 - finished), "{:.2f}".format(bytes_megabytes(live)),
                                        "{:.2f}".format(bytes_megabytes(stream.filesize))))
    sys.stdout.flush()


def bytes_megabytes(bytes_size):
    megabytes_size = bytes_size / (1024 ** 2)
    return megabytes_size


def download_and_convert(url):
    print(f"Video Title : {YouTube(url).title}")
    print(f"Video Length : {str(datetime.timedelta(seconds=YouTube(url).length))}")
    print(f"Video Date : {YouTube(url).publish_date}")
    print(f"Video Views : {YouTube(url).views}")
    time.sleep(1)
    video = YouTube(url,on_progress_callback=progress_func)
    stream = video.streams.filter(only_audio=True).first()
    try:
        os.mkdir("./audio")
    except:
        pass
    stream.download(filename=f"{video.title}.mp3",output_path='./audio')




if __name__ == '__main__':
    print("*"*40)
    print("Welcome To Mp3PlayList")
    print("*"*40)

    
    while True:
        playlist_url = input("\n Youtube Playlist Url : ")
        try:
            playlist = Playlist(playlist_url)
            print("\n")
            print(f"Playlist Name : {playlist.title}")
            print(f"Playlist Owner : {playlist.owner}")
            print(f"Playlist Lenght : {playlist.length} Video")
            print(f"Playlist Last Update : {playlist.last_updated}")
        except:
            print("Error, Wrong Url")
            continue

        time.sleep(1)
        print("\n Start Download... \n")
        time.sleep(1)

        videos_done = 0
        playlist_urls = playlist.video_urls


        for url in playlist_urls:
            print("\n")
            videos_done += 1
            print(f"Video {videos_done}/{playlist.length}")
            download_and_convert(url)
        print(f"\n The \"{playlist.title}\" playlist has been successfully downloaded")
            

        
