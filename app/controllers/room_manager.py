from random import randint

from app.models.rooms import Room


class RoomManager:

    def __init__(self):
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