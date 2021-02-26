import os

def get_uploaded_images():
  rootdir = os.getcwd()
    
  for subdir, dirs, files in os.walk(rootdir + '/uploads'):
    return [file for file in files if file.endswith('.jpg') or file.endswith('.png')]
  pass