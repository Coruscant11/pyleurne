from random import randint

class roomManager:

    def __init__(self):
        print("Initialisation du RoomManager...")
        self.__roomsList = set()

    def __addNewRoom__(self, creatorName):
        generatedRoomID = randint(1, 1000)

        while generatedRoomID in self.__roomsList:
            generatedRoomID = randint(1, 1000)

        self.__roomsList.add(Room(generatedRoomID, creatorName))


class Room:

    def __init__(self, roomID, creatorName):
        self.__roomID = roomID
        self.__userCreatorname = creatorName
        self.__userList = set()
        self.__videoPlaylist = []

    def addNewUser(self, userName):
        if userName in self.__userList:
            return False
        else:
            self.__userList.add(userName)
            return True
        return False

    def addNewVideo(self, videoUrl):
        self.__videoPlaylist.append(videoUrl)