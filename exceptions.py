class InvalidUrlError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid URL check video existense or url"
    
class StaringAppError(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "Starting app error"