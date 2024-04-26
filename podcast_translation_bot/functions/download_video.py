from pytube import YouTube

class Video:
    def __init__(self, url: str):
        self.yt = YouTube(url)
        self.video = self.yt.streams.filter(only_audio=True).first() 

    def get_video_title(self) -> str:
        return self.video.title
    
    def download_video(self) -> None:
        self.video.download(filename=f'/Users/vladislavananev/Desktop/project/podcast-translation-bot/static/{self.get_video_title()}.mp3')
        
    
    