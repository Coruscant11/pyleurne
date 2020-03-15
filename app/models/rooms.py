from random import randint


class RoomManager:

    def __init__(self):
        print("Initialisation du Room_Manager...")
        self.__roomsList = {}
        self.__next_population_acc = 0

    def __str__(self):
        return self.__roomsList.__str__()

    def add_new_room__(self, user):
        generated_room_id = RoomManager.generate_random_room_id(self.__roomsList)
        self.__roomsList[generated_room_id] = Room(generated_room_id, user)

        return generated_room_id

    def check_room(self, room_id):
        return room_id in self.__roomsList

    def room_population(self, room_id):
        return len(self.__roomsList[room_id].get_userlist())

    def room_next_population_id(self, room_id):
        return len(self.__roomsList[room_id].get_userlist())

    @staticmethod
    def generate_random_room_id(roomList):
        generatedRoomID = randint(1, 1000)

        while generatedRoomID in roomList:
            generatedRoomID = randint(1, 1000)

        return generatedRoomID

    def get_room_list(self):
        return self.__roomsList


class Room:

    def __init__(self, roomID, creatorUser):
        self.__room_ID = roomID
        self.__creatorUser = creatorUser
        self.__userlist = set()
        self.__video_playlist = []
        self.add_new_user(self.__creatorUser)
        self.__creator_connection_state = False

    def add_new_user(self, user):
        if user in self.__userlist:
            return False
        else:
            self.__userlist.add(user)
            return True
        return False

    def add_new_video(self, videoUrl):
        self.__video_playlist.append(videoUrl)

    def get_creator_connected_state(self):
        return self.__creator_connection_state

    def set_creator_connected_state(self, state):
        self.__creator_connection_state = state

    def get_creator(self):
        return self.__creatorUser

    def get_room_id(self):
        return self.__room_ID

    def get_userlist(self):
        return self.__userlist

    def get_json_username_list(self):
        str_json = "{\n\t\"population\":%d," % len(self.__userlist)

        for i in self.__userlist:
            str_json += "\n\t\"%s\": {\n\t\t" % i.get_pseudo() + "\"username\":\"%s\",\n\t\t" % str(i.get_pseudo()) + "\"address\":\"%s\",\n\t\t" % str(i.get_ip_address()) + "\"role\":\"%s\"\n\t" % str(i.get_role().name) + "\n\t},"

        str_json = str_json[:-1]
        str_json += "\n}"

        return str_json