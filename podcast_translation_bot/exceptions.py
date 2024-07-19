class InvalidUrlError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid URL check video existense or url"


class StartingAppError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Starting app error"


class GetAudioInVideoException(Exception):
    def __init__(self):
        ...

    def __str__(self):
        return "Get audio error!"


class PropertyValueException(Exception):
    def __init__(self, error):
        self.error_message = error

    def __str__(self):
        return self.error_message
