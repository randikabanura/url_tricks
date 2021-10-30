"""
This module implements the main functionality of url tricks for python package.
Author: Banura Randika Perera
Gothub: https://github.com/randikabanura
"""

__author__ = "Banura Randika Perera"
__email__ = "randika.banura@gmail.com"
__status__ = "planning"


class GoogleUrlTricks:
    """
    Class for the google url tricks
    """

    def __init__(self):
        """
        Creates a new instance of GoogleUrlTricks
        """

    def downloadable_drive_url(self, url: str):
        """
        Gives a downloadable url of a shared link in Google Drive
        :param url: Should be a string and the link of a shared resource in google drive
        :return: if successful will return downloadable url, otherwise None
        """

        try:
            resource_id = url.split("/")[5]
            return f"https://drive.google.com/uc?id={resource_id}"
        except (RuntimeError, IndexError):
            return None

    def previewable_docs_url(self, url: str):
        """
        Gives a previewable url form the docs url
        :param url: Should be a string and the url of a shared resource in google docs
        :return: if successful will return previewable url, otherwise None
        """

        try:
            split_url = url.split("/")
            main_url = "/".join(split_url[:6])
            return f"{main_url}/preview"
        except (RuntimeError, IndexError):
            return None