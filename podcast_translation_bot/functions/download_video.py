from pytube import YouTube
import os
from dotenv import load_dotenv
load_dotenv()

GET_VIDEO = range(1)
class Video:
    def __init__(self, url: str):
        self.yt = YouTube(url)
        self.video = self.yt.streams.filter(only_audio=True).first() 
        self.PATH = os.getenv("PATH")

    def get_video_title(self) -> str:
        return self.video.title
    
    def download_video(self) -> None:
        self.video.download(filename=f'{os.getcwd()}/static/{self.get_video_title()}.mp3')
        
    
    