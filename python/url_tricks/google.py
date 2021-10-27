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

    def downloadable_drive_link(self, url: str):
        """
        Gives a downloadable url of a shared link in Google Drive
        :param url: Should a string and the link of a shared resource in google drive
        :return: if successful will return downloadable url , otherwise None
        """

        try:
            resource_id = url.split("/")[5]
            return f"https://drive.google.com/uc?id={resource_id}"
        except RuntimeError:
            return None
