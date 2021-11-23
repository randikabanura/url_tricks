# URL Tricks (Python Package)

Tricks that can be done with urls of popular sites. Currently, under development.

## Examples of How To Use

### Google

```python
# Google Drive Downloadable URL
# Gives a downloadable url of a shared url in Google Drive

from url_tricks import GoogleUrlTricks
gut = GoogleUrlTricks()

gut.downloadable_drive_url("https://drive.google.com/file/d/<some_code_from_google_drive>/view?usp=sharing"

# Google Drive Web Viewer URL
# Gives a web viewer url of a shared url in Google Drive
gut.web_viewer_drive_url("https://drive.google.com/file/d/<some_code_from_google_drive>/view?usp=sharing"

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

## Developer

Name: [Banura Randika Perera](https://github.com/randikabanura) <br/>
Linkedin: [randika-banura](https://www.linkedin.com/in/randika-banura/) <br/>
Email: [randika.banura@gamil.com](mailto:randika.banura@gamil.com) <br/>
Bsc (Hons) Information Technology specialized in Software Engineering (SLIIT) <br/>