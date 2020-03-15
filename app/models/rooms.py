from app.controllers.playlist_manager import PlaylistManager


class Room:

    def __init__(self, roomID, creatorUser):
        self.__room_ID = roomID
        self.__creatorUser = creatorUser
        self.__userlist = {}
        self.__video_playlist = PlaylistManager(roomID)
        self.add_new_user(self.__creatorUser)
        self.__creator_connection_state = False

    def add_new_user(self, user):
        if user in self.__userlist:
            return False
        else:
            self.__userlist[user.get_pseudo()] = user
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

    def get_playlist_manager(self):
        return self.__video_playlist

    def get_json_username_list(self):
        str_json = "{\n\t\"population\":%d," % len(self.__userlist)

        for i in self.__userlist:
            str_json += "\n\t\"%s\": {\n\t\t" % self.__userlist[i].get_pseudo() + "\"username\":\"%s\",\n\t\t" % str(self.__userlist[i].get_pseudo()) + "\"address\":\"%s\",\n\t\t" % str(self.__userlist[i].get_ip_address()) + "\"role\":\"%s\"\n\t" % str(self.__userlist[i].get_role().name) + "\n\t},"

        str_json = str_json[:-1]
        str_json += "\n}"

        return str_json