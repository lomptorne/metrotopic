import requests
import os
import shutil
import json
from django.http import HttpResponse

from celery import shared_task 
from celery_progress.backend import ProgressRecorder
from time import sleep 
from pathlib import Path
from django.conf import settings

@shared_task(bind=True)
def collecteur(self, hashtag, imgNbr):

    # Set the function variable
    results =[]
    path = os.getcwd()
    url = "https://www.instagram.com/explore/tags/{}/?__a=1".format(hashtag)
    page = requests.get(url)
    counter_progress = 0
    progress_recorder = ProgressRecorder(self)
    print(page)
    print(hashtag)
    print(imgNbr)
    print(url)


    jsonDump = requests.get(url).json()['graphql']['hashtag']['edge_hashtag_to_media']['edges']

    print(jsonDump)

    # Append the results from the json to a link list
    for node in jsonDump :
        counter_progress += 1

        if counter_progress > imgNbr :
            counter_progress = imgNbr

        progress_recorder.set_progress(counter_progress, imgNbr, "Fetching : ")
        results.append(node['node']['display_url'])

    # if there is not enough image in the first page then scroll to more results until it reachs the user input
    if len(results) <= imgNbr and len(results) > 69:
        
        while len(results) < imgNbr :

            # Modifying the url in order to scroll the pages
            urlnext  =  url + "&max_id=" + page.json()['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
            page = requests.get(urlnext)
            jsonDump = page.json()['graphql']['hashtag']['edge_hashtag_to_media']['edges']

            # Add the new results to the list
            for node in jsonDump :
                counter_progress += 1
                if counter_progress > imgNbr :
                    counter_progress = imgNbr
                progress_recorder.set_progress(counter_progress, imgNbr, "Fetching : ")
                results.append(node['node']['display_url'])
    counter_progress = 0

    # Reduce the list size to make it the same number as user input
    if len(results) > imgNbr : 
        accuration = len(results) - imgNbr
        results = results[:-accuration]
    
    # Create the folder to contian the images
    try:
        dir_name =  settings.MEDIA_ROOT + '/{}'.format(hashtag)
        os.makedirs(dir_name)
        os.chdir(dir_name)

    except OSError:
        os.chdir(dir_name)
    

    for image in results : 

        # Set the loop variables and update progressbar
        progress_recorder.set_progress(counter_progress, imgNbr, "Downloading : ")
        counter_progress += 1
        counter_name = counter_progress

        # Create the file if file depending on file already present in the folder
        try:
            response = requests.get(image)
            filename = str(counter_name) + ".jpg"
            while os.path.isfile('./{}'.format(filename)) is True :
                counter_name +=1
                filename = str(counter_name) + ".jpg"	
        except:
            continue

        # Write data in the file
        try:
            f = open(filename, "wb")
            f.write(response.content)
            f.close()
        except :
            raise("Error Writing Files")

    # Reinit the name counter and the path and set the result
    os.chdir(settings.MEDIA_ROOT)	
    counter_name = 0



    filename = hashtag + ".zip"
    while os.path.isfile('./{}'.format(filename)) is True :
        counter_name +=1
        filename = hashtag + "({})".format(str(counter_name)) + ".zip"

    filename = filename[:-4]
    progress_recorder.set_progress(imgNbr, imgNbr, "Compressing : ")
    shutil.make_archive( settings.MEDIA_ROOT + '/{}'.format(filename), 'zip',  settings.MEDIA_ROOT + '/{}'.format(hashtag))
    shutil.rmtree(settings.MEDIA_ROOT + '/{}'.format(hashtag), ignore_errors=False, onerror=None)
    resulte = str(filename + ".zip")

    return resulte