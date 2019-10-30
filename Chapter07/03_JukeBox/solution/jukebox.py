class JukeBox:
    #TODO:: Check self.variables accessible here like in Java ?

    def __init__(self, cdPlayer, user, cdCollection, ts):
        self.ts = ts
        self.user = user
        pass

    def getCurrentSong(self):
        return ts.getCurrentSong()

    def setUser(self, u):
        self.user = u

class CDPlayer:
    # TODO: Check Constructors in the Library
    def __init__(self, p, c):
        self.p = p
        self.c = c
    def playSong(self, s):
        pass
    def getPlaylist(self):
        return p
    def setPlaylist(self, p):
        self.p = p
    def getCD(self):
        return self.c
    def setCD(self, c):
        self.c = c

class PlayList:
    def __init__(self, song, queue):
        self.song = song
        self.queue = queue
    def getNextSToPlay(self):
        return a[-1]
    def queueUpSong(self, s):
        self.queue.append(s)

class CD:
    def __init__(self, id, artist, songs):
        self.id = id
        self.artist = artist
        self.songs = songs

class Song:
    def __init__(self, id, CD, title, length):
        self.id = id
        self.CD = CD
        self.title = title
        self.length = length

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getID(self):
        return self.id
    def setID(self, id):
        self.id = id
    def addUser(self, name, iD):
        pass

