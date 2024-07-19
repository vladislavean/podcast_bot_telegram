import speech_recognition as rc


class TranslateVideo:

    def translate_text(self, mp3_file):
        pass


class ConvertToText:

    @staticmethod
    def convert_mp3_to_text(
            file
    ) -> str:
        recognizer = rc.Recognizer()
        with rc.AudioFile(file) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google_cloud(audio_data=audio, language='ru-RU,en-US')
        return text

    def get_text(self, file):
        pass
