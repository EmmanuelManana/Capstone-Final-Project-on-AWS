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
        #read bytes
        imgFile = open('/tmp/dog.jpg', 'rb')
        imgBytes = imgFile.read()
        imgFile.clode()
    except:
        print('Could not read the file')
        
    imgobj = {'Bytes': imgBytes}
    response_labels = client.detect_labels(Image = imgobj)
    
    print(response_labels)
    
    return {
        'body' : json.dumps(response_labels)
    }

# response_labels, model was able to detect the image and identy its contents.
# {'Labels': [{'Name': 'Manga', 'Confidence': 99.71334075927734, 'Instances': [], 'Parents': [{'Name': 'Comics'}, {'Name': 'Book'}]}, {'Name': 'Comics', 'Confidence': 99.71334075927734, 'Instances': [], 'Parents': [{'Name': 'Book'}]}, {'Name': 'Book', 'Confidence': 99.71334075927734, 'Instances': [], 'Parents': []}, {'Name': 'Person', 'Confidence': 78.16822814941406, 'Instances': [{'BoundingBox': {'Width': 0.5692188143730164, 'Height': 0.9165003895759583, 'Left': 0.3229805827140808, 'Top': 0.05902675911784172}, 'Confidence': 78.16822814941406}], 'Parents': []}, {'Name': 'Human', 'Confidence': 78.16822814941406, 'Instances': [], 'Parents': []}], 'LabelModelVersion': '2.0', 'ResponseMetadata': {'RequestId': '65ab097b-a990-4f32-b756-08dde75d51d9', 'HTTPStatusCode': 200, 'HTTPHeaders': {'content-type': 'application/x-amz-json-1.1', 'date': 'Thu, 04 Feb 2021 21:48:39 GMT', 'x-amzn-requestid': '65ab097b-a990-4f32-b756-08dde75d51d9', 'content-length': '622', 'connection': 'keep-alive'}, 'RetryAttempts': 0}}
# END RequestId: bd06dd56-3a78-496c-92fe-2725f46bf2f3
# REPORT RequestId: bd06dd56-3a78-496c-92fe-2725f46bf2f3	Duration: 1150.17 ms	Billed Duration: 1151 ms	Memory Size: 128 MB	Max Memory Used: 79 MB	
