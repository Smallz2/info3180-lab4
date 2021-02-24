from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
  file = FileField("", validators=[FileRequired(),
                   FileAllowed(['jpg', 'png'])])
