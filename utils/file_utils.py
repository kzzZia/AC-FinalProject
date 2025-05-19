# utils/file_utils.py
import os

def save_uploaded_file(uploaded_file, folder='uploads'):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, uploaded_file.filename)
    uploaded_file.save(path)
    return path
