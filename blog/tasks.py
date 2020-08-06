
import json
import os
import shutil
import requests
import uuid
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, redirect

from celery import shared_task 
from celery_progress.backend import ProgressRecorder
from time import sleep 
from pathlib import Path
from django.conf import settings

@shared_task(bind=True)
def collecteur(self, data):

    # Set the function variable
    path = os.getcwd()
    imgNbr = len(data)
    urlList = data
    counter_progress = 0
    filename = str(uuid.uuid4())
    progress_recorder = ProgressRecorder(self)
    
    # Create the folder to contian the images
    try:
        dir_name =  settings.MEDIA_ROOT + '/{}'.format(filename)
        os.makedirs(dir_name)
        os.chdir(dir_name)

    except OSError:
        os.chdir(dir_name)
    
    for image in urlList : 
        
        # Set the loop variables and update progressbar
        progress_recorder.set_progress(counter_progress, imgNbr, "Downloading : ")
        counter_progress += 1
        counter_name = counter_progress

        # Create the file if file depending on file already present in the folder
        try:
            response = requests.get(image)
            imgName = str(counter_name) + ".jpg"
            while os.path.isfile('./{}'.format(imgName)) is True :
                counter_name +=1
                imgName = str(counter_name) + ".jpg"	
        except:
            continue

        # Write data in the file
        try:
            f = open(imgName, "wb")
            f.write(response.content)
            f.close()
        except :
            raise("Error Writing Files")

    # Reinit the name counter and the path and set the result
    os.chdir(settings.MEDIA_ROOT)	
    counter_name = 0



    filenom = filename + ".zip"
    while os.path.isfile('./{}'.format(filenom)) is True :
        counter_name +=1
        filenom = filename + "({})".format(str(counter_name)) + ".zip"

    filenom = filenom[:-4]
    progress_recorder.set_progress(imgNbr, imgNbr, "Compressing : ")
    shutil.make_archive( settings.MEDIA_ROOT + '/{}'.format(filenom), 'zip',  settings.MEDIA_ROOT + '/{}'.format(filename))
    shutil.rmtree(settings.MEDIA_ROOT + '/{}'.format(filename), ignore_errors=False, onerror=None)
    resulte = str(filenom + ".zip")

    return resulte