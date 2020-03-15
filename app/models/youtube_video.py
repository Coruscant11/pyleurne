import urllib.parse as urlparse
from urllib.parse import parse_qs


class YoutubeVideo:

    def __init__(self, url, caller_user):
        self.__url = url
        self.__callerUser = caller_user
        self.__is_url_valid = False
        self.__video_id = "0"

        self.__validate_url()

    def __str__(self):
        return "URL[%s] - asked by user[%s]" % (self.__url, self.__callerUser)

    def __validate_url(self):
        self.__video_id = None
        url = self.__url
        parsed = urlparse.urlparse(url)

        if parsed.hostname == "youtu.be":
            self.__video_id = parsed.path[1:]
            self.__is_url_valid = True
        elif parsed.hostname == "www.youtube.com":
            self.__video_id = parse_qs(parsed.query)['v'][0]
            self.__is_url_valid = True
        else:
            self.__video_id = "0"
            self.__is_url_valid = False

        return self.__is_url_valid

    def is_valid(self):
        return self.__is_url_valid

    def get_video_url(self):
        return self.__url

    def set_video_url(self, url):
        self.__url = url

    def get_caller(self):
        return self.__callerUser

    def get_video_id(self):
        return self.__video_id
