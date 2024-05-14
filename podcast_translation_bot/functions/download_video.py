from pytube import YouTube
import os
from dotenv import load_dotenv
load_dotenv()


class Video: 
    
    def __init__(self, url: str):
        try:
            self.yt = YouTube(url)
            self.video = self.yt.streams.filter(only_audio=True).first()
        except:
            pass
    @property
    def get_video(self):
        return self.video

    @property
    def get_video_title(self) -> str:
        return self.video.title
    

class VideoDownloader:
    
    @staticmethod
    def download_video(video: Video) -> None:    
        video.get_video.download(filename=f'{os.getcwd()}/../static/{video.get_video_title}.mp3')
        
    
    