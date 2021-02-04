import json
import sys
import os
import boto3
import base64

def write_to_file(save_path, data):
    # doc strings here
    with open(save_path, "wb") as file:
        file.write(base64.b64decode(data))

def lambda_handler(event, context):
    # doc strings here
    client =  boto3.client('rekognition')
    encodedImage = event['photo']
    # trim the string
    encodedImage = encodedImage[23:] 
    
    write_to_file('/tmp/dog.jpg', encodedImage) 
    
    try:
        #read as bytes
        imgFile = open('/tmp/dog.jpg', 'rb')
        imgBytes = imgFile.read()
        imgFile.clode()
    except:
        print('Could not read the file')
        
    imgobj = {'Bytes': imgBytes}
    
    return {
        
    }
