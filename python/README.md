# URL Tricks (Python Package)

Tricks that can be done with urls of popular sites. Currently, under development.

## Examples of How To Use

### Google

```python
# Google Drive Downloadable URL
# Gives a downloadable url of a shared url in Google Drive

from url_tricks import GoogleUrlTricks
gut = GoogleUrlTricks()

gut.downloadable_drive_url("https://drive.google.com/file/d/<some_code_from_google_drive>/view?usp=sharing")

# Google Drive Web Viewer URL
# Gives a web viewer url of a shared url in Google Drive
gut.web_viewer_drive_url("https://drive.google.com/file/d/<some_code_from_google_drive>/view?usp=sharing")

# Google Docs Previewable URL
# Gives a previewable url of a shared url in Google Docs
gut.previewable_docs_url("https://docs.google.com/document/d/<some_code_from_google_docs>/edit")

# Google Docs Templatable URL
# Gives a templatable url of a shared url in Google Docs
gut.templatable_docs_url("https://docs.google.com/document/d/<some_code_from_google_docs>/edit")

# Google Docs Exportable URL
# Gives an exportable url of a shared url in Google Docs / Google Sheets
# Some possible values for "export_type" is "pdf", "odt" and "docx"
# exportable_sheets_url would do the same functionality
gut.exportable_docs_url("https://docs.google.com/document/d/<some_code_from_google_docs>/edit", "odt")
```

### Youtube

```python
# Youtube current time URL
# Gives a current time url of a url in Youtube video

from url_tricks import YoutubeUrlTricks
yut = YoutubeUrlTricks()

yut.current_time_url("https://www.youtube.com/watch?v=<video_id>", 150)

# Youtube thumbnail URL
# Gives a thumbnail url of a url in Youtube video
yut.thumbnail_url("https://www.youtube.com/watch?v=<video_id>")
```

## Developer

Name: [Banura Randika Perera](https://github.com/randikabanura) <br/>
Linkedin: [randika-banura](https://www.linkedin.com/in/randika-banura/) <br/>
Email: [randika.banura@gamil.com](mailto:randika.banura@gamil.com) <br/>
Bsc (Hons) Information Technology specialized in Software Engineering (SLIIT) <br/>