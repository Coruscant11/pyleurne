from app.models.youtube_video import YoutubeVideo


class PlaylistManager:

    def __init__(self, room_id):
        self.__playlist = []
        self.__room_id = room_id

    def __str__(self):
        return "room[%s]" % self.__room_id + self.__playlist.__str__()

    def add_video(self, video_url, user):
        video = YoutubeVideo(video_url, user)

        if video.is_valid():
            self.__playlist.append(video)
            return True
        else:
            return False

    def delete_video(self, order):
        return self.__playlist.pop(order)

    def playlist_size(self):
        return len(self.__playlist)

    def get_video(self, index):
        return self.__playlist[index]

    def set_video(self, video, index):
        self.__playlist[index] = video

    def swap_videos(self, first_video_index, second_video_index):
        temp_video = self.__playlist[first_video_index]
        self.__playlist[first_video_index] = self.__playlist[second_video_index]
        self.__playlist[second_video_index] = temp_video

    def get_playlist(self):
        return self.__playlist