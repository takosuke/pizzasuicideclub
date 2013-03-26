from flask import Flask, safe_join, request
from werkzeug import secure_filename
import os, datetime, random
from psc_app import app

STATIC = app.config['STATIC']
ALLOWED_EXTENSIONS = app.config['ALLOWED_EXTENSIONS']
UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def file_save(file, category):
    if file and allowed_file(file.filename):
        extension = secure_filename(file.filename).rsplit('.', 1)[1]
        foldername = safe_join (category, datetime.date.today().strftime('%Y%m'))
        filename = (datetime.date.today().strftime('%Y%m%d')) + str(random.randint(1000, 9999))+ '.' + extension
        image_rel_path = safe_join(foldername, filename)
        category_folder = safe_join(UPLOAD_FOLDER, category)
        save_folder = safe_join(UPLOAD_FOLDER, foldername)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        full_save_path = safe_join(save_folder, filename)
        file.save(full_save_path)
        return image_rel_path
    return None

