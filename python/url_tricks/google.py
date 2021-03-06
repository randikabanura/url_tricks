
"""
This module implements the main Google functionality of url tricks for python package.
Author: Banura Randika Perera
Github: https://github.com/randikabanura
"""

__author__ = "Banura Randika Perera"
__email__ = "randika.banura@gmail.com"
__status__ = "planning"

from urllib.parse import urlparse


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
        Gives a downloadable url of a shared url in Google Drive
        :param url: Should be a string and the url of a shared resource in google drive
        :return: if successful will return downloadable url, otherwise None
        """

        try:
            url_scheme = urlparse(url).scheme

            if url_scheme is None or url_scheme == '':
                resource_id = url.split("/")[3]
            else:
                resource_id = url.split("/")[5]

            return f"https://drive.google.com/uc?id={resource_id}"
        except Exception:
            return None

    def web_viewer_drive_url(self, url: str):
        """
        Gives a web viewer url of a shared url in Google Drive
        :param url: Should be a string and the url of a shared resource in google drive
        :return: if successful will return web viewer  url, otherwise None
        """

        try:
            url_scheme = urlparse(url).scheme

            if url_scheme is None or url_scheme == '':
                resource_id = url.split("/")[3]
            else:
                resource_id = url.split("/")[5]

            return f"https://docs.google.com/viewer?url={resource_id}"
        except Exception:
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
        except Exception:
            return None

    def templatable_docs_url(self, url: str):
        """
        Gives a templatable url form the docs url
        :param url: Should be a string and the url of a shared resource in google docs
        :return: if successful will return templatable url, otherwise None
        """

        try:
            split_url = url.split("/")
            main_url = "/".join(split_url[:6])
            return f"{main_url}/template/preview"
        except Exception:
            return None

    def exportable_docs_url(self, url: str, export_type: str = "pdf"):
        """
        Gives a exportable url form the docs url
        :param export_type: Type of the export needed such as pdf, docx and odt, Default is "pdf"
        :param url: Should be a string and the url of a shared resource in google docs
        :return: if successful will return exportable url, otherwise None
        """

        try:
            split_url = url.split("/")
            main_url = "/".join(split_url[:6])
            return f"{main_url}/export?format={export_type}"
        except Exception:
            return None

    def exportable_sheets_url(self, url: str, export_type: str = "pdf"):
        """
        Alias method to call "exportable_docs_url" method
        """
        self.exportable_docs_url(url, export_type)
