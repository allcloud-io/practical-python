import boto3
import json
import sys
import traceback

def read_image(filename):
    with open(filename, 'rb') as image:
        return image.read()

def read_image_from_s3(client, bucket, key):
    obj = client.Object(bucket, key)
    data = obj.get()['Body'].read()

    return data

def send_email(celebrities, unrecognized_faces):
    print('Sending email')

def main():
    bucket = sys.argv[1]
    key = sys.argv[2]

    s3 = boto3.resource('s3', region_name='eu-west-1')
    rek = boto3.client('rekognition', region_name='eu-west-1')

    try:
        image_data = read_image_from_s3(s3, bucket, key)
        response = rek.recognize_celebrities(Image={'Bytes': image_data})
    except:
        print('Oh no! An error has occurred. Maybe the following will help:')
        print(traceback.format_exc())
        sys.exit(1)

    celebrities = response['CelebrityFaces']
    if celebrities:
        print(f'Detected {len(celebrities)} known face(s):')
        for celebrity in celebrities:
            print(celebrity['Name'])

    unrecognized_faces = response['UnrecognizedFaces']
    if unrecognized_faces:
        print(f'Detected {len(unrecognized_faces)} unknown person(s)')

    if not celebrities and not unrecognized_faces:
        print('No faces detected')

    try:
        send_email(celebrities, unrecognized_faces)
    except:
        print('Woops! Could not send the email. Here is what we know:')
        print(traceback.format_exc())

if __name__ == "__main__":
    main()
