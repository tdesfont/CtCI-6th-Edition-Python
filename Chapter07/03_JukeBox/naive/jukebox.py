class Song:

    def __init__(self, title, duration, author):
        self.title = title
        self.duration = duration
        self.author = author
        self.filePath = None

    def setFilePath(self, filePath):
        """
        Get the path of the mp3 file.
        :return:
        """
        self.filePath = filePath

    def getFilePath(self):
        return self.filePath

class JukeBox:

    def __init__(self):
        self.titles = []
        #
        self.currentSong = None
        self.isPlaying = False

    def addTitles(self, titles):
        # TODO: Handle the titles when given as an array or as a file
        if type(titles) is str:
            self.titles.append(titles)
        else:
            for title in titles:
                self.titles.append(title)
        pass