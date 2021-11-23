"""
This module implements the main Youtube functionality of url tricks for python package.
Author: Banura Randika Perera
Github: https://github.com/randikabanura
"""

__author__ = "Banura Randika Perera"
__email__ = "randika.banura@gmail.com"
__status__ = "planning"

from urllib.parse import urlparse
from urllib.parse import parse_qs


class YoutubeUrlTricks:
    """
    Class for the youtube url tricks
    """

    def __init__(self):
        """
        Creates a new instance of YoutubeUrlTricks
        """

    def current_time_url(self, url: str, time_in_seconds: int = 0):
        """
        Gives a url with a preconfigured start time
        :param url: Youtube video url
        :param time_in_seconds: How many seconds in the video it should start
        :return: if successful will return youtube time configured url, otherwise None
        """
        try:
            return f"{url}&t={time_in_seconds}"
        except (RuntimeError, IndexError):
            return None

    def thumbnail_url(self, url: str):
        """
        Gives a url to videos thumbnail
        :param url: Youtube video url
        :return: if successful will return youtube thumbnail url, otherwise None
        """
        try:
            parsed_url = urlparse(url)
            video_id = parse_qs(parsed_url.query)['v'][0]
            return f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        except (RuntimeError, IndexError):
            return None
