from pytube import YouTube
import os
from dotenv import load_dotenv
from podcast_translation_bot.exceptions import GetAudioInVideoException, PropertyValueException

load_dotenv()


class Video:

    def __init__(self, url: str):
        try:
            self.yt = YouTube(url)
            self.video = self.yt.streams.filter(only_audio=True).first()
        except ValueError:
            raise GetAudioInVideoException
        except IndexError:
            raise GetAudioInVideoException

    @property
    def get_video(self):
        if self.video is None:
            raise PropertyValueException(
                error='Video is none'
            )
        return self.video

    @property
    def get_video_title(self) -> str:
        if self.video.title is None:
            raise PropertyValueException(
                error='Video title is none. May be video is none'
            )
        return self.video.title


class VideoDownloader:

    @staticmethod
    def download_video(video: Video) -> None:
        video.get_video.download(filename=f'{os.getcwd()}/../static/{video.get_video_title}.mp3')
